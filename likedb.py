from tinydb import TinyDB,Query
from tinydb.database import Document
import json
class LikeDB:
    def __init__(self,file) -> None:
        self.db=TinyDB(file,indent=4)
    def save(self,message_id,chat_id):
        id=self.db.table(message_id)
        user=Document(
            {
                "like":0,
                "dislike":0
            },doc_id=chat_id
        )
        id.insert(user)
    def like(self,message_id,chat_id):
        like=self.db.table(str(message_id-1)).get(doc_id=chat_id)["like"]
        dislike=self.db.table(str(message_id-1)).get(doc_id=chat_id)["dislike"]
        if like==0 and dislike==0:
            user={"like":1}
            self.db.table(str(message_id-1)).update(user,doc_ids=[chat_id])
        elif like ==0 and dislike==1:
            user={"like":1,
                  "dislike":0}
            self.db.table(str(message_id-1)).update(user,doc_ids=[chat_id])
        elif like ==1 and dislike ==0:
            user={
                "like":0
            }
            self.db.table(str(message_id-1)).update(user,doc_ids=[chat_id])
    def dislike(self,message_id,chat_id):
        like=self.db.table(str(message_id-1)).get(doc_id=chat_id)["like"]
        dislike=self.db.table(str(message_id-1)).get(doc_id=chat_id)["dislike"]
        if like==0 and dislike==0:
            user={"dislike":1}
            self.db.table(str(message_id-1)).update(user,doc_ids=[chat_id])
        elif like ==0 and dislike==1:
            user={
                  "dislike":0}
            self.db.table(str(message_id-1)).update(user,doc_ids=[chat_id])
        elif like ==1 and dislike ==0:
            user={
                "like":0,
                "dislike":1
            }
            self.db.table(str(message_id-1)).update(user,doc_ids=[chat_id])
    def add_like(self,message_id,chat_id):
        like=self.db.table(str(message_id-1)).get(doc_id=chat_id)["like"]
        return like
    def add_dislike(self,message_id,chat_id):
        dislike=self.db.table(str(message_id-1)).get(doc_id=chat_id)["dislike"]
        return dislike