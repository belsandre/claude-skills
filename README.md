# Claude Code Skills

This repository contains custom Claude Code skills for specialized research and analysis workflows.

## Skills

### company-research
Comprehensive research on companies and key people with critical source evaluation, objectivity assessment, and verification status tracking. Outputs structured research summaries with proper sourcing.

**Features:**
- Web search and source extraction
- Source objectivity assessment (High/Medium/Low)
- Verification status (Interested party vs. Independent)
- Critical evaluation of inconsistencies
- Resumability support for long research projects

### deck-to-pdf
Download presentation slides from Pitch.com, Google Slides, Figma Slides, and Canva as searchable PDF files.

### video-downloader
Extract clean article content from URLs and save as readable text without ads or clutter.

### text-converter
Convert folders containing mixed media (images, PDFs, presentations) into faithful markdown reproductions using multi-pass extraction.

### notebooklm
Query Google NotebookLM notebooks for source-grounded, citation-backed answers from Gemini.

### csv-data-summarizer
Analyze CSV files, generate summary statistics, and plot visualizations.

### market-assessment
Analyze companies, identify competitors, assess competitive threats, and build competitive matrices.

### youtube-transcript
Download YouTube video transcripts.

### article-extractor
Extract article content from URLs.

## Installation

These skills are located in `~/.claude/skills/` and are automatically available to Claude Code via the Skill tool.

## Usage

Skills are invoked via the Skill tool in Claude Code. See individual skill SKILL.md files for detailed usage instructions.

## Related

- **Workflows**: See `Prod/users/*/workflows/` for workflow definitions that use these skills
- **Multi-user system**: See `Prod/web_interface/` for the job queue system

## Version

Last updated: 2025-01-12
