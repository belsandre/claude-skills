---
name: company-research
description: Conduct thorough, critical research on companies and key people using web search, extracting high-quality information from diverse sources, thinking critically about source objectivity and inconsistencies, and producing structured research outputs with resumability support. Use this skill when the user provides information about a company or person (URLs, LinkedIn profiles, pitch decks, meeting notes, etc.) and requests comprehensive research, due diligence, or evaluation against criteria.
---

# Company Research Skill

## Overview

This skill enables comprehensive, rigorous research on companies and key people by:
- Systematically searching the web for high-quality information sources
- Extracting and documenting content from diverse sources (articles, filings, reviews, documentation, etc.)
- Critically evaluating source objectivity and identifying biases
- Detecting and documenting inconsistencies across sources
- Organizing research into structured outputs with proper sourcing
- Supporting resumability for long research projects that may hit context limits
- Optionally evaluating findings against provided criteria

## When to Use This Skill

Use this skill when the user requests research on:
- A company (startup, growth-stage, or public company)
- Key people (founders, executives, potential hires, investors)
- Both company and associated people together

**Trigger scenarios**:
- User provides URLs, LinkedIn profiles, pitch decks, or meeting notes about a company/person
- User requests "research", "due diligence", "background check", or "evaluation"
- User asks to assess a company/person against specific criteria
- User needs comprehensive information gathering before a decision

**Do NOT use this skill for**:
- Quick fact-checking (use direct web search)
- Researching general topics not related to companies/people
- Academic literature reviews
- Product comparisons without company context

## Research Workflow

### Phase 1: Initialize Research Project

**Note on Multi-User Context**: When running in a multi-user job queue environment, the skill automatically detects the user context and creates outputs in `users/{username}/{project}/outputs/company-research/` where `{project}` is the project name. You can also override the output location by setting the `RESEARCH_OUTPUTS_DIR` environment variable.

1. **Create Project Structure**
   - Determine project name from company/person being researched
   - Create output directory: `users/{username}/{project}/outputs/company-research/`
   - Create subdirectories: `company/` and `people/`
   - Initialize state tracking:
     ```bash
     python3 scripts/research_state.py init [project-name]
     ```

2. **Create Research Plan**
   - Copy `assets/research_plan_template.md` to project directory
   - Customize based on user's request and available information
   - Identify key questions to answer
   - Note if criteria file is provided
   - Define search strategy and phases

3. **Parse Initial Information**
   - Review any URLs, documents, or notes provided by user
   - Extract key details (company name, people names, industry, etc.)
   - Identify gaps in information
   - Add initial insights to research plan

### Phase 2: Information Gathering

Execute research in phases as defined in research plan. For each phase:

1. **Conduct Web Searches**
   - Use strategic search queries from research plan
   - Prioritize high-objectivity sources first (filings, official records, analyst reports)
   - Then medium-objectivity sources (news, reviews, professional content)
   - Finally low-objectivity sources (company materials, promotional content)

2. **For Each High-Quality Source Found**:

   a. **Extract and Document**:
   - Navigate to the source URL
   - Read/extract the full content
   - Copy `assets/source_template.md` to appropriate directory:
     - `users/{username}/{project}/outputs/company-research/company/[source-name].md` for company info
     - `users/{username}/{project}/outputs/company-research/people/[person-name]-[source-name].md` for people info
   - Fill in the template with:
     - Full URL
     - Source type (Financial Filing, News Article, etc.)
     - Publication/last updated date
     - Objectivity level (High/Medium/Low) - consult `references/critical_evaluation_framework.md`
     - Reliability assessment
     - Key information bullets
     - Funding details (if applicable): amount, valuation, lead investor, participating investors
     - Customer information (if applicable): Fortune 500/Global 2000 status, unicorn status, recent IPO, high-growth tech company
     - Critical assessment (strengths, limitations, biases, verification status, inconsistencies)
     - Full raw content from the source

   b. **Track Progress**:
   ```bash
   python3 scripts/research_state.py add-source [project-name] [company|people] [source-name] [url]
   python3 scripts/research_state.py mark-complete [project-name] [company|people] [source-name]
   ```

