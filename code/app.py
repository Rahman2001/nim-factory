import os
from flask import Flask
from flask import render_template

proxy_prefix = os.environ.get("PROXY_PREFIX")

app = Flask(__name__)
# app.config['APPLICATION_ROOT'] = proxy_prefix

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

# demo.launch(server_name="0.0.0.0", server_port=8080, root_path=proxy_prefix)