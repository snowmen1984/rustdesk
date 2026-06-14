#!/usr/bin/env python3
"""
Patch RustDesk OSS default self-host server before CI builds.

This script edits libs/hbb_common/src/config.rs after submodules are checked out.
It keeps the server public key out of the repository: pass it through GitHub
Actions input or the RUSTDESK_RS_PUB_KEY repository secret.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
