from fastapi import FastAPI, Response, status

app = FastAPI(
    title="quizAPI",
    version="0.1.0",
    docs_url="/"
)


@app.head(path="/")
async def ping_api():
    return Response(status_code=status.HTTP_204_NO_CONTENT)
