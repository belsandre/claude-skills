# Supported Platforms

This document provides detailed information about each supported presentation platform, including URL patterns, platform-specific behaviors, and known limitations.

## Platform Overview

The deck-to-pdf skill supports downloading presentations from the following platforms:
1. **Pitch.com** - Modern presentation platform with animation support
2. **Google Slides** - Google's presentation tool (Publish to Web mode only)
3. **Figma Slides** - Figma's presentation mode
4. **Canva** - Canva's presentation builder

---

## 1. Pitch.com

### URL Pattern
- `https://pitch.com/v/[presentation-id]`
- Example: `https://pitch.com/v/example-deck-xyz123`

### Platform-Specific Behavior
- **Animation Handling**: Pitch decks often have slide animations. The scraper automatically clicks through animations by detecting when animations complete (using `pitch_at_slide_end()` function).
- **Cookie Consent**: Automatically accepts cookie consent dialogs if present.
- **Branding Popover**: Automatically dismisses the "Made with Pitch" popover if it appears.

### Detection Method
- URL contains "pitch.com"
- Backup: Page title contains "Pitch" or "Deck"

### Known Limitations
- Requires animations to complete before moving to next slide (may be slower)
- Some complex animations might need manual adjustment

### Navigation
- Uses arrow key (Right arrow) to navigate between slides
- Detects slide end by monitoring slide container changes

---

## 2. Google Slides

### URL Pattern
- Must be in "Publish to Web" mode
- `https://docs.google.com/presentation/d/e/[presentation-id]/pub`
- Example: `https://docs.google.com/presentation/d/e/2PACX-xxx/pub`

### Platform-Specific Behavior
- **Publish to Web Required**: Standard Google Slides URLs will not work; presentation must be published to web
- **Slide Count**: Automatically extracts total slide count from page metadata
- **No Login Required**: Works with public presentations only

### Detection Method
- URL contains "docs.google.com/presentation" and "/pub"
- Page contains Google Slides-specific elements

### Known Limitations
- Only works with presentations set to "Publish to Web"
- Private presentations require manual publishing first
- Animations and transitions are not captured (static slides only)

### Navigation
- Uses next slide button click
- Slide count extracted from `data-slides-count` attribute

---

## 3. Figma Slides

### URL Pattern
- `https://www.figma.com/proto/[file-id]/[presentation-name]`
- Example: `https://www.figma.com/proto/abc123/My-Presentation`

### Platform-Specific Behavior
- **Prototype Controls**: Automatically hides Figma's prototype control overlay
- **Video Handling**: Detects and handles video content by clicking multiple times (similar to Pitch animations)
- **Slide Number Tracking**: Uses Figma's slide number indicator to track progress

### Detection Method
- URL contains "figma.com/proto"
- Page contains Figma prototype viewer elements

### Known Limitations
- Requires prototype mode to be enabled in Figma
- Interactive elements might interfere with screenshots
- Some complex prototypes with custom navigation may not work

### Navigation
- Uses right arrow key for navigation
- Monitors slide number changes to detect navigation completion

---

## 4. Canva

### URL Pattern
- `https://www.canva.com/design/[design-id]/[presentation-name]/view`
- Example: `https://www.canva.com/design/DAFxxx/My-Presentation/view`

### Platform-Specific Behavior
- **Cookie Consent**: Automatically accepts cookie consent dialogs
- **Header/Footer Hiding**: Hides Canva's viewer header and footer for clean screenshots
- **Full-Screen Mode**: Presentation should be in view mode (not edit mode)

### Detection Method
- URL contains "canva.com/design" and "/view"
- Page contains Canva viewer elements

### Known Limitations
- Only works with presentations in view mode
- Edit mode URLs will not work
- Some Canva-specific effects may not render in screenshots

### Navigation
- Uses right arrow key for navigation
- Next button click for slide transitions

---

## Platform Detection Logic

The scraper automatically detects the platform in the following order:

1. **URL-based detection** (primary):
   - Check URL for platform-specific patterns
   - Most reliable method

2. **Content-based detection** (fallback):
   - Analyze page elements and structure
   - Used when URL doesn't clearly indicate platform

3. **Error handling**:
   - If platform cannot be detected, raises an error
   - User receives clear message about unsupported URL

---

## Adding New Platforms

To add support for a new platform:

1. **Add detection logic** in `sources.py`:
   ```python
   def detect_new_platform(driver):
       # Check URL or page content
       return "new_platform" if conditions_met else None
   ```

2. **Add parameter extraction** function:
   ```python
   def get_new_platform_params(driver):
       return {
           "slide_count": ...,
           "next_button": ...,
           "container": ...
       }
   ```

3. **Update detection** in `SlideDownloader._detect_source()`:
   ```python
   elif "newplatform.com" in url:
       self.source = "new_platform"
   ```

4. **Test thoroughly** with multiple presentations from the new platform

---

## Troubleshooting by Platform

### Pitch.com Issues
- **Slow downloads**: Animations take time; use `--skip-border-removal` to speed up
- **Stuck on slide**: Increase wait time in `pitch_at_slide_end()` function

### Google Slides Issues
- **"Not published" error**: Ensure presentation is set to "Publish to Web" in File menu
- **Incorrect slide count**: Check that all slides are visible in published version

### Figma Slides Issues
- **Missing slides**: Ensure prototype mode is properly configured in Figma
- **Controls visible**: Prototype controls should auto-hide; if not, check Figma settings

### Canva Issues
- **Header/footer visible**: Edit mode detected; switch to view mode URL
- **Cookie dialog blocking**: Script should auto-dismiss; if not, manually accept first

---

## URL Validation

Before processing, validate URLs:

```python
# Pitch.com
if "pitch.com/v/" in url:
    valid = True

# Google Slides
if "docs.google.com/presentation" in url and "/pub" in url:
    valid = True

# Figma
if "figma.com/proto/" in url:
    valid = True

# Canva
if "canva.com/design/" in url and "/view" in url:
    valid = True
```

If URL doesn't match any pattern, inform user about supported platforms and URL requirements.
