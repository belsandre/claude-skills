# Timeline Constructor Methodology

This document provides detailed methodology for extracting claims, building timelines, and validating marketing narratives against objective evidence.

---

## Part A: Claims Extraction

### Where to Look

Extract claims from **dataroom materials ONLY** (no external search in this phase):
- Fund pitch decks and investment memos
- Portfolio materials and case studies
- GP bios, team pages, and About sections
- Marketing decks and one-pagers
- Blog posts, Substack articles, social media profiles
- Thought leadership content (talks, podcasts, interviews)

### GP-Specific Claim Categories

| Category | What to Look For | Example Claims |
|----------|------------------|----------------|
| **Sourcing Differentiator** | How they find/originate deals uniquely | "Proprietary deal flow from industry network"<br>"First call for YC founders in vertical SaaS"<br>"Thematic investing approach yields pre-institutional access" |
| **Right to Win Competitive Deals** | Why founders choose them over competitors | "Founder-friendly terms and governance"<br>"Deep operational experience in category X"<br>"Track record in sector yields pattern recognition" |
| **Network Quality** | Access, relationships, and connections | "C-suite network in Fortune 500 enterprise buyers"<br>"Board experience at 3 unicorns"<br>"Connections to Sequoia/a16z for follow-on funding" |
| **Other Key Claims** | Sector expertise, value-add, performance, thought leadership | "10 years investing in fintech"<br>"Portfolio MOIC of 5x+"<br>"Published 50+ essays predicting trends"<br>"Hands-on go-to-market support" |

**For other entity types**, adapt categories:
- **Founders**: Product innovation, market insight, execution track record, technical expertise
- **Companies**: Traction metrics, competitive moat, market timing, technology differentiation
- **Firms**: Portfolio performance, fund returns, market positioning, LP value-add

### Hierarchical Claims Structure

Build claims in two tiers:

**Tier 1: KEY Claims (3-5 total)**
- The hero marketing messages
- Core value propositions
- What entity wants to be known for
- Usually found in pitch deck opening, bio summary, homepage hero section

**Tier 2: Sub-Claims (2-10 per KEY claim)**
- Specific examples supporting KEY claim
- Metrics, case studies, or proof points
- Concrete instances demonstrating the KEY claim
- Found throughout detailed materials

**Example for GP:**

**KEY Claim 1: "Proprietary sourcing in vertical SaaS"**
- Sub-claim: "Invested in 5 companies at pre-seed before institutional rounds"
- Sub-claim: "Built and run Slack community with 2,000+ vertical SaaS founders"
- Sub-claim: "First investor in Company X (18 months before a16z Series A)"
- Sub-claim: "Thesis-driven approach with published vertical SaaS framework from 2019"

**KEY Claim 2: "Right to win through deep founder relationships"**
- Sub-claim: "Portfolio founders refer 40% of new deal flow"
- Sub-claim: "Average 15 reference calls per investment"
- Sub-claim: "Intro'd 8 portfolio companies to Series A leads (Sequoia, Benchmark, etc.)"

**KEY Claim 3: "Network quality in enterprise buyer ecosystem"**
- Sub-claim: "Advisory board includes 5 Fortune 500 CIOs"
- Sub-claim: "Facilitate enterprise pilot programs for portfolio"
- Sub-claim: "20-year career at Oracle provides deep customer relationships"

### Narrative Arc Extraction

Document how entity tells their chronological story:
- What order do they present their journey?
- What milestones do they emphasize?
- What time periods do they focus on vs. gloss over?
- How do they frame timing ("early," "before it was consensus," "predicted")?
- What framing language do they use ("pioneered," "first," "only")?

This narrative arc will be compared against objective timeline to identify retroactive framing or selective emphasis.

### Output Format

Save to `claims-inventory.md` using template from `templates-and-example.md`.

---

## Part B: Timeline Construction

### Event Extraction

Source events from **provided research folder ONLY** (no external search). Look for:

