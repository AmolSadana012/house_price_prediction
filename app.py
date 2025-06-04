from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session handling

model = joblib.load('house_price_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'user' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    try:
        longitude = float(request.form['longitude'])
        latitude = float(request.form['latitude'])
        housing_median_age = float(request.form['housing_median_age'])
        total_rooms = float(request.form['total_rooms'])
        total_bedrooms = float(request.form['total_bedrooms'])
        population = float(request.form['population'])
        households = float(request.form['households'])
        median_income = float(request.form['median_income'])
        bedroom_ratio = float(request.form['bedroom_ratio'])
        household_rooms = float(request.form['household_rooms'])

        ocean_proximity_1H_OCEAN = 1 if request.form.get('<1H_OCEAN') else 0
        ocean_proximity_INLAND = 1 if request.form.get('INLAND') else 0
        ocean_proximity_ISLAND = 1 if request.form.get('ISLAND') else 0
        ocean_proximity_NEAR_BAY = 1 if request.form.get('NEAR_BAY') else 0
        ocean_proximity_NEAR_OCEAN = 1 if request.form.get('NEAR_OCEAN') else 0

        input_features = [longitude, latitude, housing_median_age, total_rooms, total_bedrooms, 
                          population, households, median_income, ocean_proximity_1H_OCEAN, 
                          ocean_proximity_INLAND, ocean_proximity_ISLAND, ocean_proximity_NEAR_BAY, 
                          ocean_proximity_NEAR_OCEAN, bedroom_ratio, household_rooms]

        prediction = model.predict([input_features])[0]
        
        return render_template('index.html', prediction_text=f"Estimated Price: ₹{prediction:,.2f}")
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}. Please try again with valid input.")

@app.route('/house/<int:house_id>')
def house_detail(house_id):
    # Example data — you can replace this with a database later
    house_info = {
    1: {
        'title': 'House 1 - Near Bay',
        'image': 'static/house1.jpg',
        'details': '''Total number of bedrooms: 3<br>
                      Total number of bathrooms: 2<br>
                      Area: 1500 sq ft<br>
                      Price: ₹85,00,000'''
    },
    2: {
        'title': 'House 2 - Inland',
        'image': 'static/house2.jpg',
        'details': '''Bedrooms: 6<br>
                      Bathrooms: 5<br>
                      Area: 2000 sq ft<br>
                      Price: ₹195,00,000'''
    },
    3: {
        'title': 'House 3 - Near Ocean',
        'image': 'static/house3.jpg',
        'details': '''Bedrooms: 4<br>
                      Bathrooms: 4<br>
                      Area: 1200 sq ft<br>
                      Price: ₹75,00,000'''
    }
}

    house = house_info.get(house_id)
    if not house:
        return "House not found", 404

    return render_template('house_detail.html', house=house)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
