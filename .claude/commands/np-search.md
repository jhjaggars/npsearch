---
description: "Execute comprehensive nurse practitioner job search workflow for Raleigh, NC area"
allowed-tools: "*"
---

# Comprehensive NP Job Search Workflow for Raleigh, NC

Execute a coordinated search across all major job platforms for nurse practitioner positions in the Raleigh/Triangle area of North Carolina.

## Workflow Overview

This command orchestrates a complete job market analysis by:

1. **Launching all specialized job search agents in parallel:**
   - **major-job-boards**: Search Indeed, LinkedIn, Glassdoor, ZipRecruiter, SimplyHired
   - **healthcare-systems**: Monitor Duke Health, Novant Health, Atrium Health, UNC Health career pages
   - **specialty-nursing-boards**: Browse nursing-specific job boards and professional association sites
   - **government-healthcare**: Check VA, federal, state, and local government healthcare positions

2. **Collecting and standardizing data** from all sources into structured JSON format with comprehensive job details

3. **Analyzing and ranking opportunities** using the job-analyzer agent:
   - Consolidate and deduplicate job listings across all platforms
   - Score positions based on compensation, benefits, growth potential, location, and work-life balance
   - Generate market intelligence and identify trending opportunities
   - Rank opportunities by overall attractiveness and candidate fit

4. **Generating comprehensive reports:**
   - Top 20 recommended positions with detailed analysis and application strategies
   - Market summary dashboard with salary trends and demand analysis
   - Specialty-specific insights and emerging opportunities
   - Geographic distribution of opportunities across the Triangle area
   - Actionable next steps and application priorities for job seekers

## Usage Examples

- **Full comprehensive search:**  
  `/np-search`

- **Specialty-focused searches:**  
  `/np-search psychiatric mental health` - Target PMHNP positions  
  `/np-search emergency medicine` - Focus on emergency NP roles  
  `/np-search family medicine` - Primary care opportunities  
  `/np-search new graduate` - Filter for new grad friendly positions

## Search Parameters

**Optional Arguments:** $ARGUMENTS  
Specify specialty focus, experience level, or other search criteria to customize the workflow.

**Geographic Focus:** Raleigh, Durham, Chapel Hill, Cary, Wake Forest, and surrounding Triangle area

**Data Collection:** Creates timestamped data files in `/data/` directory for analysis and historical tracking

## Expected Timeline

- **Data Collection Phase:** 60-90 minutes (parallel execution across all platforms)
- **Analysis Phase:** 15-30 minutes (consolidation, deduplication, scoring)
- **Report Generation:** 5-10 minutes (comprehensive analysis and recommendations)
- **Total Workflow Time:** ~2 hours for complete market analysis

## Output Deliverables

Upon completion, you will receive:

1. **Executive Summary** - Key findings and immediate opportunities
2. **Top Opportunities Report** - Detailed analysis of highest-ranked positions
3. **Market Intelligence Dashboard** - Salary trends, demand analysis, competitive landscape
4. **Application Strategy Guide** - Prioritized action plan with timeline recommendations
5. **Raw Data Files** - Complete job listings for further analysis or follow-up searches

## Execution Strategy

The workflow uses browser automation with Playwright/Puppeteer to systematically navigate job sites, extract comprehensive job information, and compile actionable intelligence for nurse practitioners seeking opportunities in North Carolina's Research Triangle region.

Start the comprehensive nurse practitioner job search workflow now!