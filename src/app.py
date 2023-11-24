from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()

    # Assuming data.txt is in the same directory
    file_path = 'data.txt'

    # Write form data to the text file
    with open(file_path, 'a') as file:
        file.write(f"ID: {data['id']}, Password: {data['password']}, New Password: {data['newPassword']}, Confirm New Password: {data['confirmNewPassword']}\n")

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