**Investment Events:**
- Investment date, amount, stage, company name
- Entry valuation if available
- Co-investors

**Exit Events:**
- Exit date, type (acquisition, IPO, shut-down), outcome
- Exit valuation, return multiple if available

**Thought Leadership Events:**
- Publication date of articles, blog posts, Substack essays
- Speaking engagement dates (conferences, podcasts)
- Topic/thesis described
- Predictions or frameworks published

**Funding Events (for company validation):**
- Funding round dates, amounts, lead investors
- Valuation milestones
- When company reached "consensus" (institutional tier-1 VC backing)

**Organizational Events:**
- Team hires, departures, promotions
- Office openings, expansions
- Strategic pivots or repositioning

**Performance Metrics:**
- ARR milestones, user growth
- Valuation updates
- Partnership announcements

### Event Format (Minimal)

For each event extracted, capture:

| Field | Description |
|-------|-------------|
| **Date** | YYYY-MM-DD (or YYYY-MM, YYYY-QX if only quarter known) |
| **Event** | Brief description (1-2 sentences max) |
| **Relevance** | Which KEY or sub-claim does this event validate, contradict, or relate to? |
| **Source** | Filename or URL from research folder |
| **Tier** | 1 (entity-controlled), 2 (affiliated), 3 (independent) |
| **Verification** | Leave blank for now; filled in Phase 3 |

### Timeline Focus

Only extract events **relevant to validating claims**. This is not an exhaustive chronology of every event in entity's history. Focus on:
- Events cited in claims (directly or implied)
- Events that would validate or contradict claims
- Events conspicuously absent from marketing narrative (potential omissions)
- Timing benchmarks (e.g., when did company become "consensus," enabling pre/post determination)

### Output Format

Save to `objective-timeline.md` using template from `templates-and-example.md`.

---

## Part C: Validation Framework

### Source Tiering System

Classify every source by objectivity and control:

| Tier | Description | Examples | Reliability |
|------|-------------|----------|-------------|
| **Tier 1: Entity-Controlled** | Created, published, or directly controlled by entity | Dataroom materials, pitch decks, entity website, entity blog/Substack, entity social media, portfolio pages | ⚠️ Low objectivity - self-reported, unverified |
| **Tier 2: Affiliated** | Created by related parties or friendly sources | Portfolio company descriptions (written by GP), co-investor quotes, friendly press (sponsored content), partnership announcements | ⚠️ Medium objectivity - aligned interests, not independent |
| **Tier 3: Independent** | Created by unaffiliated third parties | News articles (TechCrunch, WSJ), SEC filings, PitchBook/Crunchbase data, third-party research, court documents, regulatory filings | ✅ High objectivity - independent verification |

**General rule**: Claims supported only by Tier 1 sources are **unverified**. Claims supported by Tier 3 sources are **verified**.

### Verification Categories

Assign each claim (KEY and sub-claim) one of these statuses:

| Status | Symbol | Criteria | Meaning |
|--------|--------|----------|---------|
| **Verified** | ✅ | Tier 3 independent sources confirm claim and timing | Claim is objectively validated |
| **Partial** | ⚠️ | Claim is directionally true but timing is uncertain, or only Tier 2 sources confirm | Claim likely true but not fully verified |
| **Unverified** | ❓ | Only Tier 1 (entity-controlled) sources support this claim | No independent validation; claim is self-reported |
| **Conflicting** | ❌ | Independent sources contradict the claim directly | Claim is likely false or misleading |
| **Timing Issue** | 🕐 | Event happened, but timing contradicts claim framing | Retroactive narrative; claim happened "after the fact" not "before" |

### Timing Analysis Methodology

Timing is critical for validating predictive, prescient, or "early" claims.

#### For Investment Claims ("early investor," "pre-consensus," "before it was hot")

**Decision Rules:**

