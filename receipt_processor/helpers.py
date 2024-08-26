import os
from typing import List

from flask import current_app


def documentation_file(*paths: str) -> str:
    """Get the swagger documentation path from path
    relative to the documentation folder.
    
    Args:
        paths (str): the path to documentation file, separated

    Returns:
        str: the joined path
    """
    with current_app.app_context():
        path = os.path.join(current_app.config['DOCUMENTATION_FOLDER'], *paths)
        return path
