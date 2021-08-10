from re import S
import mysql.connector
from mysql.connector.connection import MySQLConnection

class MySQLConnect(MySQLConnection):
    
    def __init__(self, userid, password, host, database):
        self.user = userid
        self.password = password
        self.host = host
        self.database = database
        
    def connection(self):
        try:
            mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
            print('Connection Openned')
        except mysql.connector.Error as err:
            if err.errno == 1045:
                print("Something is wrong with your user name or password")
            elif err.errno == 1049:
                print("Database does not exist")
            else:
                print(err)
        else:
            mysql.connector.connection.MySQLConnection.close

    def close(self):
        mysql.connector.connection.MySQLConnection.close
        print('Connection Closed')
        
    def insertCursor(self, info):
        MySQLConnection.cursor(info)
        
    def testDataInsert(self):
        ("INSERT INTO kutaku_news "
             "(title, url, date)"
             "VALUES (test1, test2, test3)")
        
    def insert_to_db(self, dataToInsert):
        self.connection()
        # Some Type of Insert Function or Command
        for articleData in dataToInsert:
            ("INSERT INTO kutaku_news "
             "(title, url, date)"
             "VALUES (test1, test2, test3)")
            print(f"{articleData['title']}, {articleData['url']}, {articleData['date']}")
        self.close()


testData = [{"title":"testTitle", "url":"TESTURL", "date":"10/03/79"}]
m = MySQLConnect("root", "password", "127.0.0.1", "scraper")