3. **Apply Critical Thinking**
   - Reference `references/critical_evaluation_framework.md` throughout
   - Assess each source's objectivity level using the credibility spectrum
   - Ask critical thinking questions relevant to the information type
   - Document inconsistencies when sources contradict each other
   - Note what's missing or unclear
   - Distinguish between objective facts and promotional claims

4. **Monitor Context and State**
   - Periodically check context usage
   - If approaching context limits:
     ```bash
     python3 scripts/research_state.py status [project-name]
     python3 scripts/research_state.py next-tasks [project-name]
     ```
   - Update research plan with current progress
   - Document next steps clearly
   - Exit gracefully with ability to resume

### Phase 3: Analysis and Synthesis

1. **Review All Gathered Sources**
   - Read through all saved source documents
   - Identify patterns and themes
   - Map out inconsistencies across sources
   - Assess confidence levels for key findings
   - Note information gaps

2. **Evaluate Source Quality**
   - Count sources by objectivity level
   - Identify which claims are well-supported vs. weakly supported
   - Note areas where only promotional sources exist
   - Flag areas needing more objective verification

2a. **Assess Signal Quality (for funding/customer data)**
   - For funding: Note valuation trends, lead investor identity, consistency across sources
   - For customers: Identify Fortune 500/Global 2000, unicorns, recent IPOs, high-growth tech companies
   - Document these as objective quality indicators in findings

3. **Identify Inconsistencies**
   - Document significant conflicts between sources
   - Assess which source is more reliable for each inconsistency
   - Provide likely explanations for discrepancies
   - Flag unresolved conflicts

4. **Formulate Key Findings**
   - Synthesize information into clear findings
   - Support each finding with specific evidence
   - Assign confidence levels (High/Medium/Low)
   - Note gaps and limitations

### Phase 4: Produce Research Summary

1. **Create Research Summary**
   - Copy `assets/research_summary_template.md` to `users/{username}/{project}/outputs/company-research/research-summary.md`
   - Fill in all sections:
     - Executive summary (high-level overview)
     - Company overview (basics, business model, product)
     - Key findings (with evidence and confidence levels). Distinguish interested-party sources (GP/company materials, dataroom, their website/LinkedIn) from independent verification (third-party news, filings, external analysis). Mark each finding's verification status.
     - Key people (background, role, reputation, assessment)
     - Source quality analysis (categorized by objectivity)
     - Inconsistencies & red flags
     - Areas for further research
     - Research methodology and limitations
     - Appendix with all sources

2. **Quality Check**
   - Verify all claims are properly sourced
   - Ensure objectivity assessments are accurate
   - Check that inconsistencies are documented
   - Verify findings mark whether claims are from interested parties or independent sources
   - Confirm confidence levels are justified
   - Review completeness against research plan

### Phase 5: Criteria Evaluation (If Applicable)

If user provided a criteria file:

1. **Analyze Criteria File**
   - Read the criteria document thoroughly
   - Break down each criterion into specific information requirements
   - Identify what evidence is needed for each criterion
   - Note required objectivity levels

2. **Map Research to Criteria**
   - For each criterion, identify relevant sources
   - Extract specific evidence from saved sources
   - Assess whether evidence meets, partially meets, or doesn't meet criterion
   - Document confidence level for each assessment
   - Note gaps in information

3. **Create Evaluation Document**
   - Copy `assets/evaluation_template.md` to `users/{username}/{project}/outputs/company-research/evaluation.md`
   - Fill in all sections:
     - Evaluation summary and recommendation
     - Detailed assessment for each criterion (with evidence, reasoning, gaps, confidence)
     - Scoring summary table
     - Strengths and weaknesses relative to criteria
     - Risk factors
     - Key considerations
     - Recommendations
     - Appendix with interpretations and alternatives

4. **Critical Evaluation**
   - Think critically about how well evidence actually addresses each criterion
   - Distinguish between strong evidence and weak evidence
   - Note where assumptions are being made
   - Identify where more information would change the assessment
   - Document areas of uncertainty

## Critical Thinking Guidelines

Throughout the research process, apply these principles from `references/critical_evaluation_framework.md`:

