from flask import Flask, jsonify, render_template, abort
import json
import hashlib
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
PROOF_DIR = BASE_DIR / "proofs"


def load_proof(proof_id):
    path = PROOF_DIR / f"{proof_id}.json"
    if not path.exists():
        abort(404)

    raw = path.read_text(encoding="utf-8")
    proof = json.loads(raw)

    proof_sha256 = hashlib.sha256(
        json.dumps(proof, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()

    proof["proof_sha256"] = proof_sha256
    return proof


@app.route("/")
def home():
    return """
    <h1>Stage320 Proof URL Viewer</h1>
    <p>JSON proof becomes a human-readable public proof page.</p>
    <p><a href="/proof/demo-ai-vulnerability">Open Public Proof URL</a></p>
    <p><a href="/proofs/demo-ai-vulnerability.json">Open JSON Proof</a></p>
    """


@app.route("/proofs/<proof_id>.json")
def proof_json(proof_id):
    proof = load_proof(proof_id)
    return jsonify(proof)


@app.route("/proof/<proof_id>")
def proof_page(proof_id):
    proof = load_proof(proof_id)
    return render_template("proof.html", proof=proof)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3200, debug=True)
