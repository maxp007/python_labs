import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='dbuser',
    passwd='12345',
    db='first_db',
    use_unicode=True,
    charset='utf8'
)

c = db.cursor()

#c.execute("INSERT INTO computer (name, description) VALUES (%s, %s);", ('компутер', 'описание'))
db.commit()

c.execute("SELECT * FROM my_app_computer;")

entries = c.fetchall()

for el in entries:
    print(el)

c.close()

db.close()

#(1, 'Asus n550jk', '15,6 1920x1080 ips display, intel core i5-4600 2,8GHz, 8Gb RAM, 128Gb SSD, wifi 2,4GHz bgn+ac, bluetooth 4.0')
#(2, 'Asus n752jk', '17,1 1920x1080 ips display, intel core i7-4800 3,2GHz, 16Gb RAM, 256Gb SSD, wifi 2,4GHz bgn+ac, bluetooth 4.0')