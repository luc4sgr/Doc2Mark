from cerberus import Validator

def document_convert_validator(request):
    schema = {
        "source": {"type": "string", "required": True, "empty": False}
    }

    v = Validator(schema)
    body = request.json or {}

    if not v.validate(body):
        raise Exception(f"Validation Error: {v.errors}")
