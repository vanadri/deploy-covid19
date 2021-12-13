from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('modelregr.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    for x in request.form.values():
        total_kasus = x

    data = []
    data.append(int(total_kasus))
    
    prediction = model.predict(data)
    output = prediction

    return render_template('index.html', sembuh=output, total_kasus=total_kasus)

if __name__ == '__main__':
    app.run(debug=True)
