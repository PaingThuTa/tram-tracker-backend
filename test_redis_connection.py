import redis

# Redis connection details
redis_host = "redis-17751.crce178.ap-east-1-1.ec2.reds.cloud.com"  # Replace with your Redis endpoint
redis_port = 17751             # Replace with your Redis port
redis_password = "EzGF9Au8QHkMbPEInpqSJ6ubZ1wWE2hy"  # Replace with your Redis password

try:
    # Connect to Redis
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    # Test connection
    r.set("test_key", "Hello, Redis!")
    value = r.get("test_key")
    print(f"Retrieved value: {value}")
except Exception as e:
    print(f"Error connecting to Redis: {e}")
