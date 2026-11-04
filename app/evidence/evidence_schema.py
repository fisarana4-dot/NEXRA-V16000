from datetime import datetime, timezone
from typing import Any, Dict, Optional, Union
import uuid
import hashlib
import json
from pydantic import BaseModel, Field, field_validator

class EvidenceContract(BaseModel):
    """
    A typed, schema-first, domain-agnostic Evidence Contract.
    Ensures strict validation, traceability, and cryptographic integrity
    for any evidence ingested into the system.
    """
    evidence_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="A unique identifier for this evidence record (UUID v4 by default)."
    )
    source: str = Field(
        ...,
        min_length=1,
        description="The origin or source system of the evidence (e.g., 'TradingView', 'Binance API')."
    )
    url: Optional[str] = Field(
        default=None,
        description="An optional URL link associated with the evidence."
    )
    title: str = Field(
        ...,
        min_length=1,
        description="A concise title or summary of the evidence."
    )
    content: Union[str, Dict[str, Any], Any] = Field(
        ...,
        description="The primary body or payload of the evidence. Can be text, structured data (JSON/dict), etc."
    )
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="The UTC timestamp when this evidence was captured or recorded."
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Arbitrary domain-specific metadata associated with the evidence."
    )
    evidence_type: str = Field(
        default="general",
        min_length=1,
        description="The classification type of the evidence (e.g., 'market_feed', 'ledger_entry')."
    )
    evidence_hash: str = Field(
        default="",
        description="A SHA-256 cryptographic hash of the evidence content/payload to guarantee integrity."
    )

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if not v:
            return None
        # Check basic URL structure (must start with http:// or https://)
        if not (v.startswith("http://") or v.startswith("https://")):
            raise ValueError("URL must start with http:// or https://")
        return v

    @field_validator("source", "title", "evidence_type")
    @classmethod
    def strip_whitespace(cls, v: str) -> str:
        if not isinstance(v, str):
            raise TypeError("Value must be a string")
        stripped = v.strip()
        if not stripped:
            raise ValueError("Value cannot be empty or just whitespace")
        return stripped

    def model_post_init(self, __context: Any) -> None:
        """
        Calculates and updates the cryptographic hash of the content 
        if evidence_hash is not explicitly set.
        """
        super().model_post_init(__context)
        if not self.evidence_hash:
            self.evidence_hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Generates a SHA-256 hash representing the complete integrity-critical payload 
        including: source, title, timestamp (ISO format), and content.
        """
        # Serialize the content to a stable JSON representation
        if isinstance(self.content, dict):
            serialized_content = json.dumps(self.content, sort_keys=True)
        elif isinstance(self.content, bytes):
            serialized_content = self.content.hex()
        else:
            serialized_content = str(self.content)

        # Build a raw message combining integrity-critical fields
        hash_payload = {
            "source": self.source,
            "title": self.title,
            "timestamp": self.timestamp.isoformat(),
            "content": serialized_content,
        }
        
        payload_bytes = json.dumps(hash_payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(payload_bytes).hexdigest()

    def verify_integrity(self) -> bool:
        """
        Verifies if the current state of the evidence matches the stored evidence_hash.
        """
        return self.evidence_hash == self.calculate_hash()
