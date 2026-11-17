param(
    [Parameter(Mandatory = $true)]
    [string] $ScriptDomPath
)
$ErrorActionPreference = 'Stop'
Add-Type -Path $ScriptDomPath
$parser = [Microsoft.SqlServer.TransactSql.ScriptDom.TSql140Parser]::new($true)
$entries = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'curriculum.json') -Raw | ConvertFrom-Json
$entries += Get-Content -LiteralPath (Join-Path $PSScriptRoot 'domain_reports.json') -Raw | ConvertFrom-Json
$entries += Get-Content -LiteralPath (Join-Path $PSScriptRoot 'advanced_queries.json') -Raw | ConvertFrom-Json
$failures = [System.Collections.Generic.List[object]]::new()
$checked = 0
$seenInterviewSql = [System.Collections.Generic.HashSet[string]]::new()
foreach ($entry in $entries) {
    if (-not $entry.sql) { continue }
    $null = $seenInterviewSql.Add($entry.sql)
    $parseErrors = $null
    $reader = [System.IO.StringReader]::new($entry.sql)
    $null = $parser.Parse($reader, [ref] $parseErrors)
    $reader.Dispose()
    $checked++
    foreach ($parseError in $parseErrors) {
        $failures.Add([pscustomobject]@{id=$entry.id; line=$parseError.Line; message=$parseError.Message})
    }
}
$interviewPath = Join-Path $PSScriptRoot 'domain_interview_questions.jsonl'
if (Test-Path -LiteralPath $interviewPath) {
    foreach ($line in [System.IO.File]::ReadLines($interviewPath)) {
        $interviewEntry = $line | ConvertFrom-Json
        foreach ($sqlText in @($interviewEntry.reference.sql, $interviewEntry.reference.witness_sql)) {
            if (-not $sqlText -or -not $seenInterviewSql.Add($sqlText)) { continue }
            $parseErrors = $null
            $reader = [System.IO.StringReader]::new($sqlText)
            $null = $parser.Parse($reader, [ref] $parseErrors)
            $reader.Dispose()
            $checked++
            foreach ($parseError in $parseErrors) {
                $failures.Add([pscustomobject]@{id=$interviewEntry.id; line=$parseError.Line; message=$parseError.Message})
            }
        }
    }
}
$sqlFiles = @(Get-ChildItem -LiteralPath (Join-Path $PSScriptRoot 'setup') -Filter '*.sql')
$sqlFiles += @(Get-ChildItem -LiteralPath (Join-Path $PSScriptRoot 'domains') -Filter '*.sql' -Recurse)
foreach ($file in $sqlFiles) {
    $parseErrors = $null
    $reader = [System.IO.StringReader]::new((Get-Content -LiteralPath $file.FullName -Raw))
    $null = $parser.Parse($reader, [ref] $parseErrors)
    $reader.Dispose()
    $checked++
    foreach ($parseError in $parseErrors) {
        $failures.Add([pscustomobject]@{id=$file.Name; line=$parseError.Line; message=$parseError.Message})
    }
}
$report = [ordered]@{
    parser = 'Microsoft ScriptDom TSql140Parser (SQL Server 2017 grammar)'
    assemblyVersion = [Microsoft.SqlServer.TransactSql.ScriptDom.TSql140Parser].Assembly.GetName().Version.ToString()
    blocksChecked = $checked
    errors = @($failures.ToArray())
    runtimeExecuted = $false
}
$report | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'SYNTAX_VALIDATION.json') -Encoding utf8
if ($failures.Count) {
    $failures | Format-Table -AutoSize
    throw "$($failures.Count) SQL parse errors in $checked blocks."
}
Write-Output "Passed: $checked SQL blocks; zero parse errors. No database execution performed."
