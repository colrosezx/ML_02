from flask import Flask, request, jsonify
import pickle
import os
from waitress import serve

app = Flask(__name__)

def load_model():
    """Загрузка обученной модели"""
    model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
    with open(model_path, 'rb') as f:
        return pickle.load(f)

model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Адаптируйте под ваши фичи (пример для Titanic)
        features = [
            data['Pclass'],
            data['Name'],
            data['Sex'],
            data['Age'],
            data['SibSp'],
            data['Parch'],
            data['Fare'],
            data['Embarked']
        ]
        prediction = model.predict([features])
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("Starting Flask service...")
    serve(app, host="0.0.0.0", port=5000)