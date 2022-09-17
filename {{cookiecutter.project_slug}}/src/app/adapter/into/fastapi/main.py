import os

from fastapi import Depends, FastAPI

from .dependencies import get_current_user
from .routes import example_route

ENVIRONMENT = os.environ.get("ENVIRONMENT", "")

root_prefix = f"/"

PROTECTED = [Depends(get_current_user)]

app = FastAPI(
    title="{{cookiecutter.project_slug}} Service",
    description="{{cookiecutter.project_slug}} description",
    version="0.0.1",
    root_path=root_prefix,
)
app.include_router(example_route.router, dependencies=PROTECTED)


@app.get("/")
async def version():
    return {"message": "{{cookiecutter.project_slug}} service"}
