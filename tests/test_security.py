from crypto_intel.security.redact import redact

def test_redact_bip39():
    text = "abandon ability able about above absent absorb abstract absurd abuse access accident"
    assert "[REDACTED]" in redact(text)
