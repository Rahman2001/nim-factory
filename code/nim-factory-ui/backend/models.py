llama = {
    "Llama-2": ["7b", "7b-hf", "7b-chat", "7b-chat-hf", "13b", "13b-hf", "13b-chat", "13b-chat-hf",
                "70b", "70b-hf", "70b-chat", "70b-chat-hf"],
    "Meta-Llama-3": ["8B", "8B-Instruct", "70B", "70B-Instruct"],
    "Llama-3.1": ["8B", "8B-Instruct", "70B", "70B-Instruct", "405B", "405B-Instruct"],
    "CodeLlama": ["7b-hf", "34b-Instruct-hf", "7b-Instruct-hf", "13b-hf", "34b-hf", "13b-Instruct-hf"]
}
phi = {
    "phi2": [None],
    "Phi-3": ["mini-4k-instruct", "mini-128k-instruct", "small-8k-instruct", "small-128k-instruct",
              "medium-8k-instruct", "medium-128k-instruct"],
    "Phi-3.5": ["mini-instruct", "MoE-instruct"]
}
mixtral = {
    "8x": ["7B", "22B"]
}
nemotron = {
    "nemotron-3": ["8B-base-4k", "8B-chat-4k-sft"],
    "nemotron-4": ["340B-Instruct", "340B-Base", "340-Reward"]
}
arctic = {
    "snowflake-arctic": ["instruct"]
}
baichuan = {
    "Baichuan": ["7B", "13B-Base", "13B-Chat"],
    "Baichuan2": ["7B-Base", "7B-Chat", "13B-Chat", "13B-Base"]
}
bloom = {
    "bloom": ["560m"]
}
glm = {
    "chatglm": ["6b"],
    "chatglm2": ["6b", "6b-32k"],
    "chatglm3": ["6b", "6b-base", "6b-32k"]
}
dbrx = {
    "dbrx": ["base", "instruct"]
}
falcon = {
    "falcon": ["7b", "7b-instruct", "11B", "40b", "40b-instruct", "180B-chat"]
}
gemma = {
    "gemma": ["2b", "7b"],
    "gemma-2": ["2b", "9b", "27b"]
}
gpt = {
    "gpt2": [None, "medium", "large", "xl"]
}

models = {
    "Llama": llama,
    "Phi": phi,
    "Mixtral": mixtral,
    "Nemotron": nemotron,
    "Arctic": arctic,
    "Baichuan": baichuan,
    "Bloom": bloom,
    "ChatGLM": glm,
    "DBRX": dbrx,
    "Falcon": falcon,
    "Gemma": gemma,
    "GPT": gpt
}
repo = {
    "Llama": "meta-llama",
    "Phi": "microsoft",
    "Mixtral": "mistral",
    "Nemotron": "nvidia",
    "Arctic": "Snowflake",
    "Baichuan": "baichuan-inc",
    "Bloom": "bigscience",
    "ChatGLM": "THUDM",
    "Databricks": "databricks",
    "Falcon": "tiiuae",
    "Gemma": "google",
    "GPT": "openai-community"
}