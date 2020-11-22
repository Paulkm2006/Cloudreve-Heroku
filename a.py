import os

mysql_str=os.getenv('JAWSDB_URL')
redis_str=os.getenv('REDISCLOUD_URL')

os.putenv('redis_pwd',redis_str[16:48])
os.putenv('redis_host',redis_str[49:107])
os.putenv('DB_Host',mysql_str[42:104])
os.putenv('DB_User',mysql_str[8:24])
os.putenv('DB_Password',mysql_str[25:41])
os.putenv('DB_Name',mysql_str[105:121])

print(redis_str[16:48])
