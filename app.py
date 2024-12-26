from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample user data (in a real application, use a database)
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"error": "Invalid credentials!"}), 400

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get numbers from the request
    num1 = request.form.get('num1', type=float)
    num2 = request.form.get('num2', type=float)
    operation = request.form.get('operation')

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({"error": "Cannot divide by zero!"}), 400
    else:
        return jsonify({"error": "Invalid operation!"}), 400

    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=True)