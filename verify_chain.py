#!/usr/bin/env python3
import json
import hashlib
import sys
from pathlib import Path

HISTORY_PATH = Path("docs/proof/history.json")

def stable_hash(record):
    data = {
        "proof_id": record["proof_id"],
        "timestamp": record["timestamp"],
        "previous_hash": record["previous_hash"],
    }
    raw = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

def main():
    if not HISTORY_PATH.exists():
        print("[ERROR] history.json not found")
        sys.exit(1)

    history = json.loads(HISTORY_PATH.read_text(encoding="utf-8"))

    if not history:
        print("[ERROR] history is empty")
        sys.exit(1)

    expected_previous = "GENESIS"

    for index, record in enumerate(history, start=1):
        required = ["proof_id", "timestamp", "previous_hash", "current_hash"]
        for key in required:
            if key not in record:
                print(f"[ERROR] missing key '{key}' at record #{index}")
                sys.exit(1)

        if record["previous_hash"] != expected_previous:
            print(f"[ERROR] chain broken at record #{index}")
            print(f" expected previous_hash: {expected_previous}")
            print(f" actual previous_hash  : {record['previous_hash']}")
            sys.exit(1)

        recalculated = stable_hash(record)

        if record["current_hash"] != recalculated:
            print(f"[ERROR] hash mismatch at record #{index}")
            print(f" expected current_hash: {recalculated}")
            print(f" actual current_hash  : {record['current_hash']}")
            sys.exit(1)

        expected_previous = record["current_hash"]

    print("[OK] Proof history chain is valid")
    print(f"[OK] records verified: {len(history)}")
    print(f"[OK] latest hash: {expected_previous}")

if __name__ == "__main__":
    main()
