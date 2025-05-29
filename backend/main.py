import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="app:app", log_level="debug", host="0.0.0.0", port=8998, workers=1)