### Source Objectivity Spectrum

**High Objectivity** (trust but verify):
- Financial/regulatory filings (SEC, annual reports)
- Technical documentation (APIs, specs, patents)
- Third-party analysis (analyst reports, academic research)
- Government/public records
- Customer usage data (GitHub, app stores, traffic)

**Medium Objectivity** (valuable but requires interpretation):
- News articles (major outlets)
- Product reviews (professional and user)
- Conference presentations
- Professional social media

**Low Objectivity** (useful for positioning, not facts):
- Company-controlled content (website, blog, press releases)
- Leadership communications (interviews, speeches)
- Sales/marketing materials
- Sponsored content

### Critical Questions to Ask

**For Company Information**:
- Are financial claims backed by verifiable filings?
- Do customer numbers/revenue align across independent sources?
- Can product claims be verified through documentation or demos?
- Do employee reviews align with stated culture?
- What's missing from company materials?

**For People Information**:
- Are job titles and dates consistent across sources?
- Can stated accomplishments be verified independently?
- What do former colleagues and employees say?
- Do public statements align with actions?
- Are there unexplained gaps or inconsistencies?

### Documenting Inconsistencies

For each significant inconsistency:
1. State the inconsistency clearly: "Source A claims X, while Source B states Y"
2. Assess source reliability: "Source A is [type] (objectivity level), Source B is [type] (objectivity level)"
3. Provide likely explanation: "The discrepancy likely stems from..."
4. Indicate confidence: "Based on source reliability, Y is more likely accurate"

### Red Flags

Watch for and document:
- Numerical inconsistencies (varying funding, employee counts, timelines)
- Narrative inconsistencies (origin stories, product evolution, leadership changes)
- Omission patterns (avoiding known problems, skipping time periods)
- Tone shifts (sudden changes in messaging or direction)

## Resumability Support

This skill is designed to handle long research projects that may exceed context limits:

### State Management

Use `scripts/research_state.py` to track progress:

```bash
# Initialize project
python3 scripts/research_state.py init [project-name]

# Add sources to research plan
python3 scripts/research_state.py add-source [project-name] company [source-name] [url]
python3 scripts/research_state.py add-source [project-name] people [person-source] [url]

# Mark sources as complete
python3 scripts/research_state.py mark-complete [project-name] company [source-name]

# Check status
python3 scripts/research_state.py status [project-name]

# Get next tasks
python3 scripts/research_state.py next-tasks [project-name]
```

### When Context Limits Approached

1. Save current state using research_state.py
2. Update research plan with progress
3. Document exactly what's completed and what's next
4. Commit any in-progress source documents
5. Note in research plan: "Research paused at [phase] due to context limits. Resume by checking state file and research plan."

### Resuming Research

When resuming:
1. Check state file: `python3 scripts/research_state.py status [project-name]`
2. Review research plan for current status
3. Get next tasks: `python3 scripts/research_state.py next-tasks [project-name]`
4. Continue from where you left off
5. Review any partially completed source documents

## Resource Usage

### Scripts

**`scripts/research_state.py`**: State management for resumability
- Track research progress across sessions
- Manage source lists (company and people)
- Mark sources as completed
- Generate status reports and next task lists
- Find state files across project directories

Execute without loading into context when managing state. Read if debugging or modifying.

### References

**`references/critical_evaluation_framework.md`**: Critical thinking guide
- Source credibility spectrum (high/medium/low objectivity)
- Critical thinking questions for companies and people
- Inconsistency identification and documentation
- Source documentation standards
- Evaluation criteria assessment frameworks
- Research quality checklist

Load this reference when:
- Starting a new research project (to internalize the framework)
- Assessing source objectivity
- Documenting inconsistencies
- Evaluating against criteria
- Unsure how to critically assess a source

### Assets

**Templates for structured outputs**:
- `assets/source_template.md`: Template for documenting each source
- `assets/research_summary_template.md`: Template for final research summary
- `assets/evaluation_template.md`: Template for criteria evaluation
- `assets/research_plan_template.md`: Template for research planning

Copy these templates to the project directory and customize as needed. Do not load into context—they are meant to be copied and filled in.

## Output Structure

