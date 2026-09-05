import hashlib
import hmac

import pytest
from fastapi import HTTPException

from app.api.v1.endpoints import tradingview
from app.core.config import settings


def test_webhook_signature_rejects_missing_secret(monkeypatch):
    monkeypatch.setattr(settings, "TRADINGVIEW_WEBHOOK_SECRET", None)

    with pytest.raises(HTTPException) as error:
        tradingview.verify_webhook_signature(b'{"signal":"BUY"}', "anything")

    assert error.value.status_code == 401


def test_webhook_signature_accepts_valid_hmac(monkeypatch):
    secret = "test-webhook-secret"
    body = b'{"signal":"BUY"}'
    monkeypatch.setattr(settings, "TRADINGVIEW_WEBHOOK_SECRET", secret)
    signature = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()

    tradingview.verify_webhook_signature(body, signature)


def test_webhook_signature_rejects_invalid_hmac(monkeypatch):
    monkeypatch.setattr(settings, "TRADINGVIEW_WEBHOOK_SECRET", "test-webhook-secret")

    with pytest.raises(HTTPException) as error:
        tradingview.verify_webhook_signature(b'{"signal":"BUY"}', "invalid")

    assert error.value.status_code == 401
