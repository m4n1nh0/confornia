import uvicorn

from settings.fastapi_app import fastapi_app

app = fastapi_app()


@app.get("/health")
def health():
    return {"message": "Active"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, server_header=False)
