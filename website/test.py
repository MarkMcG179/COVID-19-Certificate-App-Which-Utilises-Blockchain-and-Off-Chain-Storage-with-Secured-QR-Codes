from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/<password>')
def index(password):
    hashed_value = generate_password_hash(password, method='sha256')

    #stored_password = 'sha256$KANzJWB5N3LabIPz$5530e2f925bdbceb2cd8e27000ade8f33902f8c544a5f616b2cda7c5283cd195'

    #result = check_password_hash(stored_password, password)

    return hashed_value

if __name__ == '__main__':
    app.run(debug=True)
