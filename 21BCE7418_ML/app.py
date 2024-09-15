#Initial Project Setup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "API is running!"}), 200

if __name__ == "__main__":
    app.run(debug=True) #Implement untill here for setup first.Then, we can commit it and check git status.
  
