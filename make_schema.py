import json
d = {
"@context": "https://schema.org",
  "@type": "SoftwareApplication",
"description": "AI-driven decision intelligence system.",
  "applicationCategory": "BusinessApplication"
}

with open("schema.json", "w") as f:
    json.dump(d, f, indent=2)
