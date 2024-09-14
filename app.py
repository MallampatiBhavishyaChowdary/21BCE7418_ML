from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "API is running!"}), 200

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is active!"}), 200

from models import db
from flask import request

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

from sentence_transformers import SentenceTransformer
from models import Document
import numpy as np

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query_text = data.get("text", "")
    top_k = data.get("top_k", 5)
    threshold = data.get("threshold", 0.8)

    # Encode the query
    query_embedding = model.encode(query_text)

    # Retrieve all documents and calculate similarity
    documents = Document.query.all()
    results = []
    for doc in documents:
        similarity = np.dot(query_embedding, np.array(doc.embedding))
        if similarity > threshold:
            results.append({"doc_id": doc.id, "similarity": similarity})

    # Sort by similarity and return top_k results
    results = sorted(results, key=lambda x: x['similarity'], reverse=True)[:top_k]
    return jsonify(results), 200

from cache import get_cached_query, cache_query_result

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query_text = data.get("text", "")
    user_id = data.get("user_id")
    
    cached_result = get_cached_query(user_id, query_text)
    if cached_result:
        return jsonify(cached_result), 200
    
    # Search logic (same as before)

    cache_query_result(user_id, query_text, results)
    return jsonify(results), 200
@app.before_request
def rate_limiter():
    user_id = request.json.get("user_id")
    user = User.query.filter_by(user_id=user_id).first()
    
    if not user:
        user = User(user_id=user_id, request_count=1)
        db.session.add(user)
    else:
        if user.request_count >= 5:
            return jsonify({"error": "Rate limit exceeded"}), 429
        user.request_count += 1
    
    db.session.commit()

from utils import log_request
import time

@app.route('/search', methods=['POST'])
def search():
    start_time = time.time()
    
    # Existing logic
    
    inference_time = time.time() - start_time
    log_request(user_id, "/search", inference_time)
    
    return jsonify(results), 200
