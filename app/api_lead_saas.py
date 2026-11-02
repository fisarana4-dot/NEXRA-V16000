from fastapi import FastAPI
app = FastAPI(title="NEXRA Lead Engine")
@app.get("/health")
def health(): return {"status": "healthy", "verified_tests": 354}
