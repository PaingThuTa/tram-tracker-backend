from flask import Flask, jsonify, request
import redis

app = Flask(__name__)

# Redis connection details
redis_host = "redis-17751.crce178.ap-east-1-1.ec2.redns.redis-cloud.com"  # Replace with your Redis hostname
redis_port = 17751  # Replace with your Redis port
redis_password = "your_password_here"  # Replace with your Redis password

# Connect to Redis
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

@app.route('/')
def home():
    """Home route to confirm the API is running."""
    return jsonify({"message": "Tram Tracker Backend is running!"})

@app.route('/gps/<tram_id>', methods=['POST'])
def store_gps(tram_id):
    """
    Store GPS data for a specific tram.
    JSON body must include 'latitude' and 'longitude'.
    """
    data = request.json
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    if not latitude or not longitude:
        return jsonify({"error": "Invalid data"}), 400

    # Save to Redis
    r.set(f"gps:{tram_id}", f"{latitude},{longitude}")
    return jsonify({"message": f"GPS data for tram {tram_id} stored successfully!"})

@app.route('/gps/<tram_id>', methods=['GET'])
def retrieve_gps(tram_id):
    """
    Retrieve GPS data for a specific tram.
    """
    gps_data = r.get(f"gps:{tram_id}")
    if gps_data:
        latitude, longitude = gps_data.split(",")
        return jsonify({"tram_id": tram_id, "latitude": latitude, "longitude": longitude})
    return jsonify({"error": "No GPS data found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
