from flask import Flask, request
import sqlite3 as sql
application = Flask(__name__)


@application.route('/auth', methods=['POST'])
def auth():
        token = request.form['token']
        with open('schema.sql', 'r') as sql_file:
           sql_script = sql_file.read()
        print('sql_script')   
        print(sql_script)
        con = sql.connect('mydb.db')
        cursor = con.cursor()
        cursor.executescript(sql_script)
        con.commit()
        cur = con.cursor()
        print("data save and execute query")
        cur.execute(
            "SELECT username from users where token = (?) LIMIT 1",
            (token, ))
        username = cur.fetchone()[0]
        print('username')
        print(username)
        con.close()
        return username


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5001)
