from flask import Flask
from flask import request, jsonify, Response

from services.messageService import MessageService

app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()

@app.route('/v1/ds/message', methods=['POST'])
def handle_message() :
    try:
        message = request.json.get('message')
        result = messageService.process_message(message)
        return Response(
            result.json(),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=['GET'])
def handle_get():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)