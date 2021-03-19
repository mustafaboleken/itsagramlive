from ItsAGramLive import ItsAGramLive;

live = ItsAGramLive('mboleken8@gmail.com', 'mustafa01')

live.login()

live.create_broadcast()

print(live.stream_key)
input()
live.start_broadcast()
id = live.broadcast_id
live.comment_stream(id)
