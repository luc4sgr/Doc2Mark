import os
import tempfile
from typing import Dict
from docling.document_converter import DocumentConverter

class DocumentConvertController:
    def convert_pdf_to_markdown(self, uploaded_file) -> Dict:
        # pega a extensão original (ex: ".pdf", ".docx", ".html")
        original_ext = os.path.splitext(uploaded_file.filename)[1]

        # salva o arquivo temporário com a mesma extensão
        with tempfile.NamedTemporaryFile(delete=False, suffix=original_ext) as tmp:
            uploaded_file.save(tmp.name)
            file_path = tmp.name

        converter = DocumentConverter()
        result = converter.convert(file_path)
        markdown = result.document.export_to_markdown()

        return {
            "data": {
                "type": "Markdown Document",
                "filename": uploaded_file.filename,
                "markdown": markdown
            }
        }
