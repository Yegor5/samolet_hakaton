import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from expert_system import predict_example_fast


app = FastAPI()


class TextRequest(BaseModel):
    data: str


@app.post("/predict")
async def predict(input: TextRequest):

    result = predict_example_fast(input.data)

    return {"result": result}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
