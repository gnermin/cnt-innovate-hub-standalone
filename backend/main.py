from fastapi import FastAPI

from routers import events, workshops, newsletter

app = FastAPI(title="CNT Innovate Hub API")

app.include_router(events.router)
app.include_router(workshops.router)
app.include_router(newsletter.router)


@app.get("/api/health")
async def health():
    return {"status": "ok"}
