# Copy and verify the entry artwork unchanged in the harness output directory.
# Local run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#   or: python3 main.py --output out
import argparse
import hashlib
import os
import shutil
import time
from pathlib import Path

start_time = time.monotonic()

parser = argparse.ArgumentParser(description="Copy and verify the entry artwork.")
parser.add_argument(
    "--output",
    default=None,
    help="Output directory for entry.png (default: $MAKEFUN_OUTPUT_DIR or /output)",
)
parser.add_argument(
    "--quiet",
    action="store_true",
    help="Only print the SHA-256 hash, without the summary lines.",
)
args = parser.parse_args()

source = Path(__file__).resolve().with_name("entry.png")
if not source.is_file():
    raise FileNotFoundError(f"Entry image is missing: {source}")
if source.stat().st_size > 1_048_576:
    raise ValueError(f"Entry image exceeds 1,048,576 bytes: {source.stat().st_size}")

output_dir = Path(args.output or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
destination = output_dir / "entry.png"
shutil.copyfile(source, destination)
source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
destination_sha = hashlib.sha256(destination.read_bytes()).hexdigest()
if source_sha != destination_sha:
    raise IOError(
        f"Copied entry image verification failed: {destination} "
        f"(source sha256 {source_sha}, output sha256 {destination_sha})"
    )
if args.quiet:
    print(destination_sha)
else:
    elapsed = time.monotonic() - start_time
    print(f"Copied and verified {destination.stat().st_size} bytes at {destination}")
    print(f"SHA-256 verified: {destination_sha}")
    print(f"done in {elapsed:.2f}s")
