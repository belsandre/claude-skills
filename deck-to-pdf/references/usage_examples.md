# Usage Examples

This document provides common usage patterns and examples for the deck-to-pdf skill.

## Basic Usage

### Standard Download (4K with OCR)
```bash
cd /path/to/deck-to-pdf
python3 scripts/download_deck.py https://pitch.com/v/example-deck
```

**Result**: Downloads deck at 4K resolution (3840x2160), applies border removal, and creates searchable PDF with OCR.

---

## Resolution Options

### HD Resolution (1920x1080)
```bash
python3 scripts/download_deck.py https://pitch.com/v/example-deck -r HD
```
**Use case**: Faster downloads, smaller file sizes (good for quick previews)

### 4K Resolution (3840x2160) - Default
```bash
python3 scripts/download_deck.py https://pitch.com/v/example-deck -r 4K
```
**Use case**: High quality for professional use, presentations, sharing

### 8K Resolution (7680x4320)
```bash
python3 scripts/download_deck.py https://pitch.com/v/example-deck -r 8K
```
**Use case**: Maximum quality for printing, detailed design work
**Note**: Large file sizes, slower processing

---

## OCR Options

### Skip OCR (Faster Processing)
```bash
python3 scripts/download_deck.py https://pitch.com/v/example-deck --skip-ocr
```
**Use case**: When searchable text is not needed, or for faster processing
**Benefit**: Reduces processing time by 30-50%

### With OCR (Default)
```bash
python3 scripts/download_deck.py https://pitch.com/v/example-deck
```
**Use case**: Create searchable PDFs for easy text search and copy-paste
**Requirement**: Requires `ocrmypdf`, Tesseract, and Ghostscript installed

---

## Border Removal Options

### Skip Border Removal
```bash
python3 scripts/download_deck.py https://pitch.com/v/example-deck --skip-border-removal
```
**Use case**: When slides don't have black borders or speed is priority
**Benefit**: Faster processing (skips cropping analysis)

### With Border Removal (Default)
```bash
python3 scripts/download_deck.py https://pitch.com/v/example-deck
```
**Use case**: Clean PDFs without black borders around slides
**Process**: Automatically detects and removes consistent borders

---

## Headless Mode Options

### Disable Headless (Show Browser)
```bash
python3 scripts/download_deck.py https://pitch.com/v/example-deck --disable-headless
```
**Use case**: Debugging, seeing what's happening, troubleshooting issues
**Note**: Browser window will be visible during scraping

### Headless Mode (Default)
```bash
python3 scripts/download_deck.py https://pitch.com/v/example-deck
```
**Use case**: Normal operation, background processing
**Benefit**: No browser window, cleaner experience

---

## Platform-Specific Examples

### Pitch.com
```bash
# Standard Pitch deck
python3 scripts/download_deck.py https://pitch.com/v/startup-pitch-xyz123

# Fast download (HD, no OCR, no border removal)
python3 scripts/download_deck.py https://pitch.com/v/startup-pitch-xyz123 -r HD --skip-ocr --skip-border-removal
```

### Google Slides
```bash
# Published Google Slides deck
python3 scripts/download_deck.py https://docs.google.com/presentation/d/e/2PACX-abc123/pub

# High quality with visible browser (for debugging)
python3 scripts/download_deck.py https://docs.google.com/presentation/d/e/2PACX-abc123/pub -r 8K --disable-headless
```

### Figma Slides
```bash
# Figma prototype presentation
python3 scripts/download_deck.py https://www.figma.com/proto/abc123/My-Design

# 4K with no OCR (image-heavy deck)
python3 scripts/download_deck.py https://www.figma.com/proto/abc123/My-Design --skip-ocr
```

### Canva
```bash
# Canva presentation in view mode
python3 scripts/download_deck.py https://www.canva.com/design/DAFxxx/Presentation/view

# HD for quick preview
python3 scripts/download_deck.py https://www.canva.com/design/DAFxxx/Presentation/view -r HD --skip-ocr
```

---

## Combined Options Examples

### Maximum Quality (8K + OCR + Border Removal)
```bash
python3 scripts/download_deck.py https://pitch.com/v/important-deck -r 8K
```
**Use case**: Professional presentations, printing, archiving
**Time**: Slowest, highest quality

### Maximum Speed (HD + No OCR + No Border Removal)
```bash
python3 scripts/download_deck.py https://pitch.com/v/quick-preview -r HD --skip-ocr --skip-border-removal
```
**Use case**: Quick previews, testing, rough drafts
**Time**: Fastest, lower quality

