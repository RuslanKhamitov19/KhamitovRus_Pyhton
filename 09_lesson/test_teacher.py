from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = create_engine(db_connection_string)

def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM teacher"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['email'] == "lloyd80@ferry.com"

    connection.close()

def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT INTO teacher(email) VALUES (:new_email)")
    connection.execute(sql, {"new_email":'rus.khamitov.19@bk.ru'})
    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE teacher SET group_id = :group_id WHERE email = :email")
    connection.execute(sql, {"group_id": 1111, "email": 'rus.khamitov.19@bk.ru'})

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM teacher WHERE group_id = :group_id")
    connection.execute(sql, {"group_id": 1111})

    transaction.commit()
    connection.close()