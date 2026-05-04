#!/bin/bash
set -e

echo "Importing public key..."
gpg --import docs/proofs/public-key.asc

echo "Verifying signed history..."
gpg --verify docs/proofs/history.json.sig docs/proofs/history.json

echo "OK: history.json is signed by the trusted issuer key."
