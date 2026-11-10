"""CI/CD 데모용 API. /health 가 200이면 이 이미지가 실행 중인 것이다."""

from __future__ import annotations

import os

from fastapi import FastAPI

app = FastAPI(title="JJ Agent Demo", version="0.1.0")

_hits = 0


@app.get("/")
def root() -> dict:
    return {"message": "cicd-test", "health": "/health"}


@app.get("/health")
def health() -> dict:
    global _hits
    _hits += 1
    return {
        "status": "ok",
        "service": "jj-agent-demo",
        "hits": _hits,
        "image_tag": os.getenv("IMAGE_TAG", ""),
    }
