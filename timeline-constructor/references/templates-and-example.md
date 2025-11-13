# Output Templates and Worked Example

This document provides templates for all three deliverables and a complete worked example demonstrating the timeline-constructor pattern.

---

## Part A: Output Templates

### Template 1: claims-inventory.md

```markdown
# [Entity Name] Claims Inventory

**Source**: [Dataroom folder path]
**Date Extracted**: [YYYY-MM-DD]
**Entity Type**: [GP / Founder / Company / Firm]

---

## KEY Claim 1: [Claim Category - e.g., Sourcing Differentiator]

**Exact Quote**: "[Direct quote from marketing materials]"
**Source**: [Document name, page number or section]

### Supporting Sub-Claims:
- [ ] **Sub-claim 1.1**: [Specific example, metric, or proof point]
  - Source: [Document reference]
- [ ] **Sub-claim 1.2**: [Specific example, metric, or proof point]
  - Source: [Document reference]
- [ ] **Sub-claim 1.3**: [Specific example, metric, or proof point]
  - Source: [Document reference]

---

## KEY Claim 2: [Claim Category - e.g., Right to Win]

**Exact Quote**: "[Direct quote from marketing materials]"
**Source**: [Document name, page number or section]

### Supporting Sub-Claims:
- [ ] **Sub-claim 2.1**: [Specific example, metric, or proof point]
  - Source: [Document reference]
- [ ] **Sub-claim 2.2**: [Specific example, metric, or proof point]
  - Source: [Document reference]

---

## KEY Claim 3: [Claim Category - e.g., Network Quality]

[Repeat structure]

---

## Narrative Arc

**How [Entity] tells their story:**

[Chronological summary of how entity frames their journey - what they emphasize, what order they present milestones, what language they use (e.g., "pioneered," "first," "early," "predicted"), what time periods they focus on vs. skip over]

**Key framing elements:**
- [Element 1: e.g., "Emphasizes 2019 as 'thesis formation year'"]
- [Element 2: e.g., "Highlights 5 'winner' companies, no mention of others"]
- [Element 3: e.g., "Claims 'early' positioning across multiple categories"]
```

---

### Template 2: objective-timeline.md

```markdown
# [Entity Name] Objective Timeline

**Research Folder**: [Path to research materials]
**Date Created**: [YYYY-MM-DD]

---

## Event Timeline

| Date | Event | Relevance | Source | Tier | Verification |
|------|-------|-----------|--------|------|--------------|
| YYYY-MM-DD | [Brief event description] | [Which KEY/sub-claim this relates to] | [Filename or URL] | [1/2/3] | [✅/⚠️/❓/❌/🕐] |
| YYYY-MM-DD | [Brief event description] | [Which KEY/sub-claim this relates to] | [Filename or URL] | [1/2/3] | [✅/⚠️/❓/❌/🕐] |
| YYYY-MM-DD | [Brief event description] | [Which KEY/sub-claim this relates to] | [Filename or URL] | [1/2/3] | [✅/⚠️/❓/❌/🕐] |

---

## Timeline Notes

**Coverage Period**: [Earliest date] to [Latest date]

**Source Distribution**:
- Tier 1 (Entity-controlled): [Count] events
- Tier 2 (Affiliated): [Count] events
- Tier 3 (Independent): [Count] events

**Potential Gaps**:
- [Note any conspicuous timeline gaps, e.g., "No events between 2020-2022"]
- [Note any events found in research but not in claims, suggesting potential omissions]
```

---

### Template 3: validation-report.md

