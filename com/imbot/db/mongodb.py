__author__ = 'ssanghra'

from pymongo import MongoClient

class IMBotDb:

  imbotdb = None
  def __init__(self, host="localhost", port=27017, dbname="imbot_db"):
    client = MongoClient(host=host, port=port)
    self.imbotdb = client[dbname]

  def writeData(self, collName, data):
    coll = self.imbotdb[collName]
    coll.insert(data)

  def readData(self, collName):
    coll = self.imbotdb[collName]
    return coll.find_one()
