import os
from flask import Flask
from flask import request, jsonify, Response
from kafka import KafkaProducer
import json
from dotenv import load_dotenv

from services.messageService import MessageService


load_dotenv()
app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()

server = os.getenv("SERVER_ADDRESS")
producer = KafkaProducer(
        bootstrap_servers = [f'{server}:9092'],
        value_serializer = lambda v: json.dumps(v).encode('utf-8')
    )

@app.route('/v1/ds/message', methods=['POST'])
def handle_message() :
    try:
        message = request.json.get('message')
        result = messageService.process_message(message)
        serialized_result = result.json()

        producer.send('expense_service', serialized_result)

        return Response(
            serialized_result,
            status=200,
            mimetype='application/json'
        )
        producer
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=['GET'])
def handle_get():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)