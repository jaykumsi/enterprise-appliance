"""Where each company's SQL data lives.

Company data (data_setup.sql, seed.sql, schema_solution.sql, questions/, solutions/) lives in
domains/<company folder>/sql, next to that company's home page. The scripts in this folder use
domain_dir(slug) instead of a hard-coded path.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent          # domains/SQL/Excerises
DOMAINS_ROOT = ROOT.parent.parent               # domains/
ASSIGNMENTS_INDEX = ROOT / 'DOMAIN_ASSIGNMENTS.md'

FOLDERS = {
    'banking': 'bank-harborstone',
    'brokerage': 'brokerage-ridgeline',
    'ecommerce': 'ecommerce-everyday-bazaar',
    'healthcare': 'healthcare-amerimed',
    'oil': 'oil-permian-ridge',
    'pharma': 'pharma-novacrest',
    'retail': 'retail-maple-main-stores',
    'retail_logistics': 'retail-logistics-maple-main',
    'retail_supply_chain': 'retail-supply-chain-maple-main',
}


def domain_dir(slug):
    """domains/<company folder>/sql for a domain slug such as 'banking'."""
    return DOMAINS_ROOT / FOLDERS[slug] / 'sql'


def domain_dirs():
    """Every company's sql folder."""
    return [domain_dir(s) for s in FOLDERS]


def domain_link(slug, from_dir):
    """Relative link (forward slashes) from from_dir to a company's sql folder, for generated Markdown."""
    import os
    return os.path.relpath(domain_dir(slug), from_dir).replace(os.sep, '/')


def slug_of(directory):
    """Domain slug for a company sql folder returned by domain_dir()/domain_dirs()."""
    from pathlib import Path
    folder = Path(directory).resolve().parent.name
    return {v: k for k, v in FOLDERS.items()}[folder]
