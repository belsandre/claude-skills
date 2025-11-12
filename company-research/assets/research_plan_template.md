# Research Plan: [Company/Project Name]

**Created**: [Date]
**Project Directory**: [PROJECT_DIR]
**State File**: [Path to .research_state.json]

---

## Research Objective

[Clear statement of what this research aims to accomplish]

**Key Questions to Answer**:
1. [Question 1]
2. [Question 2]
3. [Additional questions]

**Criteria File**: [Path if provided, or "None"]

---

## Information Gathering Strategy

### Phase 1: Core Company Information
**Objective**: Establish basic facts about the company

**Sources to Find**:
- [ ] Company website and about page
- [ ] LinkedIn company page
- [ ] Recent news articles (past 6 months)
- [ ] Funding databases (Crunchbase, PitchBook)
- [ ] Financial filings (if public)
- [ ] Product documentation

**Priority**: High
**Estimated Effort**: [time estimate]

### Phase 2: Financial & Business Model
**Objective**: Understand how the company makes money and its financial health

**Sources to Find**:
- [ ] SEC filings (10-K, 10-Q, S-1 if applicable)
- [ ] Earnings reports and transcripts
- [ ] Analyst reports
- [ ] Revenue/funding announcements
- [ ] Customer case studies
- [ ] Pricing information

**Priority**: High
**Estimated Effort**: [time estimate]

### Phase 3: Product & Technology
**Objective**: Evaluate product capabilities and technical approach

**Sources to Find**:
- [ ] Product documentation and specs
- [ ] API documentation
- [ ] Technical blogs/whitepapers
- [ ] GitHub repositories (if applicable)
- [ ] Product reviews and comparisons
- [ ] Customer reviews (G2, Capterra, etc.)
- [ ] Demo videos or trials

**Priority**: Medium
**Estimated Effort**: [time estimate]

### Phase 4: Market Position & Competition
**Objective**: Understand competitive landscape and market position

**Sources to Find**:
- [ ] Industry analyst reports (Gartner, Forrester)
- [ ] Competitive analysis articles
- [ ] Market size/growth projections
- [ ] Customer win/loss analysis
- [ ] Competitor websites and positioning
- [ ] Industry news and trends

**Priority**: Medium
**Estimated Effort**: [time estimate]

### Phase 5: Leadership & Key People
**Objective**: Research founders, executives, and key personnel

**People to Research**:
- [ ] CEO/Founder: [Name]
- [ ] CTO/Co-founder: [Name]
- [ ] [Other key roles]

**Sources to Find (per person)**:
- [ ] LinkedIn profile
- [ ] Previous companies/roles
- [ ] Interviews and podcasts
- [ ] Social media presence
- [ ] Educational background
- [ ] Published articles/talks
- [ ] Glassdoor reviews mentioning them

**Priority**: Medium
**Estimated Effort**: [time estimate]

### Phase 6: Culture & Employee Sentiment
**Objective**: Understand company culture and employee experience

**Sources to Find**:
- [ ] Glassdoor reviews
- [ ] Blind posts
- [ ] LinkedIn employee posts
- [ ] Employee tenure analysis
- [ ] Job postings analysis
- [ ] Employer brand content

**Priority**: Low
**Estimated Effort**: [time estimate]

---

## Search Strategy

### Primary Search Queries
1. "[Company name]" + "funding"
2. "[Company name]" + "revenue"
3. "[Company name]" + "customers"
4. "[Company name]" + "Fortune 500" OR "[Company name]" + "customer logos"
5. "[Company name]" + "review"
6. "[Company name]" + "vs" + "[competitor]"
7. "[Product name]" + "documentation"
8. "[Founder name]" + "interview"
9. [Additional strategic searches]

### Sources to Prioritize
1. **High-objectivity sources** (search first):
   - SEC.gov (if public company)
   - Crunchbase/PitchBook
   - Bloomberg/Reuters
   - Industry analyst firms

2. **Medium-objectivity sources**:
   - TechCrunch, The Information, WSJ
   - Product review sites
   - Professional LinkedIn posts
   - Conference presentations

3. **Low-objectivity sources** (for positioning only):
   - Company website and blog
   - Press releases
   - Marketing materials
   - Executive interviews

---

## Output Structure

```
[BASE_DIR]/
├── .research_state.json          # State file for resumability
├── research-plan.md               # This file
├── research-summary.md            # Final summary (created at end)
├── evaluation.md                  # Criteria evaluation (if applicable)
├── company/
│   ├── [source-1].md
│   ├── [source-2].md
│   └── [additional-sources].md
└── people/
    ├── [person-1-source-1].md
    ├── [person-1-source-2].md
    └── [additional-people-sources].md
```

Where `[BASE_DIR]` is `outputs/[date]-[project]` in standalone mode or `users/{username}/outputs/[date]-[project]` in multi-user mode.

---

## Resumability Plan

### State Tracking
- Use `scripts/research_state.py` to track progress
- Mark sources as completed after processing
- Save state file after each major source

### If Context Limits Reached
1. Save current state with `research_state.py status [project-name]`
2. Document progress in this file
3. Note next tasks with `research_state.py next-tasks [project-name]`
4. Exit and resume by checking state file

### Checkpoints
- [ ] After Phase 1 (Core Information)
- [ ] After Phase 2 (Financial)
- [ ] After Phase 3 (Product)
- [ ] After Phase 4 (Market)
- [ ] After Phase 5 (People)
- [ ] Before writing summary

---

## Progress Tracking

### Completed Tasks
- [Date] [Task description]

### Current Status
**Phase**: [Current phase name]
**Next**: [Next immediate task]
**Blocked By**: [Any blockers]

### Outstanding Items
1. [Item 1]
2. [Item 2]

---

## Notes & Observations

### Initial Observations
[Early findings or patterns noticed during initial research]

### Research Challenges
[Difficulties encountered, information that's hard to find]

### Unexpected Discoveries
[Interesting findings that weren't part of original plan]

---

## Timeline

| Phase | Start Date | End Date | Status |
|-------|------------|----------|--------|
| Phase 1: Core Company Info | [Date] | [Date] | [Not Started/In Progress/Complete] |
| Phase 2: Financial | [Date] | [Date] | [Status] |
| Phase 3: Product | [Date] | [Date] | [Status] |
| Phase 4: Market | [Date] | [Date] | [Status] |
| Phase 5: People | [Date] | [Date] | [Status] |
| Phase 6: Culture | [Date] | [Date] | [Status] |
| Summary Writing | [Date] | [Date] | [Status] |
| Evaluation (if criteria) | [Date] | [Date] | [Status] |
