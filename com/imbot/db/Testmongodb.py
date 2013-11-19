__author__ = 'grishmashah'

from com.imbot.db import mongodb
def test_db():
  testDbClient = mongodb.IMBotDb(dbname='imbot_testdb')
  testDbClient.writeData("testcoll1", {"fname": "grishma", "lname": "shah"})
  data = testDbClient.readData("testcoll1")
  assert data['fname'] == "grishma"
  assert data['lname'] == "shah"