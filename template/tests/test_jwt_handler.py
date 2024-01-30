from unittest.mock import patch

import pytest
from jose.exceptions import ExpiredSignatureError, JWTError

from parma_mining.mining_common.jwt_handler import JWTHandler


@pytest.fixture
def valid_jwt():
    return "valid.jwt.token"


@pytest.fixture
def expired_jwt():
    return "expired.jwt.token"


@pytest.fixture
def invalid_jwt():
    return "invalid.jwt.token"


def test_verify_jwt_with_valid_token(valid_jwt):
    with patch("jose.jwt.decode", return_value=True) as mock_decode:
        assert JWTHandler.verify_jwt(valid_jwt) is True
        mock_decode.assert_called_once_with(
            valid_jwt, JWTHandler.SHARED_SECRET_KEY, algorithms=[JWTHandler.ALGORITHM]
        )


def test_verify_jwt_with_expired_token(expired_jwt):
    with patch("jose.jwt.decode", side_effect=ExpiredSignatureError) as mock_decode:
        assert JWTHandler.verify_jwt(expired_jwt) is False
        mock_decode.assert_called_once_with(
            expired_jwt, JWTHandler.SHARED_SECRET_KEY, algorithms=[JWTHandler.ALGORITHM]
        )


def test_verify_jwt_with_invalid_token(invalid_jwt):
    with patch("jose.jwt.decode", side_effect=JWTError) as mock_decode:
        assert JWTHandler.verify_jwt(invalid_jwt) is False
        mock_decode.assert_called_once_with(
            invalid_jwt, JWTHandler.SHARED_SECRET_KEY, algorithms=[JWTHandler.ALGORITHM]
        )
