# 101 Linux Commands eBook Generation

This directory contains the setup for generating the "101 Linux Commands" eBook using [Ibis Next](https://github.com/Hi-Folks/ibis-next).

## Features

- **Multiple Output Formats**: Generate PDF, EPUB, and HTML versions of the eBook
- **Theme Support**: PDF generation supports both light and dark themes
- **Professional Styling**: Custom CSS and HTML templates for each format
- **Cover Image Support**: Automatic cover page generation
- **Table of Contents**: Auto-generated navigation for all formats

## Directory Structure

```
ebook/en/
├── assets/
│   ├── cover.jpg           # Cover image
│   ├── style.css           # CSS for EPUB generation
│   ├── theme-dark.html     # Dark theme for PDF
│   ├── theme-light.html    # Light theme for PDF
│   └── theme-html.html     # Template for HTML generation
├── content/                # Markdown source files
├── export/                 # Generated eBook files
└── ibis.php               # Configuration file
```

## Configuration

The `ibis.php` file contains all configuration options:

- **title**: Book title
- **author**: Author information
- **header**: Page header styling
- **cover**: Cover image configuration
- **fonts**: Custom font definitions
- **sample**: Sample page ranges

## Generation Commands

From the project root directory, run:

```bash
# Generate PDF (light theme)
composer run pdf

# Generate PDF (dark theme)
composer run pdf-dark

# Generate EPUB
composer run epub

# Generate HTML
composer run html
```

## Output Files

Generated files are saved in the `export/` directory:

- `101-linux-commands-ebook-light.pdf` - PDF with light theme
- `101-linux-commands-ebook-dark.pdf` - PDF with dark theme
- `101-linux-commands-ebook.epub` - EPUB format
- `101-linux-commands-ebook.html` - HTML format

## Advanced Features

### Custom Content Selection

To generate a partial eBook with specific files, uncomment and modify the `md_file_list` configuration in `ibis.php`:

```php
'md_file_list' => [
    '001-the-ls-command.md',
    '002-the-cd-command.md',
    '003-the-cat-tac-command.md',
],
```

### Sample Generation

Generate sample PDFs with specific page ranges:

```bash
vendor/bin/ibis-next sample
vendor/bin/ibis-next sample dark
```

### Custom Themes

Modify the HTML template files in the `assets/` directory to customize the appearance of your eBooks.

## Requirements

- PHP 8.1 or higher
- Composer
- GD extension enabled

## Support

For issues related to Ibis Next, visit: https://github.com/Hi-Folks/ibis-next
