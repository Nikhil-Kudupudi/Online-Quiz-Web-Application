from pymongo import MongoClient
from django.conf import settings
def get_db_handle():
    client=MongoClient('mongodb://localhost:27017/')
    db_handle=client['polls_website']
    col=db_handle["poll_poll"]
    x=col.find()
    print(x)
    for data in x:
        print(data)
    return db_handle,client
get_db_handle()