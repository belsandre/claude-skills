---
name: market-assessment
description: Comprehensive market assessment skill for analyzing companies, identifying competitors, assessing competitive threats, building competitive matrices, verifying marketing claims, and evaluating market dynamics. Use this skill when conducting due diligence on companies, performing competitive analysis, evaluating investment opportunities, or researching market positioning. Particularly valuable for technical products with documentation and GitHub repositories. Designed for resumability - can pause and continue across conversations.
---

# Market Assessment

## Overview

Perform comprehensive market assessment and competitive analysis for target companies. This skill provides a systematic framework for:
- Identifying and researching competitors
- Assessing competitive threats with quantitative scoring
- Building detailed competitive matrices
- Verifying marketing claims
- Analyzing market size and penetration
- Synthesizing findings into actionable insights

The skill is designed for robustness and resumability, saving intermediate outputs at each phase to enable pausing and continuing across multiple conversations.

## When to Use This Skill

Invoke this skill when:
- **Due diligence:** Evaluating a company for investment, partnership, or acquisition
- **Competitive analysis:** Understanding competitive landscape for strategic planning
- **Market research:** Assessing market opportunity and positioning
- **Product strategy:** Identifying differentiation and competitive gaps
- **Claims verification:** Validating company marketing claims and assertions

**Trigger phrases:**
- "Perform market assessment on [company]"
- "Analyze competitors for [company]"
- "Do competitive analysis for [company]"
- "Assess the market for [company/product]"
- "Verify claims made by [company]"

## Input Requirements

The skill accepts flexible input formats:
- **Company name and URLs** (website, GitHub, product pages)
- **Existing research documents** (in `users/{username}/{project}/company-research/`)
- **Pitch decks and presentations** (PDFs, PPTX)
- **Meeting notes and research summaries** (Markdown, text)
- **Direct instructions** (custom analysis focus areas)

The skill will work with whatever information is provided and note gaps in the analysis.

## Output Structure

All outputs are saved to: `users/{username}/{project}/market-assessment/`

```
market-assessment/
├── progress.json                    # Tracks completed phases
├── 01-target-company-summary.md     # Target company analysis
├── 02-competitor-list.md            # Identified competitors
├── 03-competitor-details/           # One file per competitor
│   ├── competitor-1.md
│   ├── competitor-2.md
│   └── ...
├── 04-financial-health.md           # Competitor financial analysis
├── 05-threat-assessment.md          # Threat level evaluations
├── 06-competitive-matrix.md         # Comparative analysis
├── 07-claims-verification.md        # Marketing claims assessment
├── 08-market-analysis.md            # Market size and penetration
└── summary.md                       # Executive summary
```

---

## Workflow

### Phase 0: Initialization & Setup

**Objective:** Set up the project structure and check for existing progress.

**Actions:**
1. Determine the target project path: `users/{username}/{project}/market-assessment/`
2. Create the `market-assessment/` directory if it doesn't exist
3. Create `03-competitor-details/` subdirectory
4. Check for existing `progress.json` file to determine what's already complete
5. If `progress.json` exists, report completed phases and ask user if they want to:
   - Continue from where left off (skip completed phases)
   - Re-run specific phases (delete specific output files)
   - Start fresh (delete all outputs)

**Progress Tracking:**
Create or update `progress.json`:
```json
{
  "last_updated": "2025-01-10T12:00:00Z",
  "completed_phases": [],
  "current_phase": 1,
  "target_company": "Company Name",
  "project_path": "users/username/project/market-assessment",
  "phase_status": {
    "phase_1": "not_started",
    "phase_2": "not_started",
    ...
  }
}
```

**Error Handling:**
- If directory creation fails, report error and suggest manual creation
- If user's folder doesn't exist, report error with clear path

---

### Phase 1: Target Company Analysis

**Objective:** Understand the target company comprehensively before analyzing competitors.

**Input Sources (check in order):**
1. Check for existing company research in `users/{username}/{project}/company-research/`
2. Check for pitch decks or documents in `users/{username}/{project}/inputs/`
3. Use company name/URLs provided by user
4. If minimal information, use web search to gather basics

**Actions:**
1. **Load or gather company information:**
   - If company-research folder exists: Read and synthesize existing research
   - If not: Web search for company website, GitHub, product pages, funding news

