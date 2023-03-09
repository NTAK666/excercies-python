import sqlite3

con = sqlite3.connect("./assets/ex4/sql.lite")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")


def insert_user():
    cur.execute("INSERT INTO users VALUES (1, 'John', 25)")
    cur.execute("INSERT INTO users VALUES (2, 'Mary', 30)")
    cur.execute("INSERT INTO users VALUES (3, 'Peter', 20)")


def update_user():
    cur.execute("UPDATE users SET age=30 WHERE id=1")


def delete_user():
    cur.execute("DELETE FROM users WHERE id=2")


def find_all():
    cur.execute("SELECT * FROM users")
    results = cur.fetchall()
    return results if len(results) else []


def find_by_id(id):
    cur.execute("SELECT * FROM users WHERE id=?", (id,))
    result = cur.fetchone()
    return result if result else None


def find_by_name(name):
    cur.execute("SELECT * FROM users WHERE name=?", (name,))
    result = cur.fetchone()
    return result if result else None


def find_by_age(age):
    cur.execute("SELECT * FROM users WHERE age=?", (age,))
    result = cur.fetchone()
    return result if result else None


if __name__ == "__main__":
    con.commit()
    con.close()
