import pymysql

db = pymysql.connect("localhost", 'root', '1234', 'innovation')
cursor = db.cursor()
cursor.execute('''
DESCRIBE APPLY;
''')
applys = cursor.fetchall()
tmp = ''
for i, a in enumerate(applys):
    tmp += a[0] + '=' + a[0] + ', '
    if i % 4 == 0:
        print(tmp)
        tmp = ''
    # if i != 0 and i % 4 == 0:
    #     print(a[0] + '=' + a[0] + ',\n')
    # else:
    #     print(a[0] + '=' + a[0] + ', ')