2. **Extract key information:**
   - Company name, website, founding year, location
   - Founders and key team members
   - Product/service description and value proposition
   - Technology stack and technical approach
   - Funding stage, investors, capital raised
   - Target market and customers (ICP)
   - Key marketing claims and positioning
   - GitHub presence (if applicable)
   - Available documentation and resources

3. **Create output:** `01-target-company-summary.md`
   - Company overview
   - Product/technology details
   - Funding and team
   - Market positioning
   - Key claims (to verify later)
   - Information gaps and uncertainties

4. **Update progress:**
   ```json
   {
     "completed_phases": ["phase_1"],
     "current_phase": 2,
     "phase_status": {"phase_1": "completed"}
   }
   ```

**Resumability:**
- If `01-target-company-summary.md` exists and is recent, ask user if they want to skip or refresh

**Time Management:**
- Limit web searches to 5-10 focused queries
- If information is sparse, proceed with what's available and note gaps

---

### Phase 2: Competitor Identification

**Objective:** Identify 10-20 relevant competitors that pose potential competitive threats.

**Selection Criteria:**
- **Product similarity:** Offer similar products or solve similar problems
- **Target market overlap:** Target similar buyers with similar budgets
- **Well-funded:** Backed by tier-1 VC funds
- **Growth stage:** Fast-growing growth-stage startups in similar space
- **Technical overlap:** For technical products, use similar technologies or approaches

**Search Strategies:**
Conduct focused web searches (limit to 10-15 searches total):

1. **Direct competitor searches:**
   - `[product category] companies`
   - `[product name] alternatives`
   - `[product name] competitors`
   - `tools like [product name]`

2. **Technology-based searches:**
   - `[core technology] startups`
   - `[programming language/framework] companies`
   - `[technical approach] products`

3. **Investor-based searches:**
   - `[investor name] portfolio companies`
   - `companies funded by [tier 1 VC]`

4. **Use case searches:**
   - `[use case] solutions`
   - `[problem being solved] companies`

5. **GitHub ecosystem searches:**
   - `site:github.com [technology/category]` (if relevant)
   - Related GitHub projects and organizations

**Actions:**
1. Execute search strategies systematically
2. Compile list of potential competitors (aim for 15-25 initial candidates)
3. Filter to most relevant 10-20 competitors using criteria:
   - High relevance: Direct product/market overlap
   - Medium relevance: Adjacent space with potential overlap
   - Remove: Too different, too small, defunct companies
4. For each competitor, capture:
   - Company name
   - Website URL
   - Brief description (1 sentence)
   - Why they're competitive (product/market similarity)
   - Preliminary threat level guess (refine in Phase 5)

5. **Create output:** `02-competitor-list.md`
   - Methodology explanation
   - Full list of identified competitors with basic info
   - Filtering rationale
   - Confidence level in competitor identification

6. **Update progress:**
   ```json
   {
     "completed_phases": ["phase_1", "phase_2"],
     "current_phase": 3,
     "competitor_count": 15
   }
   ```

**Fallback Strategies:**
- If few competitors found: Broaden search (adjacent spaces, alternative solutions)
- If too many found: Prioritize by funding level, market presence, recent news
- If stuck: Continue with partial list (minimum 5 competitors)

**Resumability:**
- If `02-competitor-list.md` exists, load it and proceed to Phase 3

---

### Phase 3: Competitor Deep Research

**Objective:** Research each competitor in depth to understand their product, technology, funding, and positioning.

**Template:** Use `references/competitor-research-template.md` as the structure for each competitor analysis.

**Actions (for each competitor):**

1. **Company overview research:**
   - Web search: `[competitor name] company`
   - Check Crunchbase/news for founding info, location, stage

2. **Product & technology research:**
   - Visit company website and product pages
   - **For technical products:** Search for GitHub repository
     - If found: Analyze stars, forks, contributors, activity, languages, license
     - Read README and documentation
   - Search for official documentation
   - Check for API docs, tutorials, technical blog posts
   - Assess actual capabilities vs marketing claims

3. **Funding & financial research:**
   - Web search: `[competitor name] funding`
   - Check Crunchbase mentions, press releases
   - Identify investors and funding stage
   - Look for financial health signals (hiring/firing, news, partnerships)

4. **Market positioning research:**
   - Identify target customers (ICP) from website
   - Check pricing if available
   - Assess go-to-market strategy (self-serve, sales-led, etc.)
   - Note differentiation claims

