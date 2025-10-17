from flask import Flask, render_template
from Utils import SCORES_FILE_NAME
import os

app = Flask(__name__)

TEST_MODE = os.environ.get("TEST_MODE", "False") == "True"

def read_score_from_file(scores_file):
    print("Reading file:", os.path.abspath(SCORES_FILE_NAME))
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            line = file.readline().strip()
            print("Raw content:", repr(line))
            if line == "":
                return 0
            score = int(line)
            return score
    except FileNotFoundError:
        return 0

@app.route("/")
def score_server():
    try:
        score = read_score_from_file(SCORES_FILE_NAME)
        return render_template("score.html", score=score)
    except Exception as e:
        return render_template("score.html", error=str(e))

if __name__ == "__main__" or TEST_MODE:
    # Run Flask server directly
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)


