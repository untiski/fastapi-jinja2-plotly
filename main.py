from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from plotly import graph_objects as go
import uvicorn

from api import router


app = FastAPI()

templates = Jinja2Templates("templates")

app.include_router(router=router, prefix="/api")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # Simple sample data
    data1 = {
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 4, 8, 16]
    }
    data2 = {
        "x": [1, 2, 3, 4, 5],
        "y": [16, 8, 4, 2, 1]
    }
    # generate a graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(**data1))
    fig.add_trace(go.Scatter(**data2))
    # Send a graph element via TemplateResponse
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "plotlyGraph1": fig.to_html(
                full_html=False,
                include_plotlyjs=False,
                div_id="plotlyGraph1",
            )
        },
    )


if __name__ == '__main__':
    uvicorn.run(app)
