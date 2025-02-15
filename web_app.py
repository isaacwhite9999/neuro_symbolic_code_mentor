from flask import Flask, render_template, request
from neuro_symbolic_code_mentor.mentor import CodeMentor

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    suggestions = []
    code_input = ""
    if request.method == "POST":
        code_input = request.form.get("code_input", "")
        # Enable neural suggestions in the web interface by default
        mentor = CodeMentor(use_neural=True)
        suggestions = mentor.analyze(code_input)
    return render_template("index.html", suggestions=suggestions, code_input=code_input)

if __name__ == "__main__":
    app.run(debug=True)
