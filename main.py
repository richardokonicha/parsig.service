import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend.api.index:app", host="localhost", port=3000, reload=True)