For each research project, create this structure in multi-user mode:

```
users/{username}/{project}/outputs/company-research/
├── .research_state.json           # State tracking (auto-created by script)
├── research-plan.md                # Research plan and progress tracking
├── research-summary.md             # Final summary with key findings
├── evaluation.md                   # Criteria evaluation (if criteria provided)
├── company/                        # Company-related sources
│   ├── [source-1].md              # Each source in separate file
│   ├── [source-2].md
│   └── ...
└── people/                         # People-related sources
    ├── [person-1-source-1].md     # Sources about person 1
    ├── [person-2-source-1].md     # Sources about person 2
    └── ...
```

Where:
- `{username}` is the current user (e.g., "yani", "ashish", "tam")
- `{project}` is the project name (e.g., "ggml", "hyperion", "defud")
- All research outputs are stored in the `outputs/company-research/` subdirectory

## Best Practices

1. **Start with High-Objectivity Sources**: Begin searches with filings, official records, and analyst reports before moving to promotional content

2. **Document Everything**: Save full content for every source, not just summaries, to enable future verification

3. **Be Skeptical of Promotional Content**: Company websites, press releases, and executive interviews are useful for understanding positioning, but verify claims elsewhere

4. **Cross-Reference Key Claims**: Any important claim should be verified across multiple sources

5. **Note What's Missing**: Explicitly document information you couldn't find—this is often as important as what you did find

6. **Assess Confidence Levels**: Always indicate whether findings are high/medium/low confidence based on source quality

7. **Track Inconsistencies**: When sources conflict, document both versions and assess which is more reliable

8. **Use State Management**: For any research lasting more than 30 minutes, use research_state.py to track progress

9. **Think About Context**: Monitor context usage and exit gracefully before hitting limits, with clear resumption instructions

10. **Quality Over Quantity**: Focus on high-quality, objective sources rather than accumulating many low-quality sources

## Example Usage Scenarios

### Scenario 1: Startup Due Diligence

**User Request**: "Research this AI startup. Here's their deck and LinkedIn. I'm considering investing."

**Approach**:
1. Initialize project for the startup name
2. Create research plan focused on: funding history, product claims, market validation, team background
3. Search for: Crunchbase data, product reviews, technical blog posts, founder backgrounds, customer case studies
4. Apply high skepticism to deck claims, verify independently
5. Document inconsistencies between deck and external sources
6. Produce research summary with investment-relevant findings

### Scenario 2: Executive Background Check

**User Request**: "I'm hiring a VP of Engineering. Here's their LinkedIn. Do thorough research on their background and track record."

**Approach**:
1. Initialize project for the person
2. Create research plan focused on: career history, technical expertise, leadership track record, reputation
3. Search for: LinkedIn, GitHub, blog posts, conference talks, employee reviews at previous companies, news mentions
4. Cross-reference job titles and dates across sources
5. Look for patterns in team turnover, product success, technical contributions
6. Produce research summary with hiring-relevant assessment

### Scenario 3: Competitive Analysis with Criteria

**User Request**: "Research these three competitors. Here's our evaluation criteria for potential acquisition targets."

**Approach**:
1. Initialize separate projects for each competitor
2. Create research plans targeted at criteria (e.g., technology stack, customer base, team quality, financial health)
3. Prioritize sources that address criteria
4. For each competitor: gather sources, apply critical evaluation, produce research summary AND evaluation.md
5. Enable direct comparison across all three evaluations

## Tips for Effective Research

- **Start Broad, Then Focus**: Begin with general searches, then drill into specific areas based on initial findings
- **Follow the Trail**: Sources often reference other valuable sources—follow those leads
- **Check Multiple Outlets**: For news, check 3+ different outlets to see if stories align
- **Look for Primary Sources**: When possible, go to the original source rather than secondhand reporting
- **Time-Bound Searches**: For recent news, limit searches to past 6-12 months
- **Use Advanced Search**: Leverage site-specific searches (site:linkedin.com, site:sec.gov, etc.)
- **Archive Awareness**: Some sources may be behind paywalls or archived—note access limitations
- **Privacy Respect**: Focus on publicly available information; don't attempt to access private data
