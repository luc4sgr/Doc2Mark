from flask import Blueprint, request, jsonify
from werkzeug.datastructures import FileStorage
from src.views.document_convert_view import DocumentConvertView
from src.errors.error_handler import handle_errors

document_routes_bp = Blueprint('document_routes', __name__)

@document_routes_bp.route("/convert_document", methods=["POST"])
def convert_document():
    try:
        print('chegou')
        uploaded_file = request.files.get("source")
        if not uploaded_file or not isinstance(uploaded_file, FileStorage):
            raise Exception("File 'source' is required.")

        view = DocumentConvertView()
        response = view.handle(uploaded_file)
    except Exception as e:
        response = handle_errors(e)

    return jsonify(response.body), response.status_code
