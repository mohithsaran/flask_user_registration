from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

users_db = {}

@app.route('/register', methods=['POST'])
def register_user():
    try:
        # Get user data from JSON payload
        user_data = request.get_json()
        username = user_data.get('username')
        if not username:
            return jsonify({'error': 'Username is required'}), 400  
        email = user_data.get('email')
        if not email:
            return jsonify({'error': 'Email is required'})
        password = user_data.get('password')
        if not password:
            return jsonify({'error': 'Password is required'}), 400 

        # Basic validation
        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400
        if len(password) < 8:
            return jsonify({'error': 'Password must be at least 8 characters long'}), 400
        
        #Hashing password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Save user information to mock database
        users_db[username] = {'email': email, 'password': hashed_password}

        return jsonify({'message': 'User registered successfully','username':username,'email':email,'password':hashed_password}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
