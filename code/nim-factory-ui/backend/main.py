from fastapi import FastAPI
from prepare_env import prepare_env
from EnvironmentRequestBody import EnvironmentRequestBody

app = FastAPI()


@app.get("/")
def say_hello():
    return {"message": "Welcome to gradio app backend!"}

@app.post("/prepare-env")
def load_env(env: EnvironmentRequestBody):
    return prepare_env(env)
