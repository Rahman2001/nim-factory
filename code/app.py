import os
from flask import Flask

proxy_prefix = os.environ.get("PROXY_PREFIX")

app = Flask(__name__)
# app.config['APPLICATION_ROOT'] = proxy_prefix

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
app.run()

# demo.launch(server_name="0.0.0.0", server_port=8080, root_path=proxy_prefix)