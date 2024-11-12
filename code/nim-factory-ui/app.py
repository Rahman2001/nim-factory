import gradio as gr

from backend.Model import Model
from backend.models import models
from backend.Environment import Environment
import requests


BASE_URL = "http://127.0.0.1:8000"
HEADERS = {'Content-Type': 'application/json'}
model = Model()
env = Environment()


def btn_click(button: gr.Button):
    model.family = button
    model_family = models[button]
    return gr.Dropdown(choices=list(model_family.keys()), interactive=True)


def selected_version(dropdown: gr.Dropdown):
    model.version = dropdown
    model_names = models[model.family][dropdown]
    return gr.Dropdown(choices=model_names, interactive=True)


def hf_textbox_save(hf: gr.Textbox):
    if hf.value != "" or hf.value is not None:
        if env.huggingface is None:
            env.huggingface = {"username": "", "token": ""}
        else:
            if hf.label == "Username":
                env.huggingface["username"] = hf.value
            else:
                env.huggingface["token"] = hf.value
    else:
        env.huggingface = None


def load_env():
    url = BASE_URL + "/" + "prepare-env"
    env.model = model
    response = requests.post(url, json=env.get_json(), headers=HEADERS).json()
    print(response)
    if response["has_tensorrt_llm"] == 0 and response["has_model"] == 0:
        return gr.Markdown("TensorRT-LLM", elem_id="tensor_mark_success")
    else:
        return gr.Markdown("TensorRT-LLM", elem_id="tensor_mark_fail")


def chat_function(message, history):
    return message


def engine_btn_click(button: gr.Button):
    return gr.Button("Stop Engine") if button == "Run Engine" else gr.Button("Run Engine")


with gr.Blocks(css_paths="nim_ui.css") as demo:
    with gr.Row():
        gr.Markdown("NVIDIA NIM Factory")
        prep_btn = gr.Button("Prepare Environment", elem_id="prep_button")
        tensor_mark = gr.Markdown("TensorRT-LLM", elem_id="tensor_markdown")

    with gr.Tabs():
        with gr.Tab("Environment"):
            with gr.Row():

                with gr.Column():
                    gr.Markdown("Which model family would you like to select?")
                    with gr.Column():
                        model_fam = []
                        with gr.Row():
                            for fam_version in models:
                                model_fam.append(gr.Button(fam_version))
                with gr.Column():
                    gr.Markdown("Which model do you want?")
                    model_ver_drp = gr.Dropdown(interactive=True, label="Model Family Versions")
                    model_names_drp = gr.Dropdown(interactive=True, label="Model Types")

                with gr.Column():
                    gr.Markdown("Hugging Face")
                    hf_username = gr.Textbox(label="Username", placeholder="Write your Hugging Face username", type="email")
                    hf_token = gr.Textbox(label="Token", placeholder="Write your API token", type="password")
                    hf_username.change(fn=hf_textbox_save, inputs=hf_username)
                    hf_token.change(fn=hf_textbox_save, inputs=hf_token)

                for version in model_fam:
                    version.click(fn=btn_click, inputs=version, outputs=model_ver_drp)

                model_ver_drp.change(fn=selected_version, inputs=model_ver_drp, outputs=model_names_drp)
                prep_btn.click(fn=load_env, outputs=tensor_mark)

        with gr.Tab("TensorRT-LLM", elem_id="tensor_tab"):

            with gr.Tab("Quantization", elem_id="quantization_tab"):
                with gr.Row():
                    with gr.Column(scale=3):
                        gr.Textbox(label="Quantization Window", lines=25, elem_id="quantization_window")

                    with gr.Column(elem_id="quantization_setting"):
                        gr.Dropdown(label="quantization format", choices=['fp8', 'int4_awq', 'w4a8_awq', 'int8_sq'],
                                    interactive=True)
                        gr.Number(label="batch size", interactive=True, value=1, minimum=1, info="Default is 1")
                        gr.Number(label="tensor parallel size", interactive=True, value=1, minimum=1,
                                  info="Default is 1")
                        gr.Number(label="pipeline parallel size", interactive=True, value=1, minimum=1,
                                  info="Default is 1")
                        gr.Number(label="calibration size", value=512, interactive=True,
                                  info="Size should be divisible by 8. (Default is 512)", step=8, minimum=8, maximum=512)
                        gr.Dropdown(label="kv cache dtype", choices=[None, 'int8', 'fp8'], interactive=True, value=None,
                                    info="If None, kv cache will be as dtype of the model")
                        gr.Dropdown(label="AWQ algorithm specific block size when quantizing weights", choices=[64, 128],
                                    value=64, interactive=True, info="Default is 64")
                        gr.Button("Start Quantization")

            with gr.Tab("Build Engine", elem_id="build_tab"):
                with gr.Row():
                    with gr.Column(scale=3):
                        gr.Textbox(label="Build Window", lines=25, elem_id="build_window")

                    with gr.Column(elem_id="build_setting"):
                        gr.Number(label="workers", minimum=1, value=1, interactive=True,
                                  info="The number of workers for building in parallel. (Default is 1)")
                        gr.Dropdown(label="memory monitoring", choices=[True, False], value=False, interactive=True,
                                    info="Enable memory monitoring during Engine build. (Default is False)")
                        gr.Number(label="max input length", minimum=1,
                                  info="should not be more than {max_position_embeddings} in config.json of the base model")
                        gr.Dropdown(label="model directory", interactive=True,
                                    info="only downloaded and/or quantized models listed")
                        gr.Button("Start Engine Build")

            with gr.Tab("Run Engine", elem_id="run_tab"):
                with gr.Row():
                    with gr.Column(scale=2, elem_id="chat_col"):
                        gr.ChatInterface(fn=chat_function, multimodal=False, type="messages", fill_height=True)

                    with gr.Column(elem_id="run_setting"):
                        gr.Dropdown(label="engine directory", interactive=True,
                                    info="only available engines are listed")
                        gr.Number(label="max output length", minimum=1, value=1)
                        gr.Dropdown(label="tokenizer directory (base model directory)", interactive=True,
                                    info="(selected based on engine)")
                        engine_btn = gr.Button("Run Engine")
                        engine_btn.click(fn=engine_btn_click, inputs=engine_btn, outputs=engine_btn)

demo.launch()