from flask import Flask, jsonify,request
import sqlite3

database='test.db'

def connect_db():
    connetion=sqlite3.connect(database)
    connetion.row_factory = sqlite3.Row 
    return connetion
    
# start the database and create the tables in db 
def db_creation():
    conn = connect_db()
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS user(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name VARCHAR(255) NOT NULL,
                     age INTEGER ,
                     email VARCHAR(255) NOT NULL
                 );
                 """)
    conn.close()
    
db_creation()

app = Flask(__name__)

# request -> process[get data,formation ,call ...] -> response

# crud 
# ->      

# 

@app.route(
    '/users/',methods=['GET']
)
def get_users():
    conn=connect_db()
    data=conn.execute("SELECT * FROM user").fetchall()
    users = [dict(row) for row in data]
    conn.close()
    return jsonify(users) 


@app.route("/users/",methods=['POST'])
def insert_user():
    data = request.get_json()
    name=data.get('name')
    email = data.get('email')
    if name  and email :
        conn=connect_db()
        conn.execute("INSERT INTO user (name, email) VALUES (?,?)",(name,email))
        conn.commit()
        conn.close()
        return jsonify({"message":"user inserted successfully"})

# get user by id 

app.run(host='0.0.0.0', port=5000)
