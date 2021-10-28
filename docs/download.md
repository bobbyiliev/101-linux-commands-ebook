---

pdf:
    parent_folder: "ebook/en/export"
    dark:
        filename: "101-linux-commands-ebook-dark.pdf"
    light:
        filename: "101-linux-commands-ebook-light.pdf"

---

{% import 'macros/all.j2' as macros %}

# Download This Book as a PDF

- **Dark** mode {{ macros.common.link_to_pdf(pdf.parent_folder ~ '/' ~ pdf.dark.filename, message="PDF", icon="fas fa-file-pdf") }}

- **Light** mode {{ macros.common.link_to_pdf(pdf.parent_folder ~ '/' ~ pdf.light.filename, message="PDF", icon="fas fa-file-pdf") }}
