# Nurse Practitioner Job Search System

## Overview
Automated job search system for nurse practitioners in the Raleigh, NC area with organized reporting and historical tracking.

## Folder Structure
```
search_reports/
├── YYYY/MM/DD/RUN_NUMBER/
│   ├── run_metadata.json          # Run information and statistics
│   ├── consolidated_np_job_analysis.json  # Complete analysis with scores
│   ├── np_market_analysis_report.json     # Market intelligence
│   ├── np_job_application_strategy.json   # Application priorities  
│   ├── np_job_search_executive_summary.md # Executive summary
│   ├── np_job_search_with_application_links.md # Application guide
│   ├── major_job_boards_data.json         # Raw data from job boards
│   ├── healthcare_systems_data.json       # Raw data from health systems
│   ├── specialty_nursing_boards_data.json # Raw data from specialty boards
│   └── government_healthcare_data.json    # Raw data from government
```

## Current Reports

### Latest Search: 2025/08/03/1 (Comprehensive FNP Search)
- **164+ positions** identified across Triangle area
- **Critical deadlines:** DOD (Aug 6), VA (Aug 11) 
- **Top employers:** Duke Health, Novant Health, VA, UNC Health

**Key Files:**
- 📋 **Application Guide:** [`search_reports/2025/08/03/1/np_job_search_with_application_links.md`](search_reports/2025/08/03/1/np_job_search_with_application_links.md)
- 📊 **Executive Summary:** [`search_reports/2025/08/03/1/np_job_search_executive_summary.md`](search_reports/2025/08/03/1/np_job_search_executive_summary.md)
- 🔍 **Complete Analysis:** [`search_reports/2025/08/03/1/consolidated_np_job_analysis.json`](search_reports/2025/08/03/1/consolidated_np_job_analysis.json)

## Quick Commands

### View All Search Runs:
```bash
python search_report_manager.py
```

### Start New Search:
```bash
/np-search [specialty_focus]
```

### View Latest Results:
```bash
ls search_reports/2025/08/03/1/
```

## System Components

1. **Search Agents** (4 specialized agents):
   - `major-job-boards`: LinkedIn, Indeed, Glassdoor, ZipRecruiter, SimplyHired
   - `healthcare-systems`: Duke Health, Novant Health, Atrium Health, UNC Health  
   - `specialty-nursing-boards`: AANP, Nurse.com, nursing-specific platforms
   - `government-healthcare`: USAJOBS, VA, state/local government

2. **Job Analyzer Agent**: Consolidates, deduplicates, scores, and ranks opportunities

3. **Report Manager**: Handles folder structure and run numbering

## Next Steps

🚨 **IMMEDIATE ACTION (Aug 3, 2025):**
1. Apply to DOD Neonatal NP (closes Aug 6): https://www.usajobs.gov/job/841983100
2. Apply to VA Intensivist (closes Aug 11): https://www.usajobs.gov/job/841942600
3. Review top Duke Health positions with direct application links

📈 **Market Intelligence:**
- Federal positions: $180K-$240K+ total compensation
- Academic medical centers: $105K-$135K
- High demand for PMHNP: $110K-$150K+
- 40-60% interview rate expected for qualified candidates