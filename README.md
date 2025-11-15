
# Healthcare Analytics Portfolio (Synthetic)

All datasets are **synthetic** and anonymized.

## Highlights for reviewers
- **Patient Experience** — bar chart of mean scores by department → `01-patient-experience/outputs/fig_likert_by_department.png`
- **Readmissions** — 30-day rate by risk decile → `02-readmissions-risk/outputs/fig_readmit_rate_by_decile.png`
- **Claims Cleaning** — canonicalized providers → `03-claims-cleaning/outputs/claims_clean.csv`
- **Auto Report** — `04-reporting-automation/outputs/report.md`
- **SPSS Snippet** — `05-spss-syntax/recode_overall.sps`

## Run locally
```bash
python 01-patient-experience/src/analyze_experience.py
python 02-readmissions-risk/src/analyze_readmissions.py
python 03-claims-cleaning/src/clean_claims.py
python 04-reporting-automation/src/generate_report.py
```

> No proprietary or protected health information (PHI) is included. Everything here is synthetic.
