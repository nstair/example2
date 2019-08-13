"""
example2
A example project with os x, linux, and windows builds
"""

# Add imports here
from .example2 import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
