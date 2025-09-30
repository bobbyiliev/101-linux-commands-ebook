# Contributing

## Pull Requests

### Creating a Pull Request

This book has been designed so that people can easily expand it.
To request us to review changes that you create, you will need to create a pull request.
Creating a pull request is described in
 [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).

### File Location/Types

### [`ebook`](./ebook)

This directory holds all of the translations of the eBook.

### [`ebook/{LANG}`](./ebook/{LANG})

In the `ebook` directory we have the translations of the eBook in different languages.

If you are adding a new translation, make sure to make a copy of the `./ebook/en` directory and use the language code as the new directory name.

### [`ebook/{LANG}/content`](./ebook/{LANG}/content)

All the Markdown files for the '101 Linux commands' eBook are located within the [`content`](./content) directory for the specific language.

For example if you are adding a Bulgarian translation copy the `./ebook/en` folder to `./ebook/bg`, translate the `.md` files in the `content` directory and submit a PR.

### eBook Generation

The project uses [Ibis Next](https://github.com/Hi-Folks/ibis-next) developed by [Roberto Butti](https://github.com/roberto-butti), forked from the original [Ibis](https://github.com/themsaid/ibis/) by [Mohamed Said](https://github.com/themsaid).

Ibis Next supports generating PDF, EPUB, and HTML formats from Markdown content.

## Setup and Usage

1. Install dependencies:
```bash
composer install
```

2. Generate PDF (light theme):
```bash
composer run pdf
```

3. Generate PDF (dark theme):
```bash
composer run pdf-dark
```

4. Generate EPUB:
```bash
composer run epub
```

5. Generate HTML:
```bash
composer run html
```

For more information about Ibis Next, visit: [Getting started with Ibis Next](https://github.com/Hi-Folks/ibis-next)

## Issue Creation

In the event that you have an issue using the guide or have a suggestion for a change but don't want to contribute changes,
 we are more than happy to help.
Make sure that when you create your issue, it follows the format for the type of issue you select
 (it has individual templates for each issue type).

Issue template types include the following:
 - Bug Reporting
 - Feature Requests
 - Help Requests
