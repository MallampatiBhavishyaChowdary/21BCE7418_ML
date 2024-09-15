#Initial Project Setup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "API is running!"}), 200

if __name__ == "__main__":
    app.run(debug=True) #Implement untill here for setup first.Then, we can commit it and check git status.
  
#Then implementing this code block.This is for /health endpoint to verify our API status.
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is active!"}), 200. #Commit
