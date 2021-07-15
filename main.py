import pymysql

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "database": "test_1"
}
db = pymysql.connect(**config)
cursor = db.cursor()
sql="INSERT INTO `user`(`name`,age)VALUES('王六','20')"
res = cursor.execute(sql)
db.commit()
print(res)