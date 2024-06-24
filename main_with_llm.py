import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from src.expert_system import predict_example_fast
from vllm import SamplingParams
from vllm.engine.arg_utils import AsyncEngineArgs
from vllm.engine.async_llm_engine import AsyncLLMEngine
from vllm.usage.usage_lib import UsageContext
from vllm.utils import random_uuid

global_prompt = "Представь, что ты помошник оператора кол центра в крупной строительной компании. Твоя задача найти в тексте размеры предложеных скидок и обстоятельства при которых их предложили. Выпиши размеры и обстоятельства. Будь краток\nText:\n"
sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=100)
engine_args = AsyncEngineArgs(model="./llama3-8b-instruct")
engine = AsyncLLMEngine.from_engine_args(engine_args, usage_context=UsageContext.API_SERVER)

app = FastAPI()


class TextRequest(BaseModel):
    data: str


@app.post("/generate")
async def generate_llm(input: TextRequest):
    prompt = "[INST]" + global_prompt + input.data + "[/INST]"
    request_id = random_uuid()

    results_generator = engine.generate(prompt, sampling_params, request_id)

    final_output = None
    async for request_output in results_generator:
        final_output = request_output

    assert final_output is not None

    text_outputs = [output.text for output in final_output.outputs]
    return {"result": text_outputs}


@app.post("/predict")
async def predict(input: TextRequest):
    result = predict_example_fast(input.data)

    return {"result": result}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
