import mysql.connector

class MySQLConnect:
    
    def __init__(self, user, password, host, database):
        self.user = user
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
        
    def insert_to_db(self, statement):
        self.connection()
        # Some Type of Insert Function or Command
        self.close()
