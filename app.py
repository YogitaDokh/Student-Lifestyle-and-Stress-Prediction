import os
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Load the trained SVC model
MODEL_PATH = "SVC_Model.pkl"
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# Interactive & User-Friendly HTML Template with Demo Button
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Performance Predictor</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: #333;
        }
        .container {
            background: #fff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            width: 100%;
            max-width: 500px;
            margin: 20px;
        }
        h2 {
            text-align: center;
            color: #4a5568;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 13px;
            color: #718096;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 18px;
        }
        label {
            display: block;
            margin-bottom: 6px;
            font-weight: 600;
            font-size: 14px;
            color: #4a5568;
        }
        input, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #cbd5e0;
            border-radius: 8px;
            box-sizing: border-box;
            font-size: 14px;
            transition: border-color 0.3s;
        }
        input:focus, select:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #667eea;
            border: none;
            border-radius: 8px;
            color: white;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s;
            margin-top: 10px;
        }
        button:hover {
            background: #5a67d8;
        }
        .demo-btn {
            background: #4a5568;
            margin-bottom: 20px;
            font-size: 14px;
            padding: 8px;
        }
        .demo-btn:hover {
            background: #2d3748;
        }
        .result-box {
            margin-top: 25px;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            font-weight: 600;
            display: none;
        }
        .success { background-color: #c6f6d5; color: #22543d; border: 1px solid #9ae6b4; }
        .error { background-color: #fed7d7; color: #742a2a; border: 1px solid #feb2b2; }
    </style>
</head>
<body>

<div class="container">
    <h2>Student Performance Predictor</h2>
    <p class="subtitle">Note: Model limits are highly sensitive to specific distance configurations.</p>
    
    <button type="button" class="demo-btn" onclick="loadDemoValues()">⚡ Load Sample Data (Will Predict 1)</button>

    <form id="predictionForm">
        <div class="form-group">
            <label for="Student_Type">Student Type (0 - 3)</label>
            <select id="Student_Type" name="Student_Type" required>
                <option value="0">Type 0</option>
                <option value="1">Type 1</option>
                <option value="2">Type 2</option>
                <option value="3">Type 3</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="Sleep_Hours">Daily Sleep Hours (4.5 - 8.5)</label>
            <input type="number" id="Sleep_Hours" name="Sleep_Hours" step="0.01" min="0" max="24" required placeholder="e.g., 6.37">
        </div>

        <div class="form-group">
            <label for="Study_Hours">Daily Study Hours (1.5 - 7.5)</label>
            <input type="number" id="Study_Hours" name="Study_Hours" step="0.01" min="0" max="24" required placeholder="e.g., 3.95">
        </div>

        <div class="form-group">
            <label for="Social_Media_Hours">Daily Social Media Hours (1.0 - 6.0)</label>
            <input type="number" id="Social_Media_Hours" name="Social_Media_Hours" step="0.01" min="0" max="24" required placeholder="e.g., 2.61">
        </div>

        <div class="form-group">
            <label for="Attendance">Attendance Percentage (65% - 100%)</label>
            <input type="number" id="Attendance" name="Attendance" step="0.01" min="0" max="100" required placeholder="e.g., 81.27">
        </div>

        <div class="form-group">
            <label for="Exam_Pressure">Exam Pressure Level (1 - 10)</label>
            <input type="number" id="Exam_Pressure" name="Exam_Pressure" min="1" max="10" required placeholder="e.g., 8">
        </div>

        <div class="form-group">
            <label for="Family_Support">Family Support Level (1 - 10)</label>
            <input type="number" id="Family_Support" name="Family_Support" min="1" max="10" required placeholder="e.g., 7">
        </div>

        <div class="form-group">
            <label for="Month">Academic Month (1 - 12)</label>
            <input type="number" id="Month" name="Month" min="1" max="12" required placeholder="e.g., 2">
        </div>

        <button type="submit">Predict Outcome</button>
    </form>

    <div id="result" class="result-box"></div>
</div>

<script>
    function loadDemoValues() {
        document.getElementById('Student_Type').value = "0";
        document.getElementById('Sleep_Hours').value = "6.0";
        document.getElementById('Study_Hours').value = "3.0";
        document.getElementById('Social_Media_Hours').value = "2.0";
        document.getElementById('Attendance').value = "80.0";
        document.getElementById('Exam_Pressure').value = "9";
        document.getElementById('Family_Support').value = "7";
        document.getElementById('Month').value = "2";
    }

    document.getElementById('predictionForm').addEventListener('submit', async function(e) {
        e.preventDefault();
        const resultDiv = document.getElementById('result');
        resultDiv.style.display = 'none';

        const formData = {
            Student_Type: parseFloat(document.getElementById('Student_Type').value),
            Sleep_Hours: parseFloat(document.getElementById('Sleep_Hours').value),
            Study_Hours: parseFloat(document.getElementById('Study_Hours').value),
            Social_Media_Hours: parseFloat(document.getElementById('Social_Media_Hours').value),
            Attendance: parseFloat(document.getElementById('Attendance').value),
            Exam_Pressure: parseFloat(document.getElementById('Exam_Pressure').value),
            Family_Support: parseFloat(document.getElementById('Family_Support').value),
            Month: parseFloat(document.getElementById('Month').value)
        };

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            const data = await response.json();

            if (response.ok) {
                resultDiv.className = "result-box success";
                resultDiv.innerHTML = `Prediction Result: <strong>${data.prediction}</strong>`;
            } else {
                resultDiv.className = "result-box error";
                resultDiv.innerHTML = `Error: ${data.error}`;
            }
        } catch (err) {
            resultDiv.className = "result-box error";
            resultDiv.innerHTML = "An error occurred while connecting to the server.";
        }
        resultDiv.style.display = 'block';
    });
</script>

</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        features = [
            float(data['Student_Type']),
            float(data['Sleep_Hours']),
            float(data['Study_Hours']),
            float(data['Social_Media_Hours']),
            float(data['Attendance']),
            float(data['Exam_Pressure']),
            float(data['Family_Support']),
            float(data['Month'])
        ]
        
        input_data = np.array([features])
        prediction = model.predict(input_data)[0]
        
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
