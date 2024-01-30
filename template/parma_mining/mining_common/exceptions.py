"""Common custom exceptions for mining modules."""
"""TODO: Customize and use them everywhere"""


class BaseError(Exception):
    """Base custom exception."""

    def __init__(self, message=None):
        self.message = message
        super().__init__(message)


class AnalyticsError(BaseError):
    """Custom exception for Analytics related issues."""

    pass


class CrawlingError(BaseError):
    """Custom exception interface for crawling related issues."""

    pass


class ClientError(BaseError):
    """Custom exception interface for client related issues."""

    pass


class CrawlingExternalError(CrawlingError):
    """Custom exception for external crawling related issues."""

    pass


class CrawlingInternalError(CrawlingError):
    """Custom exception for internal crawling related issues."""

    pass


class ClientInvalidBodyError(ClientError):
    """Custom exception for client wrong body input related issues."""

    pass


class ClientUnauthorizedError(ClientError):
    """Custom exception for unauthorized client related issues."""

    pass