5. **Create output:** `03-competitor-details/{competitor-name}.md`
   - Follow competitor-research-template.md structure
   - Complete all sections with available information
   - Note information gaps
   - Include preliminary threat assessment (refine in Phase 5)

6. **Update progress after each competitor:**
   - Save individual file immediately
   - Update progress.json with count: `"competitors_researched": 5`

**Batching Strategy:**
- Research 3-5 competitors at a time
- Save progress after each batch
- If context is getting large, summarize and continue

**Time Management:**
- Spend ~10-15 minutes of research per competitor
- Limit to 5-8 web searches per competitor
- If information is sparse, note it and move on
- For technical products: Prioritize GitHub/docs analysis

**Resumability:**
- Check which competitor files already exist in `03-competitor-details/`
- Skip completed competitors, only research remaining ones
- User can delete specific competitor files to re-research

**Fallback Strategies:**
- If GitHub not found: Continue with website/docs analysis
- If no docs found: Rely on website and third-party info
- If very limited info: Create short analysis with gaps noted
- If too time-consuming: Reduce scope to top 8-10 competitors

---

### Phase 4: Financial Health Analysis

**Objective:** Synthesize financial health signals across all competitors to understand competitive resource dynamics.

**Actions:**
1. Review all competitor files in `03-competitor-details/`
2. Extract funding and financial data for each
3. Compile comparative financial analysis:
   - Funding comparison table (amount, stage, investors)
   - Investor tier analysis (tier 1 vs tier 2/3 VCs)
   - Runway estimates (conservative projections)
   - Financial health scoring (strong/moderate/concerning)
   - Growth signals (hiring trends, partnerships, news)
   - Risk factors (burn rate concerns, market challenges)

4. **Create output:** `04-financial-health.md`
   - Comparative funding table
   - Financial health assessment for each competitor
   - Resource advantages/disadvantages vs target company
   - Strategic implications

5. **Update progress:**
   ```json
   {
     "completed_phases": ["phase_1", "phase_2", "phase_3", "phase_4"],
     "current_phase": 5
   }
   ```

**Resumability:**
- If `04-financial-health.md` exists, skip this phase or refresh if requested

---

### Phase 5: Threat Assessment

**Objective:** Assign HIGH/MEDIUM/LOW threat levels to each competitor using systematic rubric.

**Template:** Use `references/threat-assessment-rubric.md` for scoring framework.

**Actions (for each competitor):**

1. **Load competitor data** from `03-competitor-details/{competitor-name}.md`

2. **Score each dimension (0-10 scale):**
   - Product Similarity (weight: 20%)
   - Market Overlap (weight: 20%)
   - Funding & Resources (weight: 15%)
   - Technical Capabilities (weight: 15%)
   - Market Traction (weight: 15%)
   - Go-to-Market Strength (weight: 10%)
   - Strategic Positioning (weight: 5%)

3. **Calculate weighted threat score:**
   - Apply weights to get total score (0-100)
   - Map to threat level:
     - 0-30: LOW
     - 31-60: MEDIUM
     - 61-100: HIGH

4. **Apply qualitative adjustments:**
   - Consider threat elevating factors
   - Consider threat reducing factors
   - Adjust final threat level if warranted

5. **Document justification:**
   - Explain why this threat level is assigned
   - List key threat factors
   - List mitigating factors
   - Recommend monitoring priorities

6. **Create output:** `05-threat-assessment.md`
   - Summary table: All competitors with threat levels
   - Detailed assessment for each competitor (using rubric template)
   - Threat level distribution (e.g., "3 HIGH, 7 MEDIUM, 5 LOW")
   - Strategic implications and recommendations
   - Monitoring priorities

7. **Update progress:**
   ```json
   {
     "completed_phases": ["phase_1", "phase_2", "phase_3", "phase_4", "phase_5"],
     "current_phase": 6,
     "threat_summary": {"high": 3, "medium": 7, "low": 5}
   }
   ```

**Resumability:**
- If `05-threat-assessment.md` exists, skip or refresh if requested

---

### Phase 6: Competitive Matrix

**Objective:** Build comprehensive comparison matrix showing points of differentiation vs parity.

**Template:** Use `references/competitive-matrix-template.md` as structure.

**Actions:**

