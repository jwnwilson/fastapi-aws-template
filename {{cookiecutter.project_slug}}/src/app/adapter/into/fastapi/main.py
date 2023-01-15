import os

from fastapi import Depends, FastAPI

from .api_versions.api_v1.api import api_router_v1

ENVIRONMENT = os.environ.get("ENVIRONMENT", "")

root_prefix = f"/"

app = FastAPI(
    title="{{cookiecutter.project_slug}} Service",
    description="{{cookiecutter.project_slug}} description",
    version="0.0.1",
    root_path=root_prefix,
)
app.include_router(api_router_v1, prefix="/api/v1")


@app.get("/")
async def version():
    return {"message": "{{cookiecutter.project_slug}} service"}
