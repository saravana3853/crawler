import json
import crawl
import db

from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/crawl', methods=['GET'])
def crawler():
  crawl.crawl_web()
  return jsonify({"response":"success"})


@app.route('/search', methods=['POST'])
def search():
 data = json.loads(request.data)
 result=db.search(data['query'])
 print(result)
 return jsonify(result),200


if __name__ == '__main__':
   app.run(port=5000) 
