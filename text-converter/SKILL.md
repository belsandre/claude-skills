---
name: text-converter
description: Convert folders containing mixed media (images, PDFs, presentations) into faithful markdown reproductions using modular multi-pass extraction. This skill should be used when converting data rooms, presentation decks, or document collections requiring verbatim text accuracy and complex visual structure preservation (network diagrams, pie charts, multi-column layouts).
---

# Text Converter

## Overview

This skill provides modular, multi-pass extraction workflows for converting documents and images to markdown with extreme verbatim accuracy. It uses progressive loading to apply specialized extraction strategies based on visual complexity, reducing hallucinations through verification checklists.

## When to Use This Skill

Use this skill when:
- Converting folders containing mixed media (PDFs, images, presentations, Word docs)
- Processing data rooms or pitch decks with complex visual structures
- Need faithful reproduction (not summaries) of:
  - Network/node diagrams with connections
  - Pie charts or segmented circular layouts
  - Multi-column slide layouts
  - Standard text and charts
- Require verbatim text extraction with verification
- Working with multi-page documents needing complete extraction

Do not use for:
- Simple text extraction (use simpler tools)
- Spreadsheet data (.xlsx files - skill skips these)
- Legal documents (auto-detected and skipped unless user is in legal business)

## Workflow Overview

### Step 1: Initialize or Resume

Check for existing checkpoint in `[folder-name]-md/.text-converter-progress.json`:
- If exists: Offer to continue from checkpoint or start fresh
- If not: Create output folder and initial checkpoint

### Step 2: Scan and Catalog Files

Scan source folder recursively and categorize:
- **Images**: .jpg, .jpeg, .png, .webp, .gif, .bmp, .tiff
- **PDFs**: .pdf
- **Word**: .doc, .docx
- **PowerPoint**: .ppt, .pptx
- **Skip**: .xls, .xlsx, .csv (all spreadsheets)

Identify consolidation groups (sequentially numbered files in same folder).

**2a. Check for Image-to-PDF Conversion Opportunity**

If 3+ image files are detected (especially screenshots of slides/documents):
- Load `references/image-to-pdf-conversion.md`
- Offer to convert images to PDF first using macOS Automator
- If user accepts:
  - Execute conversion to create combined PDF
  - Regenerate file catalog (PDF replaces images in processing queue)
  - Update checkpoint to reflect PDF instead of individual images
  - Process the resulting PDF using streamlined PDF workflow
- If user declines: Continue with image extraction workflow (with per-region verification)

Benefits of conversion: Searchable text, better archival format, faster processing (no per-region verification), single output file.

### Step 3: Process Each File

For each file:

**3a. Detect File Type**

- If `.pdf` → Load `references/pdf-extraction.md`
- If image → Load `references/image-extraction.md` (handles all visual structures including network diagrams, pie charts, multi-column layouts)

**3b. Run Extraction Workflow**

Each reference file defines its own extraction workflow:
- **Images:** Region-based extraction with per-region verification (handles all visual structures: network diagrams, pie charts, multi-column layouts, standard images)
- **PDFs:** Page-by-page extraction with tracing mindset, capturing network relationships and spatial layouts

**3c. Save and Checkpoint**

- Save markdown to `[output-folder]/[mirrored-path]/[filename].md`
- Update checkpoint with completion status
- Preserve exact folder hierarchy

### Step 4: Generate Final Report

Create `EXTRACTION_LOG.md` with:
- Files processed by type
- Extraction references used per file
- Any failed/skipped files

## How Image Extraction Handles Different Visual Structures

The `image-extraction.md` workflow automatically handles all visual structures through its region-based approach:

**Network Diagrams** (circles/nodes with arrows/connections):
- Identifies nodes as regions
- Extracts labels and descriptions
- Captures connection relationships
- Verifies node names and connections

**Pie Charts** (circular/arc layouts with center element):
- Identifies sections as regions
- Extracts items grouped in each section
- Captures center element
- Verifies section labels and completeness

**Multi-Column Layouts** (2-4 vertical sections):
- Identifies columns as regions
- Extracts column headers and content
- Maintains left-to-right ordering
- Verifies alignment and structure

**Standard Content** (text, charts, tables):
- Identifies logical regions
- Extracts text and visual elements
- Verifies verbatim accuracy

## Legal Document Detection

Before processing PDFs, check if primarily legal:
1. Filename contains: "terms", "privacy", "license", "legal", "agreement", "LPA"
2. Sample first 3 + last 3 pages for legal keywords
3. If >50% legal boilerplate → Skip entire document
4. Exception: If user's company is in legal business, process all documents

## Checkpoint System

Checkpoint tracks:
- Which files completed
- Which extraction reference used per file
- Failed files with error messages
- Allows resuming in new conversation

Checkpoint schema:
```json
{
  "source_folder": "/absolute/path",
  "output_folder": "/absolute/path",
  "total_files": 35,
  "completed_files": 15,
  "extraction_references_used": {
    "file1.png": "network-diagram",
    "file2.pdf": "pdf-extraction"
  },
  "completed_list": []
}
```

## Progressive Loading Example

```
User: Convert /path/to/data-room

Skill:
1. Scans folder → finds mixed images and PDFs
2. Checks for image-to-PDF conversion opportunity
   → If 3+ images detected, offers batch conversion
   → If accepted, converts using macOS Automator
   → Catalog regenerates, PDF replaces images in processing queue

3. Processes first file (image with network diagram):
   → Detects image file type
   → Loads references/image-extraction.md only
   → Runs region-based extraction:
     - Identifies regions (network nodes, connections, labels)
     - Extracts each region with tracing mindset
     - Verifies each region (text samples, numbers, completeness)
   → Saves to markdown + checkpoint

4. Processes second file (PDF):
   → Detects PDF file type
   → Loads references/pdf-extraction.md only
   → Runs page-by-page extraction:
     - Extracts text layer + visual elements per page
     - Captures network relationships: "NodeA - connected to NodeB, NodeC"
     - Describes spatial layouts: "3 sections around center"
   → Saves to markdown + checkpoint

5. Continues through all files with appropriate references
6. Generates EXTRACTION_LOG.md
```

## Resources

This skill uses reference files for progressive loading of extraction workflows:

### references/image-to-pdf-conversion.md
Workflow for converting image files (screenshots, slides) to PDF format using macOS Automator. Load when 3+ image files are detected. Offers better extraction quality and archival format.

### references/image-extraction.md
Region-based extraction workflow with per-region verification. Load for all image files. Handles all visual structures including network diagrams, pie charts, multi-column layouts, charts, tables, and standard images. Includes strong verification with "SHOW YOUR WORK" requirements to ensure accuracy.

### references/pdf-extraction.md
Streamlined page-by-page extraction workflow for PDF files. Load for all .pdf files. Includes instructions for capturing network diagram relationships and spatial layouts. No verification required due to reliable text layers in PDFs.

## Quality Improvements vs Single-Pass

**Problem with single-pass:**
- Cognitive overload (text + logos + relationships simultaneously)
- Vision model limits on complex diagrams
- Missing network relationships and spatial layouts
- Confirmation bias

**Multi-pass solution:**
- Each pass has singular focus → less cognitive load → fewer errors
- Specialized workflows for complex structures (network diagrams, pie charts)
- Explicit instructions for capturing relationships and spatial arrangements
- Progressive loading reduces instruction context
- Image-to-PDF conversion option for better extraction quality
