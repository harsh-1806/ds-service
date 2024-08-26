import os
from flask import Flask
from flask import request, jsonify, Response
from kafka import KafkaProducer
import json
from dotenv import load_dotenv

from services.messageService import MessageService


app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()

load_dotenv()

kafka_host = os.getenv("KAFKA_HOST", "localhost")
kafka_port = os.getenv("KAFKA_PORT", "9092")
producer = KafkaProducer(
        bootstrap_servers = [f'{kafka_host}:{kafka_port}'],
        value_serializer = lambda v: json.dumps(v).encode('utf-8')
    )

@app.route('/api/v1/ds/message', methods=['POST'])
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
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="localhost", port=8010, debug=True)