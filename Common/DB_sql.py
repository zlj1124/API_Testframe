# -*- coding:UTF-8 -*-
import pymysql.cursors
from Conf.Config import Config
conf = Config()



class DbConnect(object):  

    def __init__(self):
        self.connection = pymysql.connect(
            host= conf.db_qiye6host,
            port= int(conf.db_qiye6port),
            user=  conf.db_qiye6user,
            password= conf.db_qiye6password,
            db= conf.db_qiye6name,
            charset= conf.db_qiye6charset,
            cursorclass=pymysql.cursors.DictCursor
            )
        self.cursor=self.connection.cursor()

    def update_sql(self, *args):
        try:
            sql = "UPDATE %s SET %s=%s WHERE %s='%s';" %(args)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:   
            print('Error:%s'%e)
               
        
            
    def delete_sql(self, *args):
        try:
            
            sql = "DELETE FROM %s WHERE %s='%s';" %(args)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:   
            print('Error:%s'%e)    
       
               
    def select_sql(self, *args):
        try:
            sql = "SELECT %s, %s, %s FROM %s WHERE %s='%s' ORDER BY %s DESC LIMIT 1;" %(args)
            self.cursor.execute(sql)
            self.connection.commit()
            result = self.cursor.fetchall()
            return result[0]
        except Exception as e:   
            print('Error:%s'%e)
       
          
    def close_conn(self):
        self.connection.close()
        self.cursor.close()
        

          
        

if __name__ == "__main__":
    pass











