"""
from __future__ import -> annotations is a Python feature import. 
It tells Python to treat type hints (annotations) as strings instead of 
evaluating them immediately.

| Field           | Meaning                       |
| --------------- | ----------------------------- |
| `%(asctime)s`   | Time of log                   |
| `%(name)s`      | Module name                   |
| `%(levelname)s` | Log type (INFO, DEBUG, ERROR) |
| `%(message)s`   | Actual log message            |

Since level is DEBUG, all logs will be captured.
"""


from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path


def get_logger(name: str = "us_visa") -> logging.Logger:
    """
    Create and configure a project logger.
    """

    # Project root (current working directory)
    project_root = Path.cwd()

    # Logs directory
    log_dir = project_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    # Log file with timestamp
    log_file = log_dir / f"{datetime.now():%m_%d_%Y_%H_%M_%S}.log"

    # Configure logging
    logging.basicConfig(
        filename=log_file,
        format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )

    return logging.getLogger(name)


# Create global logger
logging = get_logger()

