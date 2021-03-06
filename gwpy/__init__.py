# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2013)
#
# This file is part of GWpy.
#
# GWpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GWpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GWpy.  If not, see <http://www.gnu.org/licenses/>.

"""A python package for gravitational-wave astrophysics

GWpy is a collaboration-driven `Python <http://www.python.org>`_ package
providing tools for studying data from ground-based gravitational-wave
detectors.

GWpy provides a user-friendly, intuitive interface to the common time-domain
and frequency-domain data produced by the `LIGO <http://www.ligo.org>`_ and
`Virgo <http://www.ego-gw.it>`_ instruments and their analysis,
with easy-to-follow tutorials at each step.
"""

import warnings

# filter out some annoying, but harmless warnings
warnings.filterwarnings("ignore", "Module (.*) was already import from")
warnings.filterwarnings("ignore", "The oldnumeric module",
                        DeprecationWarning)

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
__credits__ = "The LIGO Scientific Collaboration and the Virgo Collaboration"

# get version information
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
