### REDIS SERVER MUST BE RUNNING ###

__author__ = 'Conor'

import redis

server = redis.Redis('localhost')
print(server)

# Use the pipeline() method to create a pipeline transaction
pipe = server.pipeline()

# The following SET commands are buffered
pipe.set('count', 1)
pipe.incr('count')
pipe.incrby('count', 8)
pipe.incr('count')
pipe.decr('count')

# the EXECUTE call sends all buffered commands to the server, returning
# a list of responses, one for each command.
print(pipe.execute())

print(server.get('count'))



