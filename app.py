from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse JSON data from request
    data = request.get_json()

    test = data.get('test')

    # Print the 'test' value to the console (or handle it as needed)
    print(test)

    # Respond with a confirmation (optional)
    return jsonify({"status": "success", "test_value": test}), 200


if __name__ == '__main__':
    app.run(debug=True)

