# Universal Image Extraction

Use this for ANY image: slides, diagrams, charts, tables, mixed layouts.

## Core Principle: Tracing Mindset

Extract text like you're tracing over it character-by-character, NOT reading it.
- Don't comprehend/interpret → Just copy what you see
- Don't paraphrase → Character-by-character match required
- Don't batch → Extract one region, output, verify, then next

## Extraction Workflow

### 1. Identify Regions (Visual Structure)

Look at image once. What distinct regions exist?
- **Columns:** Side-by-side sections with headers
- **Timeline:** Horizontal sequence of dates/events
- **Table:** Rows and columns with data
- **Diagram:** Nodes, arrows, connections
- **Text blocks:** Paragraphs, bullet lists

**Output:** "Identified regions: [list]" → STOP

### 2. Extract Per Region (One at a Time)

For EACH region separately:
1. **Focus only on this region** (mentally cover others)
2. **Trace text character-by-character** (not reading)
3. **Read numbers 3 times independently** (check ~, $, M vs B, exact values)
4. **Note logos inline:** "Text Company [logo] more text"

**Output this region completely → STOP before next region**

### 3. MANDATORY Verification (Per Region) - SHOW YOUR WORK

Before moving to next region, verify THIS region by outputting both versions:

**Text verification (3 samples - OUTPUT BOTH VERSIONS):**

For each of 3 random text snippets:
1. OUTPUT: "My extraction says: '[exact text from my extraction]'"
2. Re-read that section from image character-by-character
3. OUTPUT: "Image actually says: '[what I just read from image]'"
4. Compare the two outputs character-by-character
5. If NOT exact match → Re-extract this region NOW

**Number verification (ALL numbers - OUTPUT 3 READINGS):**

1. List all numbers from your extraction: [list them]
2. For EACH number:
   - OUTPUT: "My extraction says: [number with units]"
   - Re-read from image 3 times independently
   - OUTPUT: "Image says: [reading 1] | [reading 2] | [reading 3]"
   - If all 3 readings ≠ my extraction → Re-extract NOW

**Symbol verification:**
- Check for bullets, arrows, triangles in image
- If symbols appear as letters/numbers (A, 4, &, ►), note: "[Triangle bullet shown as 'A']"

**Only proceed to next region if ALL verifications pass with exact matches.**

### 4. Combine All Regions

After all regions extracted and verified individually.

## Examples

**Mixed layout (columns + timeline):**
- Identify: "4 columns at top, timeline at bottom"
- Extract Column 1 → Output → Verify → Extract Column 2 → Output → Verify...
- Extract timeline → Output → Verify
- Combine

**Network diagram:**
- Identify: "Nodes with labels, arrows connecting them"
- Extract nodes region → Output → Verify
- Extract connections region → Output → Verify
- Combine

**Simple slide:**
- Identify: "Title, bullet points, footer"
- Extract each section → Output → Verify per section
- Combine

## Common Errors to Avoid

- ❌ Reading across regions (e.g., left-to-right across columns)
- ❌ Paraphrasing: "Dillon researched" → "He researched"
- ❌ Number errors: $8.8B → $5.0B, ~550 → 500
- ❌ Skipping verification: "I read it 3 times" without actually doing it
- ❌ Batching: Extract all regions then verify (NO - verify each before next)
