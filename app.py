from flask import Flask
import psycopg

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Mike Davis in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg.connect("postgresql://render_tutorial_db_cnqp_user:SJybzxIsRC5XycPzOK1MG2oFYz8B0UMH@dpg-d7ast0cvjg8s73emsjmg-a/render_tutorial_db_cnqp")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg.connect("postgresql://render_tutorial_db_cnqp_user:SJybzxIsRC5XycPzOK1MG2oFYz8B0UMH@dpg-d7ast0cvjg8s73emsjmg-a/render_tutorial_db_cnqp")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()