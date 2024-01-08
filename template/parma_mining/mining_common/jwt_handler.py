"""Module for JWT (JSON Web Token) handling.

This module contains the JWTHandler class which is designed to verify JWTs. The
verification process supports shared secret keys to enable authentication.
"""
import logging
import os

from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError

logger = logging.getLogger(__name__)


class JWTHandler:
    """A handler for verifying JWTs."""

    SHARED_SECRET_KEY: str = str(os.getenv("PARMA_SHARED_SECRET_KEY") or "PARMA_SHARED_SECRET_KEY")
    ALGORITHM: str = "HS256"

    @staticmethod
    def verify_jwt(token: str) -> bool:
        """Verify a JWT using the shared secret key.

        Args:
            token (str): The JWT token to verify.

        Returns:
            bool: True if the verification is successful, False otherwise.
        """
        try:
            jwt.decode(
                token, JWTHandler.SHARED_SECRET_KEY, algorithms=[JWTHandler.ALGORITHM]
            )
            return True
        except ExpiredSignatureError:
            logger.error("JWT has expired.")
        except JWTError:
            logger.error("Invalid JWT, unable to decode.")

        return False
