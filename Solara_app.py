from flask import Flask

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return "Welcome to Solara App!"

if __name__ == "__main__":
    app.run(debug=True, port=8050)
