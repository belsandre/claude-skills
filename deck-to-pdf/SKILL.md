---
name: deck-to-pdf
description: Download presentation slides from Pitch.com, Google Slides, Figma Slides, and Canva as high-quality searchable PDF files. Use this skill when the user provides a presentation URL and wants to convert it to PDF format, or when asked to download, scrape, or save online presentation decks.
---

# Deck to PDF

## Overview

This skill enables downloading presentation slides from popular online platforms and converting them into high-quality, searchable PDF files. It supports Pitch.com, Google Slides (published to web), Figma Slides (prototype mode), and Canva presentations, with options for resolution, OCR, and border removal.

## When to Use This Skill

Use this skill when:
- User provides a URL to an online presentation (Pitch, Google Slides, Figma, Canva)
- User requests to "download", "convert", "scrape", or "save" a presentation as PDF
- User asks to make a presentation searchable or extract slides
- User mentions needing a local copy of an online deck

**Example user requests:**
- "Download this Pitch deck as a PDF: https://pitch.com/v/example"
- "Convert this Google Slides presentation to PDF"
- "I need a searchable PDF of this Canva presentation"
- "Get me a high-quality PDF of this Figma slides deck"

## Quick Start

### Basic Workflow

1. **Navigate to deck-to-pdf directory**:
   ```bash
   cd /Users/changxu/Agents/Prod/deck-to-pdf
   ```

2. **Run download script with URL**:
   ```bash
   python3 scripts/download_deck.py [URL]
   ```

3. **Wait for completion** - Progress bar shows slide download status

4. **Locate output** - PDF saved in `decks/` directory with sanitized filename

### Default Behavior

By default, the script:
- Downloads at **4K resolution** (3840x2160) for high quality
- **Removes black borders** automatically for clean output
- **Applies OCR** to make PDF searchable
- Runs in **headless mode** (no visible browser window)

## Supported Platforms

### 1. Pitch.com
- **URL pattern**: `https://pitch.com/v/[presentation-id]`
- **Special handling**: Automatically waits for slide animations to complete
- **Use case**: Modern pitch decks with animations

### 2. Google Slides
- **URL pattern**: `https://docs.google.com/presentation/d/e/[id]/pub`
- **Requirement**: Presentation must be "Published to Web" (File → Share → Publish to web)
- **Use case**: Public Google Slides presentations

### 3. Figma Slides
- **URL pattern**: `https://www.figma.com/proto/[file-id]/[name]`
- **Requirement**: Figma prototype mode enabled
- **Special handling**: Hides prototype controls, handles video content
- **Use case**: Design presentations in Figma

### 4. Canva
- **URL pattern**: `https://www.canva.com/design/[id]/[name]/view`
- **Requirement**: View mode (not edit mode)
- **Special handling**: Hides header/footer automatically
- **Use case**: Canva-created presentations

**For detailed platform information**, including troubleshooting platform-specific issues, see `references/supported_platforms.md`.

## Core Capabilities

### 1. Standard Download (4K with OCR)

**Command**:
```bash
python3 scripts/download_deck.py [URL]
```

**Use when**: User wants high-quality, searchable PDF with standard settings

**Result**: 4K resolution PDF with OCR in `decks/` directory

---

### 2. Resolution Selection

Choose resolution based on use case:

**HD (1920x1080) - Fast**:
```bash
python3 scripts/download_deck.py [URL] -r HD
```
**Use when**: Quick previews, smaller file sizes needed, or speed is priority

**4K (3840x2160) - Default**:
```bash
python3 scripts/download_deck.py [URL] -r 4K
```
**Use when**: Professional quality needed, standard output

**8K (7680x4320) - Maximum Quality**:
```bash
python3 scripts/download_deck.py [URL] -r 8K
```
**Use when**: Printing, detailed design work, or maximum quality required
**Note**: Significantly larger files and longer processing time

---

### 3. OCR Control

**With OCR (default)** - Creates searchable PDF:
```bash
python3 scripts/download_deck.py [URL]
```
**Use when**: User needs to search or copy text from PDF

**Without OCR** - Faster processing:
```bash
python3 scripts/download_deck.py [URL] --skip-ocr
```
**Use when**: Searchable text not needed, or faster processing is priority
**Note**: Requires `ocrmypdf`, Tesseract, and Ghostscript for OCR. If not installed, use `--skip-ocr`.

