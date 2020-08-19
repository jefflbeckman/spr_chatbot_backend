import pymongo
from chat_ai import ChatAI

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["DiscordMessagesDB"]
messages = mydb["messages"]

class ChatServer:

    def __init__(self,
                 dburl="mongodb://localhost:27017/",
                 table_name="DiscordMessagesDB",
                 collection_name="messages"):
        self._dburl = dburl
        self.__table_name = table_name
        self.__collection_name = collection_name
        myclient = pymongo.MongoClient(self._dburl)
        mydb = myclient[self.__table_name]
        messages = mydb[self.__collection_name]

    def get_messages(self, n=1000):
            for message in messages.find().sort("_id", -1).limit(1000):
                yield message

    def generate_message(self):
        ai = ChatAI()
        pass
