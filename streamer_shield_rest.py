import os
import sys
from quart import Quart, request, jsonify
import numpy as np
from streamer_shield import StreamerShield

app = Quart(__name__)
shield = StreamerShield("attempt_5.h5", "vocabulary_5.json", 30)

# Create an endpoint that accepts a string and returns a float
@app.route('/api/predict', methods=['POST'])
async def calculate():
    try:
        data = await request.get_json()

        input_string = data['input_string']

        # You can perform your calculations here and return a float
        result = predict(input_string).numpy()

        return jsonify({'result': np.floor(result[0][0]*1000)})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400

@app.route('/health')
def health():
    return 'I\'m Healthy',200

def predict(input_string):
    return shield.predict(input_string)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 38080))
    app.run('0.0.0.0',debug=False, port=port)
