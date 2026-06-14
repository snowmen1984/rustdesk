#!/usr/bin/env python3
import argparse
import os
import re
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description='Patch RustDesk default self-host server in hbb_common config.rs')
parser.add_argument('--server', default=os.environ.get('CUSTOM_ID_SERVER', 'rd.sgohome.us'))
parser.add_argument('--public-key', default=os.environ.get('CUSTOM_RS_PUB