1. **Select comparison dimensions:**
   - Review all competitor data
   - Choose 10-15 most relevant dimensions from template categories:
     - Product & Technology (architecture, features, performance, open source, etc.)
     - Market & Business Model (target customer, pricing, sales motion)
     - Company & Traction (funding, team size, growth, financial health)
     - Strategic Positioning (value prop, differentiators, competitive moat)

2. **Build comparison tables:**
   - Create table for each category
   - Populate data for target company and all competitors
   - Mark each dimension as POD (Point of Differentiation) or POP (Point of Parity)

3. **Differentiation analysis:**
   - Identify clear points of differentiation (where companies differ meaningfully)
   - Identify points of parity (commoditized features)
   - Identify unique advantages (features only one company has)
   - Assess strategic importance of each differentiator

4. **Create positioning map:**
   - Select two key dimensions (e.g., price vs features)
   - Plot target company and competitors on 2x2 map
   - Identify whitespace and competitive clusters

5. **Feature comparison deep dive:**
   - For technical products: Detailed feature-by-feature comparison
   - Calculate feature scores for each company

6. **Strategic implications:**
   - Strengths vs competition
   - Weaknesses vs competition
   - Opportunities (gaps in competitor offerings)
   - Threats (competitive pressure areas)

7. **Create output:** `06-competitive-matrix.md`
   - Comparison tables across all dimensions
   - Differentiation analysis
   - Positioning map
   - Feature comparison (if applicable)
   - Strategic implications
   - Key takeaways and recommendations

8. **Update progress:**
   ```json
   {
     "completed_phases": ["phase_1", "phase_2", "phase_3", "phase_4", "phase_5", "phase_6"],
     "current_phase": 7
   }
   ```

**Resumability:**
- If `06-competitive-matrix.md` exists, skip or refresh if requested

---

### Phase 7: Claims Verification

**Objective:** Verify marketing claims made by target company against evidence.

**Template:** Use `references/claim-verification-guide.md` for methodology.

**Actions:**

1. **Extract claims from target company materials:**
   - Review `01-target-company-summary.md` for captured claims
   - Visit company website, product pages, about page
   - Review any pitch decks or marketing materials provided
   - Compile comprehensive list of distinct claims

2. **Categorize claims:**
   - Technical performance claims
   - Market position claims
   - Customer/traction claims
   - Funding/financial claims
   - Product capability claims
   - Team/credentials claims
   - Differentiation claims

3. **Verify each claim:**
   - Search for evidence (GitHub metrics, third-party sources, docs)
   - Check against competitor analysis (for comparative claims)
   - Apply evidence hierarchy (verifiable metrics > third-party > company claims)
   - Assign verification status:
     - ✅ Verified (strong evidence)
     - ✓ Likely true (circumstantial evidence)
     - ⚠️ Unverified (no evidence found)
     - ❌ Contradicted (evidence suggests false)

4. **Document findings:**
   - Create verification table for each claim category
   - Calculate summary statistics (% verified, % unverified, etc.)
   - Identify red flags (contradicted or highly misleading claims)
   - Highlight well-supported claims

5. **Assess overall credibility:**
   - Pattern analysis (do they make verifiable claims generally?)
   - Severity assessment (minor exaggerations vs material misrepresentations)
   - Transparency evaluation (do they provide evidence?)
   - Comparison to industry norms

6. **Create output:** `07-claims-verification.md`
   - Summary statistics table
   - Detailed claim analysis by category
   - Red flags identified
   - Well-supported claims
   - Overall credibility assessment
   - Key takeaways and recommendations

7. **Update progress:**
   ```json
   {
     "completed_phases": ["phase_1", "phase_2", "phase_3", "phase_4", "phase_5", "phase_6", "phase_7"],
     "current_phase": 8
   }
   ```

**Time Management:**
- Limit to 3-5 searches per claim
- Focus on most critical claims (business-critical, differentiating, quantitative)
- If many claims, prioritize top 15-20 most important ones

**Resumability:**
- If `07-claims-verification.md` exists, skip or refresh if requested

---

### Phase 8: Market Analysis

**Objective:** Assess total addressable market (TAM), ideal customer profiles (ICPs), and market penetration levels.

**Actions:**

1. **Research total addressable market (TAM):**
   - Web search: `[market category] market size`
   - Look for industry analyst reports (Gartner, IDC, Forrester)
   - Check market research summaries
   - Estimate TAM range (conservative to optimistic)
   - Note methodology and confidence level

