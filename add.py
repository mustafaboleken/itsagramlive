from ItsAGramLive import ItsAGramLive

live = ItsAGramLive('mboleken8@gmail.com', 'mustafa02')

live.login()

live.create_broadcast()

print(live.stream_key)
input()
live.start_broadcast()
id = live.broadcast_id
live.comment_stream(id)

procedure #1

from ItsAGramLive import ItsAGramLive

live = ItsAGramLive('mboleken8@gmail.com', 'mustafa02')

live.login()

live.create_broadcast()

print(live.stream_key)
print(live.broadcast_id)

live.start_broadcast()

procedure #2

from ItsAGramLive import ItsAGramLive

live = ItsAGramLive('mboleken8@gmail.com', 'mustafa01')

live.login()

live.comment_stream(id)
