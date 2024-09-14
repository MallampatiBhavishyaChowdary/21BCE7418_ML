import redis
import json

cache = redis.Redis(host='localhost', port=6379)

def get_cached_query(user_id, query):
    key = f"{user_id}:{query}"
    cached_result = cache.get(key)
    if cached_result:
        return json.loads(cached_result)
    return None

def cache_query_result(user_id, query, result):
    key = f"{user_id}:{query}"
    cache.setex(key, 3600, json.dumps(result))
