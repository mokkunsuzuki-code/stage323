#!/usr/bin/env python3
import json
import hashlib
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
    history = json.loads(HISTORY_PATH.read_text(encoding="utf-8"))

    previous_hash = "GENESIS"

    for record in history:
        record["previous_hash"] = previous_hash
        record["current_hash"] = stable_hash(record)
        previous_hash = record["current_hash"]

    HISTORY_PATH.write_text(
        json.dumps(history, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )

    print("[OK] history chain generated")
    for i, record in enumerate(history, start=1):
        print(f"#{i} {record['proof_id']}")
        print(f" previous_hash: {record['previous_hash']}")
        print(f" current_hash : {record['current_hash']}")

if __name__ == "__main__":
    main()
