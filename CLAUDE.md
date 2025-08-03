# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## System Overview

This is an automated nurse practitioner job search system for the Raleigh, NC area that uses specialized agents to collect, analyze, and rank job opportunities. The system operates through a coordinated workflow of four search agents, data consolidation, analysis, and structured reporting with historical tracking.

## Core Architecture

### Multi-Agent Search System
The system uses four specialized search agents that run in parallel:

- **major-job-boards**: Searches LinkedIn, Indeed, Glassdoor, ZipRecruiter, SimplyHired
- **healthcare-systems**: Monitors Duke Health, Novant Health, Atrium Health, UNC Health career pages  
- **specialty-nursing-boards**: Browses AANP, Nurse.com, and nursing-specific platforms
- **government-healthcare**: Searches USAJOBS, VA, state/local government positions

### Data Flow Architecture
1. **Collection Phase**: Four agents collect raw job data in parallel
2. **Analysis Phase**: `job-analyzer` agent consolidates, deduplicates, and scores positions
3. **Reporting Phase**: Generate structured reports with application links and market intelligence
4. **Storage Phase**: Save all data to timestamped, hierarchical folder structure

### Report Management System
The `SearchReportManager` class handles:
- Automatic folder creation with `YYYY/MM/DD/RUN_NUMBER/` structure
- Monotonic run numbering (starts at 1, increments per day)
- Metadata tracking and standardized file naming
- Historical run comparison and analysis

## Essential Commands

### Execute Complete Job Search
```bash
/np-search [specialty_focus]  # Main command to run full search workflow
```

### View Search History
```bash
python search_report_manager.py  # List all previous search runs
```

### Access Latest Results
```bash
ls search_reports/YYYY/MM/DD/N/  # View files from specific run
```

## File Structure and Data Standards

### Required Output Files Per Run
Each search run must generate these standardized files:
- `run_metadata.json` - Run statistics and configuration
- `consolidated_np_job_analysis.json` - Complete analysis with position scores
- `np_market_analysis_report.json` - Market intelligence dashboard
- `np_job_application_strategy.json` - Application priority matrix
- `np_job_search_executive_summary.md` - Executive summary for users
- `np_job_search_with_application_links.md` - Complete application guide with direct URLs
- `major_job_boards_data.json` - Raw data from job boards
- `healthcare_systems_data.json` - Raw data from health systems
- `specialty_nursing_boards_data.json` - Raw data from specialty boards
- `government_healthcare_data.json` - Raw data from government sources

### Critical Data Requirements
Every job position must include:
- `application_url` - Direct link to apply
- `posting_url` - Link to job listing
- `source` - Platform where job was found
- `position_id` - Unique identifier
- Scoring data (1-100 scale with breakdown)

## Working with the Job Analyzer Agent

### Agent Integration Protocol
When launching search agents, use the Task tool with specific subagent types:
- `major-job-boards`
- `healthcare-systems` 
- `specialty-nursing-boards`
- `government-healthcare`
- `job-analyzer`

### Required Workflow for New Searches
1. Initialize new search run using `SearchReportManager.setup_new_search_run()`
2. Launch all four search agents in parallel with Task tool
3. Run job-analyzer agent to consolidate and rank results
4. Ensure all required files are generated with application URLs
5. Update run metadata with final statistics

### Scoring Methodology
The job-analyzer uses weighted scoring (1-100):
- Compensation (30%): Salary, benefits, bonuses, loan forgiveness
- Growth Potential (25%): Career advancement, academic affiliation
- Work-Life Balance (20%): Schedule flexibility, call requirements
- Location (15%): Proximity to Triangle area
- Employer Stability (10%): Organization reputation

## Key System Behaviors

### Run Number Management
- Run numbers are monotonically increasing per day
- First run of any day starts at 1
- System automatically detects next available run number
- Each run gets isolated folder structure for data integrity

### Agent Coordination
- All search agents run in parallel for efficiency
- job-analyzer agent waits for all search agents to complete
- Application URLs are mandatory - searches fail if URLs missing
- Deduplication occurs across all data sources

### Report Generation Requirements
- Executive summaries must highlight time-sensitive opportunities
- Application guides must include direct URLs for all top positions
- Market analysis must include salary trends and demand analysis
- All reports must be generated in both JSON and Markdown formats