"""This module contains authentication and authorization dependencies.

Specifically designed for sourcing modules in the FastAPI application, it includes
functions to authenticate requests using JWTs and to authorize these requests by
validating the JWTs against defined secret keys. The module ensures that only valid and
authorized sourcing modules can access certain endpoints.
"""
import logging

from fastapi import HTTPException, Header, status

from parma_mining.mining_common.jwt_handler import JWTHandler

logger = logging.getLogger(__name__)


def authenticate(
    authorization: str = Header(None),
) -> str:
    """Authenticate the incoming request using the JWT in the Authorization header.

    Args:
        authorization: The Authorization header containing the JWT.

    Returns:
        Extracted token from the Authorization header.
        (Whenever a request is needed to be made to the Analytics Backend,
        This token can be used to authenticate the request.)

    Raises:
        HTTPException: If the JWT is invalid.
        HTTPException: If the JWT is expired.
        HTTPException: If the Authorization header is missing.
    """
    if authorization is None:
        logger.error("Authorization header is required!")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header is required!",
        )

    token = (
        authorization.split(" ")[1]
        if authorization.startswith("Bearer ")
        else authorization
    )
    is_verified: bool = JWTHandler.verify_jwt(token)
    if is_verified is False:
        logger.error("Invalid shared token or expired token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid shared token or expired token",
        )

    return token
