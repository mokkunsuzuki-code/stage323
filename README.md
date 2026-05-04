# Stage323: YubiKey Signed History

Stage323 adds **issuer assurance** to the Stage322 audit history.

Stage322 created an audit history.
Stage323 signs that history with a GPG/YubiKey-backed issuer key.

## Core Idea

```text
history.json
  ↓
history.json.sig
  ↓
public-key.asc
  ↓
third-party signature verification
Files
docs/proofs/history.json
docs/proofs/history.json.sig
docs/proofs/public-key.asc
verify_signature.sh
Verify
./verify_signature.sh

Or manually:

gpg --import docs/proofs/public-key.asc
gpg --verify docs/proofs/history.json.sig docs/proofs/history.json
What This Proves

Stage322 became audit infrastructure.

Stage323 makes it:

Trusted issuer-backed audit infrastructure.

Security Policy

Private keys, core logic, local secrets, and internal files must not be committed.

Excluded:

core/
keys/
*.pem
*.key
*.p12
.env
.env.*

Only public verification artifacts are published.

License

MIT License

Copyright (c) 2025 Motohiro Suzuki
