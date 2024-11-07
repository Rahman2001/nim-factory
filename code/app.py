import gradio as gr
import os

script = '''
function wrap() {
    function test() {
        document.getElementById('demo').innerHTML = "Hello"
    }
}
'''
    
with open("index.html") as f:
    lines = f.readlines()
    
with gr.Blocks() as demo:   
    input_mic = gr.HTML(lines)
    out_text  = gr.Textbox()
    demo.load(_js = script)

if __name__ == "__main__":   
    proxy_prefix = os.environ.get("PROXY_PREFIX")
    demo.launch(server_name="0.0.0.0", server_port=8080, root_path=proxy_prefix)