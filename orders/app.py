from pathlib import Path

from fastapi import FastAPI
import yaml

from orders.api import api

app = FastAPI(
    debug=True, openapi_url='/openapi/orders.json', docs_url='/docs/orders'
)

oas_doc = yaml.safe_load(
    (Path(__file__).parent / '../oas.yml').read_text()
)

app.openapi = lambda: oas_doc

app.include_router(api.app)

