# Domains: one folder per company

Each fictional company has its own folder with a home page, an Assignments tab, a Control Tower tab
(placeholder for now) and an `sql` subfolder holding its data, student questions and private instructor solutions.
Open [the site index](../index.html) to browse them.

| Company | Industry | Folder |
|---|---|---|
| Harborstone Bank | Banking | [bank-harborstone](bank-harborstone/index.html) |
| Ridgeline Securities | Brokerage | [brokerage-ridgeline](brokerage-ridgeline/index.html) |
| Everyday Bazaar | E-commerce | [ecommerce-everyday-bazaar](ecommerce-everyday-bazaar/index.html) |
| AmeriMed Healthcare | Healthcare | [healthcare-amerimed](healthcare-amerimed/index.html) |
| Permian Ridge Energy | Oil & Gas | [oil-permian-ridge](oil-permian-ridge/index.html) |
| Novacrest Pharmaceuticals | Pharma | [pharma-novacrest](pharma-novacrest/index.html) |
| Maple & Main Stores | Retail | [retail-maple-main-stores](retail-maple-main-stores/index.html) |
| Maple & Main Supply Chain | Retail Supply Chain | [retail-supply-chain-maple-main](retail-supply-chain-maple-main/index.html) |
| Maple & Main Distribution | Retail Logistics | [retail-logistics-maple-main](retail-logistics-maple-main/index.html) |

## Inside each company folder

```
<company>/
  index.html           home page (header: Home · Assignments · Control Tower)
  assignments.html     Assignments tab
  control-tower.html   Control Tower tab (placeholder)
  sql/
    schema_solution.sql, seed.sql   small sample fixture
    data_setup.sql                  large practice dataset
    questions/                      student assignments (shareable)
    solutions/                      instructor answers (keep private)
```

## Shared SQL curriculum

[SQL/Excerises](SQL/Excerises/README.md) holds the shared lessons, the generator and validation scripts and
the [SQL assignments index](SQL/Excerises/DOMAIN_ASSIGNMENTS.md). The scripts find each company's data through
`SQL/Excerises/company_paths.py`. Regenerate the HTML pages with `python build_site.py` from the repository root.
