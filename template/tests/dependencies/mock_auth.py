"""Mock implementations of auth function for testing.

This module provides mock versions of authentication function. This mock function is
designed for use in test environments where actual authentication process is not
required.
"""
import logging

from fastapi import Header

logger = logging.getLogger(__name__)


def mock_authenticate(
    authorization: str = Header(None),
) -> str:
    """Authenticate the incoming request using the JWT in the Authorization header.

    Args:
        authorization: The Authorization header containing the JWT.

    Returns:
        Dummy token for testing purposes.
    """
    return "dummytoken"