2. **Define ideal customer profiles (ICPs):**
   - Based on target company positioning (from Phase 1)
   - Identify distinct ICP segments:
     - Company size (enterprise, mid-market, SMB, startups)
     - Industry verticals
     - Use cases
     - Geographic regions
     - Technical sophistication
   - Estimate size of each ICP segment

3. **Assess market penetration:**
   - **Target company penetration:**
     - Estimate current customers (from Phase 1)
     - Calculate penetration rate (customers / TAM)
     - Growth trajectory
   - **Competitor penetration:**
     - Estimate top competitors' customer bases
     - Calculate their penetration rates
     - Identify market leaders by penetration

4. **Market dynamics analysis:**
   - Market maturity (emerging, growth, mature, declining)
   - Growth trends
   - Consolidation trends
   - Barriers to entry
   - Regulatory factors
   - Technology trends

5. **Opportunity assessment:**
   - Underserved segments
   - Geographic expansion opportunities
   - Adjacent markets
   - Emerging use cases

6. **Create output:** `08-market-analysis.md`
   - TAM estimation and methodology
   - ICP definitions and segment sizes
   - Market penetration analysis (target + competitors)
   - Market dynamics and trends
   - Opportunity assessment
   - Strategic implications

7. **Update progress:**
   ```json
   {
     "completed_phases": ["phase_1", "phase_2", "phase_3", "phase_4", "phase_5", "phase_6", "phase_7", "phase_8"],
     "current_phase": 9
   }
   ```

**Fallback Strategies:**
- If TAM data not found: Provide conservative estimate with clear assumptions
- If ICP unclear: Use competitor ICPs as proxy
- If penetration data unavailable: Provide qualitative assessment (high/medium/low penetration)

**Resumability:**
- If `08-market-analysis.md` exists, skip or refresh if requested

---

### Phase 9: Summary Generation

**Objective:** Synthesize all findings into a streamlined, readable executive summary (2-3 pages).

**Actions:**

1. **Review all phase outputs:**
   - Load and review files from phases 1-8
   - Extract key insights from each phase
   - Identify most critical findings

2. **Structure executive summary:**

   **Section 1: Target Company Overview (3-4 paragraphs)**
   - Company description and value proposition
   - Product/technology summary
   - Funding and team
   - Market positioning

   **Section 2: Competitive Landscape (4-5 paragraphs)**
   - Overview of competitive intensity
   - Key competitors identified (list top 5-7)
   - Threat level distribution (X high, Y medium, Z low)
   - Most significant competitive threats
   - Competitive positioning summary

   **Section 3: Differentiation Analysis (3-4 paragraphs)**
   - Key points of differentiation (strengths)
   - Points of parity (commoditized areas)
   - Unique advantages
   - Competitive weaknesses/gaps

   **Section 4: Market Opportunity (3 paragraphs)**
   - TAM and market size
   - Target ICPs and market segments
   - Penetration levels (target + competitors)
   - Market dynamics and growth trends

   **Section 5: Claims Credibility (2-3 paragraphs)**
   - Overall credibility assessment
   - Key verified strengths
   - Red flags or concerns
   - Summary of claim verification

   **Section 6: Key Findings (Bullet points)**
   - Top 5-7 most important findings
   - Most critical competitive threats
   - Strongest differentiation points
   - Biggest risks/concerns
   - Best opportunities

   **Section 7: Recommendations (Bullet points)**
   - Strategic recommendations (3-5)
   - Monitoring priorities
   - Areas for further investigation

3. **Create output:** `summary.md`
   - Streamlined, highly readable format
   - Focus on key insights, not exhaustive detail
   - Use clear section headers
   - Include selective data points (not full tables)
   - Write for executive audience

4. **Update progress:**
   ```json
   {
     "completed_phases": ["phase_1", "phase_2", "phase_3", "phase_4", "phase_5", "phase_6", "phase_7", "phase_8", "phase_9"],
     "current_phase": "complete",
     "phase_status": {"phase_9": "completed"},
     "completion_date": "2025-01-10T15:00:00Z"
   }
   ```

5. **Final message to user:**
   - Report completion
   - Provide path to `summary.md` and other outputs
   - Highlight key findings
   - Suggest next steps or follow-up analyses

**Resumability:**
- If `summary.md` exists but other phases were updated, regenerate summary
- Otherwise skip if already complete

---

## Resumption Logic

### Starting a Market Assessment

When the skill is invoked:

