from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Mike Davis in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://render_tutorial_db_cnqp_user:SJybzxIsRC5XycPzOK1MG2oFYz8B0UMH@dpg-d7ast0cvjg8s73emsjmg-a/render_tutorial_db_cnqp")
    conn.close()
    return "Database Connection Successful"