from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route (renders the HTML form)
@app.route('/')
def home():
    return render_template('index.html')  # Ensure this matches your HTML file name

# Route to handle form submission
@app.route('/get_diet', methods=['POST'])
def get_diet():
    try:
        # Get user input from the form
        age = int(request.form.get('age'))
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        gender = request.form.get('gender')
        activity = int(request.form.get('activity'))
        plan = request.form.get('plan')
        meals = int(request.form.get('meals'))
        disease = request.form.get('disease')
        allergy = request.form.get('allergy')

        # Placeholder for diet recommendation logic
        recommendation = f"Based on your input, your recommended diet plan will be generated."

        # Return the response
        return jsonify({
            "age": age,
            "height": height,
            "weight": weight,
            "gender": gender,
            "activity_level": activity,
            "plan": plan,
            "meals": meals,
            "disease": disease,
            "allergy": allergy,
            "recommendation": recommendation
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
