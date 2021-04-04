from flask import Flask, request
import psycopg2

app = Flask(__name__)

# con = psycopg2.connect(
#     host = "localhost",
#     port = "26257",
#     database = "savesmart",
#     user = "lex",
#     password = "lex"
# )

# cur = con.cursor()

# def get_last_tid():
#     cur.execute("SELECT * FROM transactions")
#     rows = cur.fetchall()
#     return len(rows)

# def add_transaction(datetime, id, quantity, total):
#     cur.execute("INSERT INTO transactions (tid, dayandtime, id, quantity, total) VALUES (" + str(get_last_tid() + 1) + ", \'" + datetime + "\', " + str(id) + ", " + str(quantity) + ", " + str(total) + ")" )

# def transaction_from_inventory(tid):
#     cur.execute("SELECT * FROM transactions WHERE tid = " + str(tid))
#     rows = cur.fetchall()
#     print("zoop")
#     item_id = rows[0][2]
#     transaction_quantity = rows[0][3]
#     cur.execute("SELECT quantity FROM inventory WHERE id = " + str(item_id))
#     rows = cur.fetchall()
#     inventory_quantity = rows[0][0]
#     cur.execute("UPDATE inventory SET quantity = " + str(inventory_quantity - transaction_quantity) + " WHERE id = " + str(item_id))



# cur.execute("SELECT * FROM inventory")
# rows = cur.fetchall()
# print(rows)

# add_transaction('2021-04-02 15:23:54', 3, 2, 5.0)

# cur.execute("SELECT * FROM inventory")
# rows = cur.fetchall()
# print(rows)


# cur.execute("SELECT * FROM transactions")
# rows = cur.fetchall()
# print(rows)

# cur.execute("COMMIT")
# cur.close()
# con.close()

@app.route('/create_transaction/<datetime>/<id>/<quantity>/<total>', methods=['GET'])
def create_transaction(datetime, id, quantity, total):
    con = psycopg2.connect(
    host = "localhost",
    port = "26257",
    database = "savesmart",
    user = "lex",
    password = "lex"
    )

    cur = con.cursor()

    def get_last_tid():
        cur.execute("SELECT * FROM transactions")
        rows = cur.fetchall()
        return len(rows)
    def add_transaction(datetime, id, quantity, total):
        cur.execute("INSERT INTO transactions (tid, dayandtime, id, quantity, total) VALUES (" + str(get_last_tid() + 1) + ", \'" + datetime + "\', " + str(id) + ", " + str(quantity) + ", " + str(total) + ")" )

    add_transaction(datetime, id, quantity, total)
    cur.execute("COMMIT")
    cur.close()
    con.close()

@app.route('/add_inventory/<id>/<name>/<quantity>/<price>', methods=['GET'])
def add_inventory(id, name, quantity, prices):
    con = psycopg2.connect(
    host = "localhost",
    port = "26257",
    database = "savesmart",
    user = "lex",
    password = "lex"
    )

    cur = con.cursor()

    def get_last_id():
        cur.execute("SELECT * FROM transactions")
        rows = cur.fetchall()
        return len(rows)

    cur.execute("COMMIT")
    cur.close()
    con.close()    

@app.route('/update_inventory/', methods=['GET'])
def update_inventory():
    con = psycopg2.connect(
    host = "localhost",
    port = "26257",
    database = "savesmart",
    user = "lex",
    password = "lex"
    )

    cur = con.cursor()

    def get_last_tid():
        cur.execute("SELECT * FROM transactions")
        rows = cur.fetchall()
        return len(rows)

    def transaction_from_inventory(tid):
        cur.execute("SELECT * FROM transactions WHERE tid = " + str(tid))
        rows = cur.fetchall()
        print("zoop")
        item_id = rows[0][2]
        transaction_quantity = rows[0][3]
        cur.execute("SELECT quantity FROM inventory WHERE id = " + str(item_id))
        rows = cur.fetchall()
        inventory_quantity = rows[0][0]
        cur.execute("UPDATE inventory SET quantity = " + str(inventory_quantity - transaction_quantity) + " WHERE id = " + str(item_id))
    last_tid = get_last_tid()
    for i in range(1, last_tid + 1):
        transaction_from_inventory(i)
    
    cur.execute("COMMIT")
    cur.close()
    con.close()   