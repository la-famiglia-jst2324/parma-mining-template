from unittest.mock import patch

import pytest
from fastapi import HTTPException, status

from parma_mining.{{module_name}}.api.dependencies.auth import authenticate


def test_authenticate_missing_header():
    with pytest.raises(HTTPException) as exc:
        authenticate("")
    assert exc.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert "Invalid shared token or expired token" in str(exc.value.detail)


def test_authenticate_invalid_token():
    with patch(
        "parma_mining.mining_common.jwt_handler.JWTHandler.verify_jwt",
        return_value=False,
    ):
        with pytest.raises(HTTPException) as exc:
            authenticate("Bearer invalid_token")
    assert exc.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert "Invalid shared token or expired token" in str(exc.value.detail)


@pytest.mark.parametrize(
    "token, expected_return",
    [
        ("Bearer valid_token", "valid_token"),
        ("valid_token", "valid_token"),
        ("Bearer xya", "xya"),
        ("xya", "xya"),
    ],
)
def test_authenticate_valid_token(token, expected_return):
    with patch(
        "parma_mining.mining_common.jwt_handler.JWTHandler.verify_jwt",
        return_value=True,
    ):
        assert authenticate(token) == expected_return
