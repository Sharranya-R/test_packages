# Ultralytics YOLO 🚀, AGPL-3.0 license

__version__ = "8.2.42"

import os

# Set ENV Variables (place before imports)
os.environ["OMP_NUM_THREADS"] = "1"  # reduce CPU utilization during training

from test_packages.data.explorer.explorer import Explorer
from test_packages.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOWorld
from test_packages.utils import ASSETS, SETTINGS
from test_packages.utils.checks import check_yolo as checks
from test_packages.utils.downloads import download

settings = SETTINGS
__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOWorld",
    "NAS",
    "SAM",
    "FastSAM",
    "RTDETR",
    "checks",
    "download",
    "settings",
    "Explorer",
)
