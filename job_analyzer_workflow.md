# Job Analyzer Agent - Enhanced Workflow with Folder Management

## Overview
The job analyzer agent consolidates, deduplicates, and ranks job opportunities from all search agents, now with proper folder structure and run tracking.

## Folder Structure Requirements

### Standard Directory Structure:
```
/home/jhjaggars/code/jobsearch/search_reports/
├── YYYY/
│   ├── MM/
│   │   ├── DD/
│   │   │   ├── 1/
│   │   │   │   ├── run_metadata.json
│   │   │   │   ├── consolidated_np_job_analysis.json
│   │   │   │   ├── np_market_analysis_report.json
│   │   │   │   ├── np_job_application_strategy.json
│   │   │   │   ├── np_job_search_executive_summary.md
│   │   │   │   ├── np_job_search_with_application_links.md
│   │   │   │   ├── major_job_boards_data.json
│   │   │   │   ├── healthcare_systems_data.json
│   │   │   │   ├── specialty_nursing_boards_data.json
│   │   │   │   └── government_healthcare_data.json
│   │   │   ├── 2/
│   │   │   └── N/
```

## Required Workflow Steps

### Step 1: Initialize Search Run
```python
from search_report_manager import SearchReportManager

# Create new run folder
manager = SearchReportManager()
run_path, metadata = manager.setup_new_search_run(
    search_type="comprehensive",  # or "specialty", "government_only", etc.
    specialty_focus="FNP"  # or "PMHNP", "ACNP", etc.
)

# Get standardized file paths
file_paths = manager.get_standard_file_paths(run_path)
```

### Step 2: Data Collection & Storage
When collecting data from search agents, save to standardized file paths:

```python
# Save data from each agent to specific files
save_data(major_job_boards_data, file_paths["major_job_boards"])
save_data(healthcare_systems_data, file_paths["healthcare_systems"])
save_data(specialty_boards_data, file_paths["specialty_boards"])
save_data(government_data, file_paths["government_data"])
```

### Step 3: Analysis & Consolidation
Create consolidated analysis file:

```python
# Consolidate all data sources
consolidated_analysis = {
    "analysis_metadata": {
        "analysis_date": datetime.now().isoformat(),
        "run_number": metadata["run_info"]["run_number"],
        "total_positions_consolidated": total_count,
        "data_sources": [
            f"Major job boards - {major_boards_count} positions",
            f"Healthcare systems - {health_systems_count} positions", 
            f"Specialty nursing boards - {specialty_count} positions",
            f"Government healthcare - {government_count} positions"
        ],
        "deduplication_performed": True,
        "unique_positions_analyzed": unique_count,
        "geographic_focus": "Raleigh, NC Triangle Area"
    },
    "scoring_methodology": { ... },
    "top_opportunities": [ ... ],
    "market_intelligence": { ... }
}

# Save to standardized path
save_json(consolidated_analysis, file_paths["consolidated_analysis"])
```

### Step 4: Generate Reports
Create all required report files:

1. **Market Analysis Report** (`np_market_analysis_report.json`)
2. **Application Strategy** (`np_job_application_strategy.json`)
3. **Executive Summary** (`np_job_search_executive_summary.md`)
4. **Application Links Guide** (`np_job_search_with_application_links.md`)

### Step 5: Update Run Metadata
```python
# Update metadata with final statistics
metadata["results"] = {
    "total_positions": total_count,
    "unique_positions": unique_count,
    "top_score": max_score,
    "analysis_completed": datetime.now().isoformat(),
    "files_generated": list(file_paths.keys())
}

# Save updated metadata
save_json(metadata, file_paths["metadata"])
```

## File Naming Standards

### Required JSON Files:
- `run_metadata.json` - Run information and statistics
- `consolidated_np_job_analysis.json` - Complete analysis with scores
- `np_market_analysis_report.json` - Market intelligence dashboard
- `np_job_application_strategy.json` - Application priority matrix
- `major_job_boards_data.json` - Raw data from major job boards
- `healthcare_systems_data.json` - Raw data from health systems
- `specialty_nursing_boards_data.json` - Raw data from specialty boards
- `government_healthcare_data.json` - Raw data from government sources

### Required Markdown Files:
- `np_job_search_executive_summary.md` - Executive summary for users
- `np_job_search_with_application_links.md` - Complete application guide

## Data Structure Requirements

### Run Metadata Structure:
```json
{
  "run_info": {
    "timestamp": "2025-08-03T10:30:00",
    "date": "2025-08-03", 
    "run_number": 1,
    "search_type": "comprehensive",
    "specialty_focus": "FNP"
  },
  "folder_structure": { ... },
  "data_sources": { ... },
  "results": {
    "total_positions": 164,
    "unique_positions": 158,
    "top_score": 94.5,
    "analysis_completed": "2025-08-03T12:45:00",
    "files_generated": [...]
  }
}
```

### Job Position Data Structure:
```json
{
  "position_id": "unique_identifier",
  "title": "Job Title",
  "employer": "Organization Name",
  "location": { "city": "City", "state": "State" },
  "salary_range": { "min": 100000, "max": 130000 },
  "application_url": "https://direct.link.to.application",
  "posting_url": "https://job.board.listing.url",
  "source": "linkedin|duke_health|usajobs|etc",
  "specialty": "primary_care|urgent_care|specialty|etc",
  "score": 89.7,
  "score_breakdown": { ... },
  "requirements": [...],
  "benefits": [...],
  "deadline": "2025-08-15"
}
```

## Integration with Search Agents

### When launching search agents, provide run information:
```python
# Pass run path to each agent
major_job_boards_agent.run(
    search_parameters=params,
    output_path=file_paths["major_job_boards"]
)
```

### Agents should save data with application URLs:
Each agent must capture and include:
- Direct application URL (`application_url`)
- Job posting URL (`posting_url`) 
- Source platform (`source`)
- Unique identifier (`position_id`)

## Review and Historical Analysis

### List Previous Runs:
```python
manager = SearchReportManager()
runs = manager.list_all_runs()

# Display run history
for run in runs:
    print(f"{run['date']} Run #{run['run_number']}: {run['metadata']['run_info']['search_type']}")
```

### Compare Runs:
```python
# Compare market trends across runs
run1 = load_run_data("2025/08/03/1")
run2 = load_run_data("2025/08/03/2") 
compare_market_trends(run1, run2)
```

## Error Handling

- Always create run folder before starting analysis
- Validate all required files are present before completing
- Save partial results if analysis fails
- Include error information in metadata

## Success Criteria

A successful job analyzer run must:
1. ✅ Create proper folder structure with run number
2. ✅ Generate all required JSON and Markdown files  
3. ✅ Include direct application URLs for all positions
4. ✅ Save complete metadata with statistics
5. ✅ Provide clear file paths for user access

This workflow ensures consistent, trackable, and reviewable job search analysis over time.