---

### 4. Border Removal

**With border removal (default)** - Clean slides:
```bash
python3 scripts/download_deck.py [URL]
```
**Use when**: Slides have black borders that should be removed

**Without border removal** - Faster:
```bash
python3 scripts/download_deck.py [URL] --skip-border-removal
```
**Use when**: Slides don't have borders, or speed is priority

---

### 5. Debugging Mode

**Show browser during scraping**:
```bash
python3 scripts/download_deck.py [URL] --disable-headless
```
**Use when**:
- Troubleshooting navigation issues
- Verifying slides load correctly
- Debugging platform-specific problems
- First-time testing with new presentation

---

## Common Usage Patterns

### Maximum Quality
```bash
python3 scripts/download_deck.py [URL] -r 8K
```
**Result**: 8K resolution with OCR and border removal
**Time**: Longest (8-12 min for 20 slides)
**Use case**: Professional presentations, printing, archiving

### Maximum Speed
```bash
python3 scripts/download_deck.py [URL] -r HD --skip-ocr --skip-border-removal
```
**Result**: HD resolution, no OCR, no border removal
**Time**: Fastest (1-2 min for 20 slides)
**Use case**: Quick previews, testing, rough drafts

### Balanced (Default)
```bash
python3 scripts/download_deck.py [URL]
```
**Result**: 4K with OCR and border removal
**Time**: Moderate (3-5 min for 20 slides)
**Use case**: Most common, good quality and searchable

### Debugging
```bash
python3 scripts/download_deck.py [URL] -r HD --disable-headless
```
**Result**: Shows browser, HD for faster loading
**Use case**: Troubleshooting navigation or loading issues

---

## Workflow for Processing User Requests

When user requests a presentation download:

1. **Verify URL format** matches supported platforms (see Supported Platforms section)
   - If Google Slides, confirm it's published to web (`/pub` in URL)
   - If Canva, confirm it's in view mode (`/view` in URL)

2. **Navigate to deck-to-pdf directory**:
   ```bash
   cd /Users/changxu/Agents/Prod/deck-to-pdf
   ```

3. **Determine appropriate options** based on user request:
   - High quality needed? → Use `-r 8K`
   - Quick preview? → Use `-r HD --skip-ocr --skip-border-removal`
   - Searchable PDF needed? → Default (includes OCR)
   - First time with this URL? → Add `--disable-headless` to verify

4. **Execute download**:
   ```bash
   python3 scripts/download_deck.py [URL] [options]
   ```

5. **Monitor progress** - Script shows progress bar and slide count

6. **Verify output**:
   ```bash
   ls -lh decks/
   ```

7. **Report to user**:
   - Filename and location: `decks/PresentationName.pdf`
   - File size
   - Resolution used
   - Whether OCR was applied

8. **Handle errors** - If issues occur:
   - Check `references/troubleshooting.md` for common problems
   - Try with `--disable-headless` to see what's happening
   - Verify URL is accessible in regular browser
   - Check platform-specific requirements

---

## Output Details

### File Location
All PDFs saved to: `/Users/changxu/Agents/Prod/deck-to-pdf/decks/`

### Filename Format
- Automatically extracted from presentation title
- Sanitized to include only alphabetic characters (a-z, A-Z)
- Example: `StartupPitchDeck.pdf`, `Q4Results.pdf`

### File Properties
- **Format**: Multi-page PDF
- **Resolution**: Based on `-r` flag (HD/4K/8K)
- **Searchability**: Yes if OCR enabled, No if `--skip-ocr` used
- **File size**: Varies by resolution and slide count
  - HD: ~1-5 MB for 20 slides
  - 4K: ~5-15 MB for 20 slides
  - 8K: ~20-50 MB for 20 slides

---

## Dependencies and Setup

### Required Software

**Python 3.8+** and packages from `scripts/requirements.txt`:
```bash
pip3 install -r scripts/requirements.txt
```

**Google Chrome** - Required for Selenium automation:
- macOS: `brew install --cask google-chrome`
- Linux: `sudo apt-get install google-chrome-stable`
- Windows: Download from https://www.google.com/chrome/

**OCR Tools** (optional, required for `--skip-ocr` to be omitted):
- **Tesseract**: OCR engine
- **Ghostscript**: PDF processing
- **ocrmypdf**: Python wrapper

