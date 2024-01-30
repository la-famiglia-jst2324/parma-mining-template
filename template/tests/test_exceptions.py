from parma_mining.mining_common.exceptions import BaseError


def test_base_error_initialization():
    message = "Test base error"
    error = BaseError(message)
    assert error.message == message
    assert str(error) == message
