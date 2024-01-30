import logging
import os
from importlib import reload
from unittest.mock import patch

import pytest

from parma_mining.{{module_name}}.api import main


@pytest.mark.parametrize(
    "env,expected_level",
    [
        ("prod", logging.INFO),
        ("staging", logging.DEBUG),
        ("local", logging.DEBUG),
        ("other", logging.INFO),
        ("", logging.INFO),
    ],
)
@patch("logging.basicConfig")
def test_logging_level(mock_basic_config, env, expected_level):
    with patch.dict(os.environ, {"DEPLOYMENT_ENV": env}):
        reload(main)
        mock_basic_config.assert_called_with(level=expected_level)
