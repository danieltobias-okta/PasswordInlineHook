from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/password", methods = ['POST'])
def password():
    print(request.json)
    response = request.json
    #your logic
    return jsonify(commands = [{"type":"com.okta.action.update", "value" : { "credential":"VERIFIED"}}])

if __name__ == "__main__":
    app.run(debug=True)
