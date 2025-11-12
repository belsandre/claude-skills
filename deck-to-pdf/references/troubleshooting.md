# Troubleshooting Guide

This document covers common issues and solutions when using the deck-to-pdf skill.

## Installation Issues

### Python Dependencies

**Problem**: `ModuleNotFoundError: No module named 'selenium'`

**Solution**:
```bash
cd /path/to/deck-to-pdf
pip3 install -r scripts/requirements.txt
```

**Problem**: Pip install fails with permission errors

**Solution**:
```bash
# Use user install
pip3 install --user -r scripts/requirements.txt

# Or use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip3 install -r scripts/requirements.txt
```

---

### Chrome and ChromeDriver

**Problem**: `selenium.common.exceptions.SessionNotCreatedException: Message: session not created`

**Solution**:
- Selenium 4.x automatically manages ChromeDriver
- Ensure Google Chrome is installed on your system
- Update Chrome to the latest version

**On macOS**:
```bash
# Check if Chrome is installed
ls /Applications/Google\ Chrome.app

# If not, install via Homebrew
brew install --cask google-chrome
```

**On Linux**:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install google-chrome-stable

# Fedora
sudo dnf install google-chrome-stable
```

**On Windows**:
- Download and install from https://www.google.com/chrome/

---

### OCR Dependencies

**Problem**: `ocrmypdf` command not found or OCR processing fails

**Solution** - Install OCR dependencies:

**On macOS**:
```bash
brew install tesseract
brew install ghostscript
pip3 install ocrmypdf
```

**On Linux (Ubuntu/Debian)**:
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install ghostscript
pip3 install ocrmypdf
```

**On Windows**:
- Install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
- Install Ghostscript: https://www.ghostscript.com/download/gsdnload.html
- Add both to PATH
- Run: `pip3 install ocrmypdf`

**Workaround**: If OCR installation is problematic, use `--skip-ocr` flag

---

## Runtime Issues

### Platform Detection Failures

**Problem**: "Unable to detect presentation platform" error

**Solution**:
1. Verify URL matches supported platform patterns:
   - Pitch: `https://pitch.com/v/[id]`
   - Google Slides: `https://docs.google.com/presentation/d/e/[id]/pub`
   - Figma: `https://www.figma.com/proto/[id]/[name]`
   - Canva: `https://www.canva.com/design/[id]/[name]/view`

2. Check if URL is accessible in regular browser

3. Run with `--disable-headless` to see what page loads

**Problem**: Platform detected incorrectly

**Solution**:
- Platform detection logic is in `utils/sources.py`
- Check if URL or page content matches expected patterns
- May need to update detection logic if platform changed their structure

---

### Navigation Issues

**Problem**: Script gets stuck on a slide and never advances

**Solutions**:

1. **Pitch.com** - Animation detection timeout:
   ```python
   # In sources.py, increase wait time in pitch_at_slide_end()
   time.sleep(2)  # Increase this value
   ```

2. **Any platform** - Next button not found:
   - Run with `--disable-headless` to see what's happening
   - Check if platform changed their UI structure
   - Verify slide navigation works manually in browser

3. **Network issues** - Slow loading:
   - Increase wait times in `slide_downloader.py`
   - Check internet connection stability

**Problem**: Script advances too quickly before slide fully loads

**Solution**:
```python
# In slide_downloader.py, increase wait times
time.sleep(3)  # Increase delay between slides
```

---

### Screenshot Issues

**Problem**: Screenshots are blank or mostly black

**Solutions**:
1. Increase wait time before screenshot
2. Check if slides use lazy loading (wait longer)
3. Disable headless mode to verify slides load visually
4. Check viewport size matches expected resolution

**Problem**: Screenshots have incorrect aspect ratio

**Solution**:
- Verify resolution settings in `download_deck.py`
- Check if platform enforces specific aspect ratios
- Adjust viewport size in `slide_downloader.py`

**Problem**: Screenshots missing content (cutoff edges)

**Solution**:
- Disable border removal: `--skip-border-removal`
- Adjust viewport size to be larger
- Check if platform has responsive design that hides content

---

### Border Removal Issues

**Problem**: Important content cropped out

**Solution**:
```bash
# Skip border removal entirely
python3 scripts/download_deck.py [url] --skip-border-removal
```

**Problem**: Borders not removed despite enabled

**Solution**:
- Check if all slides have consistent borders (algorithm requires consistency)
- Verify slides actually have black borders to remove
- May need to adjust detection threshold in `_crop_black_borders()` method

---

### OCR Issues

**Problem**: OCR processing takes extremely long time

**Solutions**:
1. Use lower resolution: `-r HD` (OCR is faster on smaller images)
2. Skip OCR entirely: `--skip-ocr`
3. Process in batches (OCR subset of slides)

**Problem**: OCR text quality is poor

**Solutions**:
1. Use higher resolution: `-r 8K` (better source for OCR)
2. Ensure slides have clear, high-contrast text
3. Check Tesseract language settings (default is English)

**Problem**: `ocrmypdf` fails with cryptic error

**Solutions**:
1. Verify all dependencies installed correctly
2. Check file permissions on output directory
3. Try processing without OCR first to isolate issue
4. Check ocrmypdf logs for specific error details

---

### Output Issues

**Problem**: PDF not created, no error message

**Solution**:
1. Check `decks/` directory exists
2. Verify write permissions on `decks/` folder
3. Check disk space availability
4. Look for error messages in console output

**Problem**: PDF filename is just numbers/random characters

