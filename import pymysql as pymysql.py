import pymysql as pymysql
import datetime as dt

#============
#DB CONNECT
#============
host = "?"
port = 3306
database = 'test'
username = 'testdb'
password = 'pw'

conn = pymysql.connect(host, user=username, passwd=password, db=database, port=port, use_unicode=True, charset='utf8')
cursor = conn.cursor()
#============
#날짜 셋팅
#============
now = dt.datetime.now()
year_ago = dt.datetime.strptime(now - dt.timedelta(years=1), "%Y-%m-%d")

#============
# SELECT
#============
sel_sql = "SELECT * FROM TESTDB WHERE DATETIME < {year_ago}".format(year_ago=year_ago)
cursor.execute(sel_sql)
rows = cursor.fetchall()

#============
#DEL 조건
#============
#여기만테스트
temp_text = ''
for key, value in rows:    
    for key2, value2 in value:        
        if key2 == 'key':
            temp_text = "{temp_text} '{row_text}',".format(temp_text=temp_text, row_text=value[key2])
temp_text.strip(",")

#============
# DELETE
#============
del_sql = "DELETE FROM TESTDB WHERE in ({key_string})".format(key_string=temp_text)
del_sql = "DELETE FROM TESTDB_thum WHERE in ({key_string})".format(key_string=temp_text)
print("select from testdb where in ({key_string})".format(key_string=temp_text))
print(del_sql)
#cursor.execute(del_sql)

#============
# DB CLOSE
#============
conn.close()