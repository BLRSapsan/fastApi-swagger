import uvicorn

from create_fastapi_app import create_app

app = create_app(create_custom_static_urls=True)


@app.get("/")
def root():
    return "Hello, World"


if __name__ == "__main__":
    uvicorn.run(app)
