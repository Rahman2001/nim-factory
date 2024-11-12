from fastapi import FastAPI
from prepare_env import prepare_env
from EnvironmentRequestBody import EnvironmentRequestBody

app = FastAPI()


@app.post("/prepare-env")
def load_env(env: EnvironmentRequestBody):
    return prepare_env(env)