Install on macOS:
```bash
brew install tesseract ghostscript
pip3 install ocrmypdf
```

**If OCR installation is problematic**, always use `--skip-ocr` flag.

---

## Error Handling

### Common Errors

**"Unable to detect presentation platform"**:
- Verify URL matches supported platform patterns
- Check if URL is accessible in regular browser
- See `references/supported_platforms.md` for valid URL formats

**"Google Slides presentation must be published to web"**:
- Open presentation in Google Slides
- File → Share → Publish to web → Publish
- Use the published URL (contains `/pub`)

**"OCR processing failed"**:
- Install OCR dependencies (Tesseract, Ghostscript)
- Or use `--skip-ocr` to bypass OCR entirely

**ChromeDriver issues**:
- Ensure Google Chrome is installed
- Selenium 4.x auto-manages ChromeDriver
- Update Chrome to latest version

**Navigation stuck on slide**:
- Platform may have changed UI
- Try `--disable-headless` to see what's happening
- Increase wait times in code if animations are slow
- See `references/troubleshooting.md` for platform-specific fixes

---

## Resources

### Scripts

**`scripts/download_deck.py`** - Main entry point:
- Command-line interface for downloading presentations
- Argument parsing (URL, resolution, OCR, headless mode)
- Orchestrates download and OCR workflow

**`scripts/utils/slide_downloader.py`** - Core downloader:
- `SlideDownloader` class with main download logic
- Platform auto-detection
- Screenshot capture and processing
- Border removal and cropping
- PDF generation

**`scripts/utils/sources.py`** - Platform-specific handlers:
- Parameter extraction for each platform
- Platform-specific UI element selectors
- Cookie consent and popup handling
- Animation and video detection logic

**`scripts/requirements.txt`** - Python dependencies:
- Selenium 4.16.0 - Browser automation
- Pillow 10.2.0 - Image processing
- tqdm 4.66.1 - Progress bars
- ocrmypdf 16.0.3 - OCR processing
- Supporting libraries (img2pdf, pikepdf, etc.)

### References

**`references/supported_platforms.md`** - Platform details:
- URL patterns for each platform
- Platform-specific behaviors and limitations
- Detection logic and troubleshooting
- Navigation methods and selectors

**`references/usage_examples.md`** - Common usage patterns:
- Example commands for different scenarios
- Processing time estimates
- Integration with Claude Code workflows
- Command-line argument reference

**`references/troubleshooting.md`** - Problem solving:
- Installation issues (Python, Chrome, OCR)
- Runtime errors (navigation, screenshots, OCR)
- Platform-specific problems
- Performance optimization
- Debugging strategies

---

## Tips and Best Practices

1. **Test with defaults first**: Use standard settings before customizing
2. **Start with HD for testing**: Verify deck downloads correctly at lower resolution first
3. **Use visible browser for debugging**: Add `--disable-headless` for first run with new platform
4. **Check platform requirements**: Google Slides needs publishing, Canva needs view mode
5. **Install OCR dependencies early**: Or plan to use `--skip-ocr` flag
6. **Monitor output directory**: Ensure `decks/` folder exists and has write permissions
7. **Consider file size**: 8K creates large files; use HD/4K unless maximum quality needed
8. **Network stability matters**: Ensure stable internet for reliable downloads
9. **Platform UI changes**: If navigation breaks, platform may have updated UI (check references)
10. **Batch processing**: For multiple decks, run commands sequentially

---

## Advanced Usage

### Multiple Decks
Process multiple presentations sequentially:
```bash
python3 scripts/download_deck.py https://pitch.com/v/deck1
python3 scripts/download_deck.py https://canva.com/design/xxx/deck2/view
python3 scripts/download_deck.py https://docs.google.com/.../pub
```

### Custom Output Location
Move PDF after generation:
```bash
python3 scripts/download_deck.py [URL]
mv decks/DeckName.pdf /path/to/custom/location/
```

### Modifying the Scripts
Scripts can be modified for specific needs:
- Adjust wait times for slow-loading slides
- Change viewport sizes for different aspect ratios
- Update selectors if platforms change their UI
- Add support for new platforms

For detailed modification guidance, read the scripts directly and refer to inline comments.