1. **Check for existing project:**
   ```
   Path: users/{username}/{project}/market-assessment/
   ```

2. **If directory doesn't exist:**
   - Create directory structure
   - Initialize progress.json
   - Start from Phase 1

3. **If directory exists:**
   - Read progress.json
   - Report completed phases
   - Ask user:
     ```
     Found existing market assessment for {company}.
     Completed phases: [list]

     Options:
     1. Continue from where we left off (Phase X)
     2. Re-run specific phases (which ones?)
     3. Start fresh (delete all and restart)
     4. Just show me the summary
     ```

4. **Based on user choice:**
   - **Continue:** Start from next incomplete phase
   - **Re-run:** Delete specified output files, re-run those phases
   - **Start fresh:** Delete all outputs, start from Phase 1
   - **Show summary:** Read and display summary.md

### Pausing and Resuming Across Conversations

**To pause:**
- User can stop at any point
- Progress is automatically saved after each phase
- No special action required

**To resume:**
- User invokes skill again in new conversation
- Skill reads progress.json automatically
- Continues from last incomplete phase
- Context from completed phases loaded from saved files (not in conversation history)

**Key resumability features:**
- Each phase saves output immediately upon completion
- progress.json updated after every phase
- Phases are independent - can skip completed ones
- Large data (competitor details) saved to files, not kept in context
- Can regenerate any phase by deleting its output file

---

## Error Handling & Robustness

### Common Issues and Solutions

**Issue: Web search not finding competitors**
- **Solution:** Broaden search terms, try adjacent markets, use minimum 5 competitors
- **Fallback:** Proceed with fewer competitors and note limitation

**Issue: GitHub/documentation not available for technical product**
- **Solution:** Continue with website analysis, third-party reviews, and limited tech assessment
- **Fallback:** Note as information gap, assess based on available info

**Issue: Limited financial/funding information**
- **Solution:** Note as "Unknown", proceed with analysis using available signals
- **Fallback:** Assess threat level with lower confidence, focus on product/market factors

**Issue: Running low on context**
- **Solution:** Save current phase, summarize previous findings, continue
- **Fallback:** User can restart skill - it will load only essential context from files

**Issue: Phase taking too long**
- **Solution:** Time-box research (e.g., 15 min per competitor), accept incomplete data
- **Fallback:** Note information gaps, proceed to next phase

**Issue: Skill gets stuck on a step**
- **Solution:** User can delete that phase's output file and try again
- **Fallback:** Skip problematic phase, continue with remaining phases, note gap in summary

### Quality Assurance

**Before saving each phase output:**
- Verify file has substantive content (not empty template)
- Include confidence level and information gaps
- Note limitations and uncertainties
- Save even if incomplete (partial data better than nothing)

**Update progress conservatively:**
- Only mark phase complete if output file successfully created
- If error occurs, leave phase as incomplete so it's retried

---

## Reference Materials

This skill includes comprehensive reference templates in `references/`:

### competitor-research-template.md
Structured template for analyzing each competitor. Covers:
- Company overview
- Product & technology (including GitHub analysis)
- Funding & financial health
- Market positioning
- Competitive analysis vs target
- Threat assessment
- Information quality assessment

**When to use:** During Phase 3 (Competitor Deep Research) for each competitor

### competitive-matrix-template.md
Framework for building comparative analysis across multiple dimensions. Includes:
- Comparison dimension categories (Product, Market, Company, Strategy)
- Differentiation vs parity analysis
- Positioning maps
- Feature comparison tables
- Strategic implications (SWOT)

**When to use:** During Phase 6 (Competitive Matrix)

### threat-assessment-rubric.md
Quantitative scoring framework for assessing competitive threats. Provides:
- 7-dimension scoring system (0-10 scale each)
- Weighted threat calculation (0-100 total)
- Qualitative adjustment factors
- HIGH/MEDIUM/LOW threat level mapping
- Monitoring recommendations

**When to use:** During Phase 5 (Threat Assessment) for each competitor

### claim-verification-guide.md
Methodology for verifying marketing claims systematically. Covers:
- Verification status taxonomy (✅/✓/⚠️/❌)
- Evidence hierarchy (strongest to weakest)
- Claim categories (technical, market, traction, financial, etc.)
- Verification strategies for each category
- Red flags and credibility assessment

**When to use:** During Phase 7 (Claims Verification)

