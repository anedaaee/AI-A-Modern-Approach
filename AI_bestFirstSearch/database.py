import mysql.connector
import json
def request(query) :
    db = mysql.connector.connect(user='root', password='ensALI!)(PASS82', host='localhost', database='AI')
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    columns = [i[0] for i in cursor.description]

    # Create dictionary from rows and columns
    data = [dict(zip(columns, row)) for row in rows]

    return data
