import redis
import sys
import json


r = redis.ConnectionPool(host='35.187.193.187', port=6380)
r = redis.Redis(connection_pool=r)

data = {'url': sys.argv[1], 'level': sys.argv[2]}
data = json.dumps(data)
r.sadd('preparation', data)

print('写入成功.')
