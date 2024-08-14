# 사원 관리 - 조회(전체, 1건), 삽입, 수정, 삭제
import sqlite3

# 사원 전체 조회
def select_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "SELECT * FROM employee"
    cur.execute(sql)
    rs = cur.fetchall()
    # print(rs)
    for i in rs:
        print(i)

    conn.close()
def insert_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e105', '조대리', 4500000)"
    cur.execute(sql)
    conn.commit()

    conn.close()

def update_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "UPDATE employee SET salary = 2500000 where emp_id = 'e104'"
    cur.execute(sql)
    conn.commit()

    conn.close()

def delete_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "DELETE FROM employee where emp_id = 'e102'"
    cur.execute(sql)
    conn.commit()

    conn.close()

def select_one():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    # 이름에 대리가 포함된 정보를 검색하시오
    sql = "SELECT * FROM employee WHERE name LIKE '%신입%'"
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs)

    conn.close()


# insert_emp()
update_emp()
delete_emp()
# select_emp()
select_one()




