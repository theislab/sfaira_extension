# -*- coding: utf-8 -*-
"""An extension for sfaira enabling private data, celltypes, models, topologies and estimators."""

from ._version import get_versions

__version__ = get_versions()['version']
__maintainer__ = ', '.join([
    "Leander Dony",
    "David S. Fischer"
])
__author__ = ', '.join([
    "Leander Dony",
    "David S. Fischer"
])
__email__ = ', '.join([
    "leander.dony@helmholtz-muenchen.de",
    "david.fischer@helmholtz-muenchen.de"
])

import sfaira_extension.data
import sfaira_extension.versions
