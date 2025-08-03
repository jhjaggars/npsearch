#!/usr/bin/env python3
"""
Job Search Report Manager
Manages folder structure and run numbering for job search reports.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Tuple, Optional

class SearchReportManager:
    """Manages job search report folder structure and run numbering."""
    
    def __init__(self, base_path: str = "/home/jhjaggars/code/jobsearch"):
        self.base_path = Path(base_path)
        self.reports_dir = self.base_path / "search_reports"
        
    def get_current_date_path(self) -> Path:
        """Get the folder path for today's date."""
        now = datetime.now()
        return self.reports_dir / str(now.year) / f"{now.month:02d}" / f"{now.day:02d}"
    
    def get_next_run_number(self, date_path: Optional[Path] = None) -> int:
        """Get the next run number for the given date (or today)."""
        if date_path is None:
            date_path = self.get_current_date_path()
        
        if not date_path.exists():
            return 1
        
        # Find existing run folders
        run_folders = [d for d in date_path.iterdir() if d.is_dir() and d.name.isdigit()]
        if not run_folders:
            return 1
        
        # Get the highest run number and increment
        max_run = max(int(folder.name) for folder in run_folders)
        return max_run + 1
    
    def create_run_folder(self, run_number: Optional[int] = None) -> Path:
        """Create a new run folder and return its path."""
        date_path = self.get_current_date_path()
        
        if run_number is None:
            run_number = self.get_next_run_number(date_path)
        
        run_path = date_path / str(run_number)
        run_path.mkdir(parents=True, exist_ok=True)
        
        return run_path
    
    def get_run_metadata_path(self, run_path: Path) -> Path:
        """Get the path for run metadata file."""
        return run_path / "run_metadata.json"
    
    def create_run_metadata(self, run_path: Path, search_type: str = "comprehensive", 
                          specialty_focus: str = "FNP") -> dict:
        """Create and save run metadata."""
        metadata = {
            "run_info": {
                "timestamp": datetime.now().isoformat(),
                "date": datetime.now().strftime("%Y-%m-%d"),
                "run_number": int(run_path.name),
                "search_type": search_type,
                "specialty_focus": specialty_focus
            },
            "folder_structure": {
                "base_path": str(run_path),
                "expected_files": [
                    "run_metadata.json",
                    "consolidated_np_job_analysis.json",
                    "np_market_analysis_report.json", 
                    "np_job_application_strategy.json",
                    "np_job_search_executive_summary.md",
                    "np_job_search_with_application_links.md",
                    "major_job_boards_data.json",
                    "healthcare_systems_data.json",
                    "specialty_nursing_boards_data.json",
                    "government_healthcare_data.json"
                ]
            },
            "data_sources": {
                "major_job_boards": "LinkedIn, Indeed, Glassdoor, ZipRecruiter, SimplyHired",
                "healthcare_systems": "Duke Health, Novant Health, Atrium Health, UNC Health",
                "specialty_boards": "AANP, Nurse.com, nursing-specific platforms",
                "government": "USAJOBS, VA, state/local government positions"
            }
        }
        
        metadata_path = self.get_run_metadata_path(run_path)
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return metadata
    
    def get_standard_file_paths(self, run_path: Path) -> dict:
        """Get standardized file paths for a run."""
        return {
            "metadata": run_path / "run_metadata.json",
            "consolidated_analysis": run_path / "consolidated_np_job_analysis.json",
            "market_analysis": run_path / "np_market_analysis_report.json",
            "application_strategy": run_path / "np_job_application_strategy.json",
            "executive_summary": run_path / "np_job_search_executive_summary.md",
            "application_links": run_path / "np_job_search_with_application_links.md",
            "major_job_boards": run_path / "major_job_boards_data.json",
            "healthcare_systems": run_path / "healthcare_systems_data.json", 
            "specialty_boards": run_path / "specialty_nursing_boards_data.json",
            "government_data": run_path / "government_healthcare_data.json"
        }
    
    def list_all_runs(self) -> list:
        """List all search runs with metadata."""
        runs = []
        
        if not self.reports_dir.exists():
            return runs
        
        # Walk through year/month/day/run structure
        for year_dir in sorted(self.reports_dir.iterdir()):
            if not year_dir.is_dir() or not year_dir.name.isdigit():
                continue
                
            for month_dir in sorted(year_dir.iterdir()):
                if not month_dir.is_dir() or not month_dir.name.isdigit():
                    continue
                    
                for day_dir in sorted(month_dir.iterdir()):
                    if not day_dir.is_dir() or not day_dir.name.isdigit():
                        continue
                        
                    for run_dir in sorted(day_dir.iterdir(), key=lambda x: int(x.name)):
                        if not run_dir.is_dir() or not run_dir.name.isdigit():
                            continue
                        
                        metadata_path = self.get_run_metadata_path(run_dir)
                        if metadata_path.exists():
                            with open(metadata_path) as f:
                                metadata = json.load(f)
                            runs.append({
                                "path": str(run_dir),
                                "date": f"{year_dir.name}-{month_dir.name}-{day_dir.name}",
                                "run_number": int(run_dir.name),
                                "metadata": metadata
                            })
        
        return runs
    
    def setup_new_search_run(self, search_type: str = "comprehensive", 
                           specialty_focus: str = "FNP") -> Tuple[Path, dict]:
        """Set up a new search run with proper folder structure."""
        run_path = self.create_run_folder()
        metadata = self.create_run_metadata(run_path, search_type, specialty_focus)
        
        print(f"Created new search run: {run_path}")
        print(f"Run number: {metadata['run_info']['run_number']}")
        print(f"Date: {metadata['run_info']['date']}")
        
        return run_path, metadata

if __name__ == "__main__":
    # Example usage
    manager = SearchReportManager()
    
    # List existing runs
    runs = manager.list_all_runs()
    print(f"Found {len(runs)} existing search runs:")
    for run in runs[-5:]:  # Show last 5 runs
        print(f"  {run['date']} Run #{run['run_number']}: {run['metadata']['run_info']['search_type']}")
    
    # Show what the next run would be
    next_run = manager.get_next_run_number()
    print(f"\nNext run number for today: {next_run}")