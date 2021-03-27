from ItsAGramLive import ItsAGramLive
import psycopg2

connectionString = "host=argestrateji-do-user-8243456-0.b.db.ondigitalocean.com port=25060 dbname=muzayede-tv-db user=muzayede-tv-admin password=t2ra1g7kxr9ssw6d"

conn = psycopg2.connect(connectionString)
cur = conn.cursor()

cur.execute("SELECT * FROM STREAMING_CONF WHERE channelname='{}';".format('unvermezat_main'))
data = cur.fetchone()
live = ItsAGramLive(data[9], data[10])

live.login()

live.comment_stream(data[1])
