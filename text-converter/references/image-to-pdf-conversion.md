# Image to PDF Conversion

## When to Use This Workflow

Use this when you encounter:
- Screenshots of slides or documents saved as image files (.png, .jpg, .jpeg, .webp)
- Multiple image files that appear to be sequential slides or pages
- User requests to convert images before extraction

## Benefits of Converting to PDF First

1. **Searchable text layer**: PDFs can have embedded text for easier extraction
2. **Better archival format**: Single PDF vs. many image files
3. **Easier extraction**: PDF extraction workflow is more reliable than image extraction
4. **Page ordering**: PDFs maintain sequence automatically

## Conversion Workflow

### Step 1: Detect Image Batch

Scan the source folder and identify:
- Image files with sequential naming (e.g., slide1.png, slide2.png, or 1.png, 2.png)
- Groups of images in the same subfolder
- File count: If 3+ images, offer batch conversion

### Step 2: Offer Conversion

Ask user:
```
"I detected [N] image files that appear to be slides/documents.
Would you like me to convert them to a searchable PDF first?
This will make extraction more accurate and create a better archival format."

Options: Yes / No / Convert only specific files
```

### Step 3: Execute Conversion (macOS)

Use macOS Automator to convert images to PDF:

```bash
cd /path/to/source/folder

# Convert all PNG files to a single PDF
automator -i *.png "/System/Library/Automator/Create PDF.workflow"

# Or convert specific file types
automator -i *.jpg "/System/Library/Automator/Create PDF.workflow"
```

**Output**: Creates a PDF named with the folder name or date stamp

**Alternative for individual files:**
```bash
# Convert single image
automator -i image.png "/System/Library/Automator/Create PDF.workflow"
```

### Step 4: Rename Output

Rename the generated PDF to match user's preference:
```bash
mv "Create PDF.pdf" "converted-slides.pdf"
```

Or use the folder name:
```bash
FOLDER_NAME=$(basename "$PWD")
mv "Create PDF.pdf" "${FOLDER_NAME}.pdf"
```

### Step 5: Verify Conversion

Check the PDF was created successfully:
```bash
ls -lh *.pdf
```

If successful, proceed with PDF extraction workflow instead of image extraction.

## Troubleshooting

**If Automator fails:**
- Check that images exist: `ls -l *.png`
- Try converting in smaller batches (10-20 images at a time)
- Ensure image files are readable: `file *.png`

**If Automator is not available:**
- Fall back to image extraction workflow
- Note to user that PDF conversion was not possible

## Notes

- This workflow is macOS-specific (uses Automator)
- Images are converted in alphabetical/numerical order
- Original image files are preserved (not deleted)
- The resulting PDF may not have searchable text unless images contain OCR data