**How to use references:**
- Read reference file when starting relevant phase
- Follow template structure for consistency
- Adapt as needed for specific context
- Reference file patterns in your outputs

---

## Tips for Effective Market Assessment

### Research Best Practices

1. **Start broad, then focus:**
   - Cast wide net in competitor identification
   - Narrow down to most relevant competitors
   - Deep dive on highest-threat competitors

2. **Prioritize technical validation:**
   - For technical products: Always check GitHub if available
   - Read actual documentation, not just marketing
   - Compare code/architecture, not just claims

3. **Use multiple sources:**
   - Don't rely on company claims alone
   - Cross-reference multiple sources
   - Prefer verifiable data over assertions

4. **Be objective:**
   - Note uncertainties and confidence levels
   - Don't assume - verify when possible
   - Include both strengths and weaknesses

5. **Think critically:**
   - Question marketing claims
   - Look for contradictions
   - Consider alternative explanations

### Time Management

- **Quick assessment (2-3 hours):**
  - 5-8 competitors, lighter research, focus on summary

- **Standard assessment (4-6 hours):**
  - 10-15 competitors, thorough research, complete all phases

- **Comprehensive assessment (8-12 hours):**
  - 15-20 competitors, deep research, extensive analysis

**Adjust scope based on needs and time constraints.**

### Maintaining Context Efficiency

- Save outputs frequently
- Summarize previous findings when loading from files
- Don't keep full competitor details in context - refer to files
- If context grows too large: pause, restart, skill will load efficiently from progress

---

## Integration with Multi-User Job Queue System

This skill is designed to work within the multi-user job queue system:

### File Paths

- **Inputs:** `users/{username}/inputs/` - Uploaded company info, pitch decks
- **Company Research:** `users/{username}/{project}/company-research/` - Prior research
- **Outputs:** `users/{username}/{project}/market-assessment/` - This skill's outputs

### Workflow Integration

1. **User submits job via web interface:**
   - Uploads company information (pitch deck, URLs, notes)
   - Selects "market-assessment" skill/workflow
   - Specifies project name (e.g., "ggml")

2. **Queue watcher picks up job:**
   - Loads uploaded files from `users/{username}/inputs/`
   - Invokes market-assessment skill
   - Provides context: username, project, input file paths

3. **Skill executes:**
   - Reads inputs from specified paths
   - Checks for existing company-research folder
   - Creates market-assessment folder if needed
   - Runs analysis phases with resumability
   - Saves outputs to `users/{username}/{project}/market-assessment/`

4. **Job completion:**
   - Skill reports completion
   - User can view/download outputs via web interface
   - Summary.md provides executive-level overview
   - Detailed phase outputs available for deep dives

### Multi-Tenant Isolation

- All file operations scoped to user's directory
- No access to other users' data
- Project-specific subdirectories maintain organization
- Admins can access any user's data for support

---

## Frequently Asked Questions

**Q: What if I don't have much information about the company?**
A: The skill will work with minimal inputs (even just a company name). It will gather information via web search and note gaps in the analysis.

**Q: Can I pause the analysis and continue later?**
A: Yes! The skill saves progress after each phase. Simply invoke the skill again, and it will pick up where you left off.

**Q: What if I want to re-run just one phase?**
A: Delete that phase's output file, then run the skill again. It will detect the missing file and re-run that phase.

**Q: How long does a full analysis take?**
A: Typically 4-6 hours for a standard analysis (10-15 competitors). You can reduce scope for faster results or expand for deeper analysis.

**Q: What if competitor information is limited?**
A: The skill will note information gaps and proceed with available data. Lower confidence levels will be indicated in the analysis.

**Q: Can I use this for non-technical companies?**
A: Yes! The skill adapts to different company types. GitHub analysis is skipped if not applicable.

**Q: What's the output format?**
A: All outputs are Markdown files. The summary.md provides an executive-level overview (2-3 pages), while phase files contain detailed analysis.

**Q: How many competitors should be analyzed?**
A: Aim for 10-15 competitors for balanced coverage. Can go higher (20) for comprehensive analysis or lower (5-8) for quick assessment.

**Q: Can I customize the analysis?**
A: Yes! You can modify which phases to run, skip less relevant sections, or add custom analysis. The framework is flexible.

**Q: What if the skill runs out of context?**
A: The skill is designed to manage context efficiently by saving to files. If needed, pause and restart - it will load only essential context from saved files.