**Solution**:
- Presentation title contains no alphabetic characters
- Filename is sanitized to only include a-z, A-Z
- Script falls back to UUID if no valid characters
- Manually rename PDF after generation

**Problem**: PDF file size is extremely large

**Solutions**:
1. Use lower resolution: `-r HD` instead of 8K
2. Skip OCR (OCR can increase file size)
3. Compress PDF after generation:
   ```bash
   gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
      -dNOPAUSE -dQUIET -dBATCH \
      -sOutputFile=compressed.pdf original.pdf
   ```

---

## Platform-Specific Issues

### Pitch.com

**Problem**: Animations not fully captured

**Solution**:
- Increase wait time in `pitch_at_slide_end()` function
- Some complex animations may require manual intervention
- Consider using `--disable-headless` to verify animation completion

**Problem**: "Made with Pitch" popover blocks content

**Solution**:
- Script should auto-dismiss this
- If not working, update the dismissal selector in `sources.py`
- Check if Pitch.com changed their UI structure

---

### Google Slides

**Problem**: "Presentation must be published to web" error

**Solution**:
1. Open presentation in Google Slides
2. Go to File → Share → Publish to web
3. Click "Publish" button
4. Copy the published URL (should contain `/pub`)
5. Use the published URL, not the edit URL

**Problem**: Slide count incorrect

**Solution**:
- Some slides may be hidden in published version
- Check Google Slides settings to ensure all slides are published
- Verify `data-slides-count` attribute in page source

---

### Figma

**Problem**: Prototype controls visible in screenshots

**Solution**:
- Script should hide these automatically
- If not working, check CSS selector in `sources.py`
- Verify Figma hasn't changed their prototype viewer structure

**Problem**: Interactive elements trigger during navigation

**Solution**:
- This is a known limitation with complex Figma prototypes
- Try increasing wait times between clicks
- Consider exporting from Figma directly if interactions interfere

---

### Canva

**Problem**: Header/footer visible in screenshots

**Solution**:
- Ensure using view mode URL (`/view`), not edit mode
- Script should hide these; if not, check selectors in `sources.py`
- Verify Canva URL is in correct format

**Problem**: Cookie consent dialog reappears

**Solution**:
- Script should auto-accept on first appearance
- If persistent, may need to update selector in `sources.py`
- Check browser cookies/cache settings

---

## Performance Issues

**Problem**: Download takes much longer than expected

**Solutions**:
1. Use lower resolution: `-r HD`
2. Skip OCR: `--skip-ocr`
3. Skip border removal: `--skip-border-removal`
4. Check network speed (slow connection affects loading)
5. Check CPU usage (OCR is CPU-intensive)

**Problem**: High memory usage

**Solutions**:
1. Process fewer slides at a time
2. Use lower resolution
3. Close other applications
4. Monitor with `top` or Activity Monitor

**Problem**: Browser crashes during scraping

**Solutions**:
1. Reduce resolution (less memory per screenshot)
2. Check available RAM
3. Update Chrome to latest version
4. Try headless mode (uses less memory): default behavior

---

## Debugging Strategies

### Enable Verbose Output

**Problem**: Need to see what's happening

**Solution**:
```bash
# Run with visible browser
python3 scripts/download_deck.py [url] --disable-headless

# Add print statements in code
# In slide_downloader.py, add:
print(f"Processing slide {i+1}/{slide_count}")
print(f"Source detected: {self.source}")
```

### Test with Known Working Decks

Create test cases:
```bash
# Test each platform with known working URLs
python3 scripts/download_deck.py https://pitch.com/v/test-deck -r HD --skip-ocr
```

### Isolate the Problem

1. Test with minimal flags (HD, no OCR, no border removal)
2. Add features one by one to identify which causes issue
3. Test different platforms to see if issue is platform-specific

### Check Dependencies

```bash
# Verify all required packages installed
pip3 list | grep selenium
pip3 list | grep Pillow
pip3 list | grep ocrmypdf

# Check Chrome version
google-chrome --version  # Linux
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version  # macOS
```

---

## Getting Help

If issues persist after troubleshooting:

1. **Check for platform changes**:
   - Presentation platforms frequently update their UI
   - Selectors in `sources.py` may need updating

2. **Review error messages**:
   - Full error stack trace often reveals root cause
   - Search error message online for common solutions

3. **Test with different presentations**:
   - Issue may be specific to one presentation
   - Try multiple presentations from same platform

4. **Update dependencies**:
   ```bash
   pip3 install --upgrade -r scripts/requirements.txt
   ```

5. **Check Python version**:
   ```bash
   python3 --version  # Should be 3.8 or higher
   ```

---

## Known Limitations

1. **Private presentations**: Cannot access presentations requiring authentication
2. **Complex interactions**: Some highly interactive prototypes may not work perfectly
3. **Custom navigation**: Presentations with custom navigation (non-standard controls) may fail
4. **Embedded videos**: Videos are captured as static frames, not playable
5. **Animations**: Animation timing is estimated; some complex animations may not fully complete
6. **Platform updates**: UI changes on platforms can break scraping logic
7. **Rate limiting**: Some platforms may rate limit repeated requests (rarely an issue)

---

## Preventive Measures

1. **Always test first**: Run with HD and visible browser first
2. **Keep dependencies updated**: Regularly update Chrome and Python packages
3. **Verify URLs**: Check URL format before running script
4. **Monitor output**: Watch console output for warnings/errors
5. **Backup important decks**: Don't rely solely on automated downloads for critical presentations
