import pytest
from flask import Request
from types import SimpleNamespace
from src.validators.document_convert_validator import document_convert_validator

class FakeRequest:
    def __init__(self, json_data):
        self.json = json_data

def test_validator_accepts_valid_data():
    request = FakeRequest({"source": "file.pdf"})
    # não deve lançar erro
    document_convert_validator(request)

def test_validator_rejects_missing_source():
    request = FakeRequest({})
    with pytest.raises(Exception) as exc_info:
        document_convert_validator(request)
    assert "source" in str(exc_info.value)

def test_validator_rejects_empty_source():
    request = FakeRequest({"source": ""})
    with pytest.raises(Exception) as exc_info:
        document_convert_validator(request)
    assert "source" in str(exc_info.value)