```markdown
# [Entity Name] Narrative Validation Report

**Date**: [YYYY-MM-DD]
**Research Source**: [Folder path]
**Analyst**: Claude (timeline-constructor skill)

---

## Executive Summary

**Overall Credibility Assessment**: [High / Medium-High / Medium / Medium-Low / Low]

**Key Findings**:
- [Finding 1: e.g., "3 of 5 KEY claims verified by independent sources"]
- [Finding 2: e.g., "Timing issues identified in thought leadership claims"]
- [Finding 3: e.g., "2 critical omissions: failed investments not disclosed"]
- [Finding 4: e.g., "Network claims largely unverified (Tier 1 sources only)"]

**Red Flags**: [Yes / No]
- [If yes, list specific red flags]

---

## Claims Validation

### KEY Claim 1: [Title]

**Overall Status**: [✅/⚠️/❓/❌/🕐]

| Sub-Claim | Verification | Evidence Summary |
|-----------|--------------|------------------|
| [Sub-claim 1.1] | [✅/⚠️/❓/❌/🕐] | [Brief reasoning: what sources confirm/contradict, timing analysis] |
| [Sub-claim 1.2] | [✅/⚠️/❓/❌/🕐] | [Brief reasoning] |
| [Sub-claim 1.3] | [✅/⚠️/❓/❌/🕐] | [Brief reasoning] |

**Analysis**: [1-2 paragraphs synthesizing validation results for this KEY claim. What's the pattern? Is it generally verified, partially supported, or problematic?]

---

### KEY Claim 2: [Title]

[Repeat structure]

---

## Critical Omissions

### Omission 1: [Title]
**What's Missing**: [Description of omitted information]
**Why It's Critical**: [Materiality - why this matters for credibility assessment]
**Evidence**: [What in timeline/research reveals this omission]

### Omission 2: [Title]
[Repeat structure]

---

## Timing Analysis

**Thought Leadership vs. Action:**
- [Pattern summary: Does thought leadership precede or follow investments/actions?]
- [Specific examples of timing discrepancies]

**"Early Investor" Claims:**
- [Analysis of pre-consensus vs. post-consensus timing]
- [Specific examples with date gaps]

---

## Source Quality Assessment

**Entity-Controlled Sources (Tier 1)**:
- [List key documents: pitch decks, website, blog posts, etc.]
- **Reliability Note**: Self-reported, unverified claims

**Affiliated Sources (Tier 2)**:
- [List: portfolio company materials, friendly press, etc.]
- **Reliability Note**: Aligned interests, not independent

**Independent Sources (Tier 3)**:
- [List: news articles, filings, third-party data, etc.]
- **Verification Status**: [How much of the narrative is confirmed by Tier 3 sources?]

**Verification Gaps**:
- [What couldn't be verified due to lack of independent sources?]

---

## Recommendations

**Investment Decision Implications**:
- [How does credibility assessment impact diligence or decision?]

**Next Steps for Further Validation**:
- [Specific actions: additional sources to check, questions to ask entity, reference calls, etc.]

**Risk Assessment**:
- [Based on omissions and conflicts, what risks are revealed?]
```

---

## Part B: Worked Example - Dillon Dunteman GP Analysis

### Scenario

**Entity**: Dillon Dunteman (GP at Example Ventures)
**Marketing Focus**: Early-stage vertical SaaS investor with proprietary sourcing and thought leadership
**Research Folder**: `research/people/dillon-dunteman/`

---

### Claims Inventory (Excerpt)

**KEY Claim 1: "Proprietary sourcing in vertical SaaS"**

Sub-claims extracted from dataroom:
- "Invested in Company X pre-institutional" (Source: Portfolio page)
- "Built vertical SaaS thesis in 2019" (Source: Substack)
- "5 vertical SaaS winners in portfolio" (Source: Pitch deck, slide 8)
- "First investor in Company X, 18 months before a16z" (Source: Case study)

**KEY Claim 2: "Right to win through founder network"**

Sub-claims:
- "First call for YC vertical SaaS founders" (Source: GP bio)
- "Portfolio founders refer 40% of deal flow" (Source: Pitch deck, slide 12)

---

### Objective Timeline (Excerpt)

| Date | Event | Relevance | Source | Tier | Verification |
|------|-------|-----------|--------|------|--------------|
| 2019-03-15 | Invested $250K in Company X seed round | Sourcing claim 1.1, 1.4 | research/deals/company-x.md | 1 | ⚠️ |
| 2019-06-01 | Published "My Vertical SaaS Thesis" on Substack | Thought leadership claim 1.2 | research/gp/articles/substack-archive.md | 1 | ⚠️ |
| 2020-01-10 | Company X Series A: $10M, a16z lead | Consensus timing benchmark | research/deals/company-x.md | 3 | ✅ |
| 2020-03-20 | Company Y (vertical SaaS) shut down | Potential omission | research/deals/company-y.md | 2 | ✅ |
| 2020-11-05 | Company Z (vertical SaaS) shut down | Potential omission | research/deals/company-z.md | 2 | ✅ |
| 2021-02-14 | Invested $500K in Company W seed | Sourcing claim (part of "5 winners") | research/deals/company-w.md | 1 | ⚠️ |

