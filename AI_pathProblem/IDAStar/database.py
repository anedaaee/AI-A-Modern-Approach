import mysql.connector
def request(query) :
    db = mysql.connector.connect(user='root', password='', host='localhost', database='AI')
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    columns = [i[0] for i in cursor.description]


    data = [dict(zip(columns, row)) for row in rows]

    return data