### Balanced (4K + OCR + Border Removal) - Default
```bash
python3 scripts/download_deck.py https://pitch.com/v/standard-deck
```
**Use case**: Most common use case, good quality and searchable
**Time**: Moderate processing time

### Debugging Mode (Show Browser + HD)
```bash
python3 scripts/download_deck.py https://pitch.com/v/problem-deck -r HD --disable-headless
```
**Use case**: Troubleshooting issues, seeing navigation problems
**Benefit**: Visual feedback during scraping

---

## Output Location

All PDFs are saved to the `decks/` directory:

```
deck-to-pdf/
└── decks/
    ├── StartupPitchDeck.pdf
    ├── Q4Results.pdf
    └── DesignPresentation.pdf
```

**Filename**: Automatically sanitized from presentation title (alphabetic characters only)

---

## Integration with Claude Code Workflows

### In a User Request Context
```
User: "Download this pitch deck as a PDF: https://pitch.com/v/example"

Claude:
1. Navigate to deck-to-pdf directory
2. Run: python3 scripts/download_deck.py https://pitch.com/v/example
3. Wait for completion
4. PDF saved to decks/ directory
5. Report filename and location to user
```

### Multiple Decks
```bash
# Process multiple decks sequentially
python3 scripts/download_deck.py https://pitch.com/v/deck1
python3 scripts/download_deck.py https://canva.com/design/DAFxxx/deck2/view
python3 scripts/download_deck.py https://docs.google.com/presentation/d/e/2PACX-abc/pub
```

### Custom Output Directory
To save to a different directory, move the PDF after generation:
```bash
python3 scripts/download_deck.py https://pitch.com/v/example
mv decks/ExampleDeck.pdf /path/to/custom/location/
```

---

## Command-Line Arguments Reference

```
positional arguments:
  url                   URL of the presentation deck

options:
  -h, --help            Show help message and exit
  -r {HD,4K,8K}, --resolution {HD,4K,8K}
                        Resolution for screenshots (default: 4K)
                        HD=1920x1080, 4K=3840x2160, 8K=7680x4320
  --skip-ocr            Skip OCR processing (faster, but PDF won't be searchable)
  --skip-border-removal Skip automatic border removal (faster processing)
  --disable-headless    Show browser window during scraping (for debugging)
```

---

## Expected Processing Times

Approximate times for a 20-slide deck (times vary by platform and network speed):

| Configuration | Time | Use Case |
|--------------|------|----------|
| HD + No OCR + No Border | 1-2 min | Quick preview |
| HD + OCR + Border | 2-3 min | Fast searchable |
| 4K + OCR + Border (Default) | 3-5 min | Standard quality |
| 8K + OCR + Border | 8-12 min | Maximum quality |

**Factors affecting speed**:
- Slide count (more slides = longer time)
- Platform (Pitch with animations is slower)
- Resolution (8K is ~4x slower than HD)
- OCR processing (adds 30-50% time)
- Border removal analysis (adds ~20% time)
- Network speed (downloading slide assets)

---

## Error Handling

### Common Errors

**Platform not detected**:
```bash
Error: Unable to detect presentation platform. Supported platforms: Pitch, Google Slides, Figma, Canva
```
→ Check URL format matches supported platforms (see supported_platforms.md)

**Google Slides not published**:
```bash
Error: Google Slides presentation must be published to web
```
→ In Google Slides: File → Share → Publish to web

**OCR failed**:
```bash
Error: OCR processing failed. Run with --skip-ocr to bypass
```
→ Either install OCR dependencies or use `--skip-ocr` flag

**ChromeDriver issues**:
```bash
Error: ChromeDriver not found or incompatible
```
→ Selenium 4.x should auto-manage ChromeDriver, but ensure Chrome browser is installed

---

## Tips and Best Practices

1. **Start with defaults**: Use default settings first, then adjust based on needs
2. **Use HD for testing**: Test with HD resolution first to ensure deck downloads correctly
3. **Watch the first run**: Use `--disable-headless` for first run to see if navigation works
4. **Check output directory**: Verify `decks/` folder exists and has write permissions
5. **Network stability**: Ensure stable internet connection for reliable downloads
6. **Platform updates**: If a platform changes their UI, navigation may break (report issues)
7. **Batch processing**: For multiple decks, create a simple bash loop or Python script