---

### Validation Results

#### KEY Claim 1: "Proprietary sourcing in vertical SaaS"

| Sub-Claim | Verification | Evidence Summary |
|-----------|--------------|------------------|
| "Invested in Company X pre-institutional" | ✅ Verified | Invested 2019-03-15, a16z Series A 2020-01-10 (10 months gap = pre-consensus) |
| "Built vertical SaaS thesis in 2019" | 🕐 Timing Issue | Published Substack 2019-06-01, AFTER investing in Company X on 2019-03-15 (retroactive framing) |
| "5 vertical SaaS winners" | ❌ Conflicting | Marketing claims 5 winners, but research shows 2 shut-downs (Companies Y, Z) not mentioned. Actual: 3 active, 2 failed = selective disclosure |
| "First investor in Company X, 18 months before a16z" | ⚠️ Partial | Timeline shows 10 months (not 18). Directionally true but overstated. |

**Analysis**: Sourcing claim is partially verified. Investment in Company X was genuinely pre-consensus (✅), but thought leadership followed investment rather than preceded it (🕐). The "5 winners" claim excludes 2 failures (❌), revealing selective disclosure. Timing is exaggerated (18 vs 10 months).

#### KEY Claim 2: "Right to win through founder network"

| Sub-Claim | Verification | Evidence Summary |
|-----------|--------------|------------------|
| "First call for YC vertical SaaS founders" | ❓ Unverified | Only Tier 1 source (GP bio). No independent confirmation. |
| "40% of deal flow from founder referrals" | ❓ Unverified | Only Tier 1 source (pitch deck). Self-reported metric. |

**Analysis**: Network claims rely entirely on entity-controlled sources. No independent validation available in research folder.

---

### Critical Omissions

**Omission 1: Failed Investments (Companies Y and Z)**
- **What's Missing**: 2 vertical SaaS portfolio companies shut down in 2020
- **Why Critical**: Marketing presents "5 winners" narrative, omitting 40% failure rate (2 of 5)
- **Evidence**: Timeline shows Company Y shut down 2020-03-20, Company Z shut down 2020-11-05

**Omission 2: Retroactive Thought Leadership**
- **What's Missing**: Substack thesis published AFTER first investment, not before
- **Why Critical**: Marketing implies thesis preceded action ("built thesis in 2019, then invested"), but timeline shows reverse
- **Evidence**: Investment 2019-03-15 precedes Substack 2019-06-01 by 2.5 months

---

### Pattern Analysis

**Thought Leadership vs. Action:**
- Published vertical SaaS thesis on 2019-06-01
- First vertical SaaS investment on 2019-03-15 (2.5 months BEFORE writing about it)
- **Pattern**: Retroactive narrative construction. Writing follows investments rather than predicting them.

**"Early Investor" Claims:**
- Company X investment was genuinely pre-consensus (10 months before a16z Series A = ✅)
- However, timing is overstated in marketing (claimed 18 months, actual 10 months)

**Selective Disclosure:**
- Marketing showcases 5 "winners," but omits 2 failures
- Actual portfolio: 3 active + 2 shut-downs = 60% success rate, not 100% as marketing implies

---

### Conclusion

**Credibility Assessment**: Medium

Dillon's core "early investor" claim is directionally accurate (did invest pre-consensus in Company X), but marketing narrative exhibits:
- **Timing exaggeration** (18 vs 10 months)
- **Retroactive framing** (wrote thesis after investing, not before)
- **Selective disclosure** (omits 40% failure rate)
- **Unverified network claims** (no independent sources)

**Recommendation**: Verify network claims through reference calls with portfolio founders. Ask about the 2 failed investments and how they inform investment thesis.
