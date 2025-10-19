from flask import Flask, render_template
from Score import read_score

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        scores = read_score()
        return render_template("score.html", scores=scores)
    except Exception as e:
        return render_template("score.html", error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
