from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key='BCT3FO5dvcED8cyJYZYYz55AO'
consumer_secret='yzznx5RFvaqjqaxnubcMWL4RPutJyRzTwu85jpqRUlykhc0dJL'
access_token ='1384514435385937926-otVjXRjJyXvNKzQ77dfG6JPTIGh0gi'
access_secret='nC9aoc6woTL21fHd3fzrWbJLGPFN2Z0clbCfSqlIMrNRi'

class StdOutListener(StreamListener):
    
    def on_Data(self,data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)
        
if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    stream = Stream(auth,listener)
    
    stream.filter(track=['covid'])