| Scenario | Investment Timing | Consensus Timing | Status |
|----------|-------------------|------------------|--------|
| **Prescient** | >90 days before consensus | Consensus = Series A+ from tier-1 VC (Sequoia, a16z, Benchmark, etc.) | ✅ Verified as "early" |
| **Reactive** | <90 days from consensus | Within same quarter or adjacent | ⚠️ Partial (early-ish but not clearly prescient) |
| **Retroactive** | After consensus | Investment post-dates tier-1 institutional round | ❌ Conflicting if claimed as "early" |

**Example:**
- Claim: "Early investor in Company X"
- Investment: 2019-03-15 (seed, $250K)
- Consensus: 2020-01-10 (Series A, $10M, a16z lead)
- Gap: 10 months
- **Status**: ✅ Verified as early (>90 days before consensus)

#### For Thought Leadership Claims ("predicted," "wrote about before," "saw trend early")

**Decision Rules:**

| Scenario | Article/Talk Date | Investment/Event Date | Status |
|----------|-------------------|----------------------|--------|
| **Predictive** | Article precedes investment by >30 days | Published before acting on thesis | ✅ Verified as predictive |
| **Concurrent** | Article within ±30 days of investment | Published around same time as action | ⚠️ Partial (not clearly predictive) |
| **Retroactive** | Article follows investment | Published after acting on thesis | 🕐 Timing Issue (retroactive framing) |

**Example:**
- Claim: "Built vertical SaaS thesis early, before investing"
- Investment in vertical SaaS Co X: 2019-03-15
- Published "Vertical SaaS Thesis" on Substack: 2019-06-01
- Gap: +2.5 months (article AFTER investment)
- **Status**: 🕐 Timing Issue (wrote about it after investing, not before)

#### For Network Claims ("introduced founders to VCs," "board experience at unicorns")

**Decision Rules:**
- Verify timing: Did relationship exist **when claimed** or was it formed later?
- Verify causality: Did GP actually make introduction, or did founder source VC independently?
- Check Tier 3 sources for independent confirmation (press releases naming GP role, LinkedIn timelines, etc.)

### Critical Omissions Framework

Identify important events **absent from marketing narrative**:

#### What Counts as "Critical" Omission:

| Type | Description | Why Critical |
|------|-------------|--------------|
| **Failed Investments** | Write-offs, shut-down companies, zombie companies in portfolio | Reveals selection bias in marketing (only showcasing winners) |
| **Material Timeline Gaps** | Multi-year periods with no investments or activity | Suggests narrative skips unflattering periods (e.g., 2020-2022 gap might hide failed fund) |
| **Conflicts of Interest** | Undisclosed relationships, side businesses, competing funds | Impacts credibility and fiduciary alignment |
| **Contradictory Evidence** | Third-party sources showing different narrative (e.g., founder says they sourced VC, not vice versa) | Directly contradicts marketing claims |

#### What Does NOT Count as Critical:

- Minor details, background trivia
- Every single investment (focus on material omissions of failures, not exhaustive listing)
- Irrelevant historical facts

#### How to Identify Omissions:

1. Review objective timeline for events **not mentioned** in claims inventory or narrative arc
2. Check for conspicuous gaps: Are there failures? Quiet periods? Competing narratives?
3. Look for "best hits only" pattern: Marketing showcases 5 winners but research folder shows 15 total investments (10 omitted)
4. Cross-reference external sources (if available in research folder) to see if they tell a different story

### Output Format

Save to `validation-report.md` using template from `templates-and-example.md`.

---

## Summary: Three-Phase Process

1. **Phase 1 (Claims)**: Extract KEY + sub-claims from dataroom → `claims-inventory.md`
2. **Phase 2 (Timeline)**: Extract events from research folder → `objective-timeline.md`
3. **Phase 3 (Validation)**: Cross-reference claims vs timeline, assign verification status, identify omissions → `validation-report.md`

**Progressive Loading**: Load this methodology file as needed during phases. Load templates during Phase 3 for output formatting.
