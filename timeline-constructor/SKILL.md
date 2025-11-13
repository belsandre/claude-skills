---
name: timeline-constructor
description: Validate entity marketing narratives by comparing key claims against objective timelines, identifying timing discrepancies and critical omissions. Use when analyzing GPs, founders, companies, or firms to assess credibility, verify claims, construct timelines, or identify narrative gaps.
---

# Timeline Constructor

## Overview

This skill validates entity marketing narratives through timeline-based claim verification. It extracts key marketing claims from dataroom materials, builds objective timelines from provided research, and identifies timing discrepancies and critical omissions. The output reveals gaps between marketing narrative and objective reality, enabling credibility assessment for due diligence and investment decisions.

Typical output includes a claims inventory (hierarchical structure of marketing claims), objective timeline (event sequence with source verification), and validation report (claim-by-claim verification with timing analysis).

## When to Use This Skill

Use this skill when:
- Conducting due diligence on GP track records and evaluating "early investor" or thought leadership claims
- Validating founder credentials and assessing execution history versus marketing narrative
- Verifying company claims about traction, competitive positioning, or market timing
- Identifying critical omissions in marketing materials (failed investments, timeline gaps, conflicts)
- Analyzing narrative credibility before investment decisions or partnerships

Example invocations:
- "Use timeline-constructor skill for GP John Doe, research folder at research/people/john-doe/"
- "Validate Company X's marketing claims using timeline-constructor, research in research/deals/company-x/"

## Inputs Required

- **Research folder path**: Location of existing research materials (GP research, company research, or other entity research)
- **Entity name**: Name of GP, founder, company, or firm being analyzed
- **Output location**: Where to save deliverables (claims-inventory.md, objective-timeline.md, validation-report.md)

## Three-Phase Workflow

### Phase 1: Claims Extraction

**Load**: `references/methodology.md` (Part A: Claims Extraction)

Extract KEY marketing claims from dataroom materials provided in research folder. Focus on:
- **GP entities**: Sourcing differentiator, right to win competitive deals, network quality, other claims
- **Other entities**: Adapt categories as needed (product claims, market timing, execution track record)

Build hierarchical structure:
- Identify 3-5 KEY claims (hero marketing messages)
- Document 2-10 sub-claims supporting each KEY claim
- Extract narrative arc (how entity tells their chronological story)

NO external search in this phase. Use only provided research materials.

**Output**: `claims-inventory.md` (template in `references/templates-and-example.md`)

### Phase 2: Objective Timeline

**Load**: `references/methodology.md` (Part B: Timeline Construction)

Extract events from provided research materials relevant to validating claims:
- Investments, exits, product launches, funding rounds
- Thought leadership (articles, talks, predictions)
- Organizational changes, metrics, milestones

Map each event to relevant claims. Use only materials in research folder (no external search).

Capture: Date, event description, relevance to claims, source, source tier (1=entity-controlled, 2=affiliated, 3=independent).

**Output**: `objective-timeline.md` (template in `references/templates-and-example.md`)

### Phase 3: Validation & Gap Analysis

**Load**: `references/methodology.md` (Part C: Validation Framework) and `references/templates-and-example.md`

Cross-reference each claim against objective timeline:
- **Timing analysis**: Did thought leadership precede or follow investments? Are "early investor" claims pre-consensus or post-consensus?
- **Source verification**: Tier 1 (entity-controlled) vs Tier 3 (independent) sources
- **Verification status**: ✅ Verified, ⚠️ Partial, ❓ Unverified, ❌ Conflicting, 🕐 Timing Issue

Identify critical omissions:
- Failed investments or shuttered companies not mentioned
- Material timeline gaps (quiet periods between highlights)
- Conflicts of interest not disclosed
- Contradictory evidence excluded from narrative

**Output**: `validation-report.md` (template in `references/templates-and-example.md`)

## Output Structure

```
{output_location}/
├── claims-inventory.md          # Hierarchical claims from dataroom
├── objective-timeline.md         # Event timeline with verification
└── validation-report.md          # Claim validation + omissions
```

## Resources

### references/methodology.md
Load during Phases 1-3. Contains:
- Part A: Claims extraction methodology (where to look, hierarchical structure, GP claim categories)
- Part B: Timeline construction (event format, extraction process)
- Part C: Validation framework (source tiers, verification categories, timing analysis rules, critical omissions criteria)

### references/templates-and-example.md
Load during Phase 3. Contains:
- Output templates for all three deliverables
- Worked example (Dillon Dunteman GP scenario) showing complete pattern: claims → timeline → validation → omissions

## Model Recommendation

Use **Opus** when invoking this skill for nuanced credibility judgment, pattern recognition, and timing analysis.
