from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Mirai Mock API"
    }

@app.post("/external/dopa/idcard/laser")
async def dopa():
    return {
        "code": "0",
        "description": "สถานะปกติ"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
