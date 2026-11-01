"""Expanded redaction patterns for zero-trust. Research only. v0.58."""
import re

PATTERNS = [
    re.compile(r"\b(?:[a-z]{3,8}\s+){11,24}[a-z]{3,8}\b", re.I),  # BIP39-like
    re.compile(r"5[HJK][1-9A-HJ-NP-Za-km-z]{49,50}"),  # WIF
    re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),  # AWS
    re.compile(r"ghp_[A-Za-z0-9]{36}"),  # GitHub PAT
    re.compile(r"sk_live_[A-Za-z0-9]{24,}"),  # Stripe-like
    re.compile(r"xoxb-[A-Za-z0-9-]+"),  # Slack bot
    re.compile(r"\b[A-Za-z0-9]{32,}\b"),  # high entropy fallback (use carefully)
    # Binance, Bybit, OKX style API keys (examples)
    re.compile(r"[A-Za-z0-9]{20,40}"),  # generic long keys - refine in research
]

def redact(text: str) -> str:
    for p in PATTERNS:
        text = p.sub("[REDACTED]", text)
    return text
