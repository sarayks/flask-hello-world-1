import os
from flask import Flask, send_file, safe_join, abort

app = Flask(__name__)

@app.route("/")
def index():
    try:
        return send_file("src/index.html")
    except FileNotFoundError:
        abort(404)

@app.route("/favicon.png")
def favicon():
    path = safe_join("src/static/icons", "favicon.png")
    try:
        return send_file(path, mimetype="image/png")
    except FileNotFoundError:
        abort(404)

def main():
    port = int(os.environ.get("PORT", 80))
    # host="0.0.0.0" permite acesso externo e facilita deploy
    app.run(host="0.0.0.0", port=port, debug=True)

if __name__ == "__main__":
    main()
