from flask import Flask, render_template, request
from gpt import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

# Define route for home page
@app.route("/get", methods=["GET", "POST"])
def gpt_response():
    userText = request.args.get('msg')
    return str(get_response(userText))

if __name__ == "__main__":
    app.run(debug=False)
    # app.run(debug=True, use_debugger=False, use_reloader=False)