# PDF Extraction

For .pdf files specifically.

## Core Principle: Page-by-Page with Tracing Mindset

Same as image extraction, but applied per page:
- Extract text like tracing character-by-character
- Treat each page as separate region
- Capture graphical relationships and spatial layouts

## Extraction Workflow

### 1. Identify Document Structure

Open PDF. Observe:
- Total pages: ___
- Document type: (slides, report, legal, mixed)
- Regions per page: (text blocks, charts, tables, images)

**Output:** "Document has ___ pages, [structure type]" → STOP

### 2. Legal Document Detection (Skip if Detected)

Before extracting, check if primarily legal:
- Filename contains: "LPA", "terms", "agreement", "privacy"
- Sample first 3 + last 3 pages for legal keywords
- If >50% legal boilerplate → Skip entire document
- Exception: Process if user is in legal business

**Output:** "Legal document detected - skipping" OR "Proceeding with extraction"

### 3. Extract Per Page (One at a Time)

For EACH page:
1. **Text layer first:** Use Skill(document-skills:pdf) or Read tool
2. **Visual elements:** Charts, logos, diagrams (if text layer missing anything)
3. **Tracing mindset:** Character-by-character, don't paraphrase
4. **Read numbers carefully:** Check values, units
5. **Network diagrams:** Describe connections between nodes
   - Format: "NodeA (description) - connected to NodeB, NodeC"
   - Example: "Quantinuum (Global Quantum Computing Leader) - connected to GR MOTH (Quantum), agora (Quantum), Normal"
6. **Pie charts/circular layouts:** Identify sections and spatial arrangement
   - Format: "N sections around center: Left (category), Center (hub), Right (category)"
   - Example: "3 sections around Hyperion center: Left (Early-Stage Deeptech Collaborators), Center (HYPERION), Right (Deeptech-Interested Generalists)"
   - Do NOT invent tier structures or hierarchies not present in the visual
7. **Spatial layouts:** Faithfully reproduce the actual visual arrangement, don't impose artificial structures

**Output this page completely → Proceed to next page**

### 4. Combine All Pages

After all pages extracted.

## Common Errors to Avoid

- ❌ Skipping pages → Must process EVERY page
- ❌ Missing footnotes → Check bottom of EACH page
- ❌ Paraphrasing → Must be verbatim
- ❌ Inventing structures → Faithfully reproduce actual visual layout (e.g., don't add "Tier 1-4" if not present)
- ❌ Missing relationships → In network diagrams, describe connections between nodes
- ❌ Assuming text layer is complete → Always check visual elements

## Multi-Page Structure

Preserve document flow:
```markdown
# [Document Title]

**Pages:** [total]

---

## Page 1

[Extracted content]

---

## Page 2

[Extracted content]

...
```
