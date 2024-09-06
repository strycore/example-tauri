#!/usr/bin/env python3
import os
import json
import sys
import datetime

PROJECT_NAME = "example-tauri"


def generate_latest_json(version):
    sig_file = f"src-tauri/target/release/bundle/appimage/{PROJECT_NAME}_{version}_amd64.AppImage.sig"
    if not os.path.exists(sig_file):
        print(f"Signature file for version {version} does not exist")
        sys.exit(1)
    with open(sig_file) as f:
        signature = f.read()
    payload = {
        "version": version,
        "notes": "",
        "pub_date": datetime.datetime.now(tz=datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "platforms": {
            "linux-x86_64": {
                "signature": signature,
                "url": f"https://github.com/strycore/example-tauri/releases/download/{version}/{PROJECT_NAME}_{version}_amd64.AppImage",
            }
        },
    }
    return json.dumps(payload, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gen_latest.py <version>")
        sys.exit(1)
    version = sys.argv[1]
    latest_json = generate_latest_json(version)
    with open("latest.json", "w") as f:
        f.write(latest_json)
