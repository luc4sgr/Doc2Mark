from src.views.http_types.http_response import HttpResponse
from src.controllers.document_convert_controller import DocumentConvertController

class DocumentConvertView:
    def handle(self, uploaded_file) -> HttpResponse:
        controller = DocumentConvertController()
        result = controller.convert_pdf_to_markdown(uploaded_file)
        return HttpResponse(status_code=200, body=result)
