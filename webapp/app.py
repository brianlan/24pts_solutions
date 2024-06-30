import os
import json

import requests
from flask import Flask, render_template

from src.solution import get_possible_outputs

app = Flask(__name__)


@app.route("/find_solution/<target>/<cards>", methods=["GET"])
def find_solution(target, cards):
    possible_outputs, hints = get_possible_outputs(tuple(cards), [], target=target)
    return render_template('solution.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
