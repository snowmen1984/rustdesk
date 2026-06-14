#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

server = os.getenv('CUSTOM_ID_SERVER', 'rd.sgohome.us').strip()
key = os.getenv('CUSTOM_RS_PUB_KEY', '').strip()
config = Path('libs/hbb_common/src/config.rs')

if not server:
    sys.exit('[ERROR] CUSTOM_ID_SERVER is empty')
if not key:
    sys.exit('[ERROR] CUSTOM_RS_PUB_KEY is empty. Add repository secret RUSTDESK_RS_PUB_KEY or enter public_key when running the workflow.')
if not config.exists():
    sys.exit('[ERROR] libs/hbb_common/src/config.rs not found. Check submodules.')

text = config.read_text(encoding='utf-8')
old = text
text = re.sub(r'pub const RENDEZVOUS_SERVERS:\s*&\[\&str\]\s*=\s*&\[[^\]]*\];', f'pub const RENDEZVOUS_SERVERS: &[&str] = &["{server}"];', text)
text = re.sub(r'pub const RS_PUB_KEY:\s*&str\s*=\s*"[^"]*";', f'pub const RS_PUB_KEY: &str = "{key}";', text)
if text == old:
    sys.exit('[ERROR] No defaults were patched. Patterns may have changed in hbb_common/src/config.rs')
config.write_text(text, encoding='utf-8')
print(f'[OK] RustDesk default server patched: {server}')
print(f'[OK] Public key length: {len(key)}')
