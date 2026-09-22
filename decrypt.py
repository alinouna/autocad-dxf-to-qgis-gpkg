#!/usr/bin/env python3
"""Decrypt this repository's archive.  pip install pyzipper"""
import getpass, pathlib, sys, zipfile

try:
    import pyzipper
except ImportError:
    sys.exit("Run: pip install pyzipper")

here = pathlib.Path(__file__).resolve().parent
arc = next(iter(sorted(here.glob("*.zip"))), None)
if arc is None:
    sys.exit("No archive found next to decrypt.py")

pw = (sys.argv[1] if len(sys.argv) > 1 else getpass.getpass("Password: ")).encode()
target = here / "src"
with pyzipper.AESZipFile(arc) as z:
    z.setpassword(pw)
    bad = z.testzip()
    if bad:
        sys.exit(f"Corrupt entry: {bad}")
    z.extractall(target)
print(f"Decrypted to {target}")
print(f"Verify from {here} with:  sha256sum -c MANIFEST.sha256")
