from flask import Flask
from flask import render_template
from flask import make_response
from flask import request
from flask import jsonify
import json
import numpy

app = Flask(__name__)

@app.route("/")
def hello():
    """
    最简单的例子
    :return:
    """
    return render_template('index.html')

@app.route("/1", methods = ['Post'])
def find_path():
    """
    调取对应的算法查询路径
    :return:
    """
    params = json.loads(request.data.decode("utf-8"))
    print(params)
    result = {"data":[]}
    return make_response(jsonify(result))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)