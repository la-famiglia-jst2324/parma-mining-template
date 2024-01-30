from parma_mining.{{module_name}}.helper import collect_errors
from parma_mining.{{module_name}}.model import ErrorInfoModel
from parma_mining.mining_common.exceptions import BaseError


class MockError(BaseError):
    """Mock error class."""

    def __init__(self, message):
        self.message = message


def test_collect_errors():
    company_id = "test_company"
    error_message = "Test error occurred"
    mock_error = MockError(message=error_message)
    errors: dict[str, ErrorInfoModel] = {}

    collect_errors(company_id, errors, mock_error)

    assert company_id in errors
    assert isinstance(errors[company_id], ErrorInfoModel)
    assert errors[company_id].error_type == "MockError"
    assert errors[company_id].error_description == error_message
