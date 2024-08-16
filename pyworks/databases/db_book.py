import sqlite3

def getconn():
    conn = sqlite3.connect('./output/bookdb.db')
    return conn
def create_book():
    conn = getconn()
    cursor = conn.cursor()
    sql = """
    CREATE TABLE book(
        book_no INTEGER PRIMARY key AUTOINCREMENT,
        title TEXT NOT NULL, 
        author TEXT NOT NULL,
        price INTEGER NOT NULL
    )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insert_book():
    conn = getconn()
    cursor = conn.cursor()
    # ? 동적 바인딩 기호
    sql = " Insert into book (title, author, price) values(?, ?, ?)"
    cursor.execute(sql, ("점프 투 파이썬", "박응용", 19800))
    conn.commit()
    conn.close()
def select_book():
    conn = getconn()
    cursor = conn.cursor()
    # ? 동적 바인딩 기호
    sql = "select * From book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    conn.close()
def update_book():
    conn = getconn()
    cursor = conn.cursor()
    # ? 동적 바인딩 기호
    sql = " update book set price = ? where title = ? "
    cursor.execute(sql, (15000, '천개의 파랑'))
    conn.commit()
    conn.close()
def select_one():
    conn = getconn()
    cursor = conn.cursor()
    # ? 동적 바인딩 기호
    sql = "select * From book where book_no = ?"
    cursor.execute(sql,(2,))
    rs = cursor.fetchone()
    print(rs)
    conn.close()

def delete_book():
    conn = getconn()
    cursor = conn.cursor()
    # ? 동적 바인딩 기호
    sql = " delete from book where book_no = ?"
    cursor.execute(sql, (1,))
    conn.commit()
    conn.close()
# create_book()
# insert_book()
# update_book()
# select_one()
delete_book()
select_book()