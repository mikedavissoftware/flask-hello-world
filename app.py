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
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg.connect("postgresql://render_tutorial_db_cnqp_user:SJybzxIsRC5XycPzOK1MG2oFYz8B0UMH@dpg-d7ast0cvjg8s73emsjmg-a/render_tutorial_db_cnqp")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg.connect("postgresql://render_tutorial_db_cnqp_user:SJybzxIsRC5XycPzOK1MG2oFYz8B0UMH@dpg-d7ast0cvjg8s73emsjmg-a/render_tutorial_db_cnqp")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_str = ''
    response_str += '<table>'
    for player in records:
        response_str += '<tr>'
        for info in player:
            response_str += '<td>{}</td>'.format(info)
        response_str += '</tr>'
    response_str += '</table>'
    return response_str

@app.rout('/db_drop')
def db_drop():
    conn = psycopg.connect("postgresql://render_tutorial_db_cnqp_user:SJybzxIsRC5XycPzOK1MG2oFYz8B0UMH@dpg-d7ast0cvjg8s73emsjmg-a/render_tutorial_db_cnqp")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"