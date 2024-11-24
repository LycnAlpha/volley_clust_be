from flask import Flask, request, jsonify
import pickle

# Load the pickle model
with open('kmeans.pickle', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    print(f"Request data: {request.json}")
    try:
        # Get JSON data from the Flutter app
        data = request.json  
        
        # Extract multiple parameters from the JSON payload
        age = data.get('Age')
        bloodPressureDiastolic = data.get('Blood Pressure diastolic(mmHg)')
        bloodPressureSystolic = data.get('Blood Pressure Systolic(mmHg)')
        randomHeartRate = data.get('Random Heart Rate(min)')
        weight = data.get('Weight(kg)')
        height = data.get('Height(m)')
        bmi = data.get('BMI (kg/m2)')
        fat = data.get('Fat%')
        medicineBallThrow = data.get('Medicine Ball Throw(m)')
        verticleJump = data.get('Vertical Jump(mm)')
        speed = data.get('Speed')
        agilityTest = data.get('Agility test')
        handGripByBodyWeight = data.get('Hand grip/Body weight')
        sitUpsPerMin = data.get('Sit-ups/min')
        pushUpsPerMin = data.get('Push-ups/min')
        sitNReach = data.get('Sit & reach(cm)')
        vo2Max = data.get('Vo2 max/kg/min')
        skillsNTechniques = data.get('Skills and Techniques (%)')
        gameCondition = data.get('Game Condition (%)')
        genderEncoded = data.get('Gender_Encoded')
       
        
        # Convert inputs to the format your model requires (example: list of lists)
        input_data = [[age,bloodPressureDiastolic,bloodPressureSystolic,randomHeartRate,weight,height,bmi,fat,medicineBallThrow,verticleJump,speed,agilityTest,handGripByBodyWeight,sitUpsPerMin,pushUpsPerMin,sitNReach,vo2Max,skillsNTechniques,gameCondition,genderEncoded]]

        # Perform prediction
        prediction = model.predict(input_data)

        # Return the prediction
        print(prediction)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        print(f"error: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
