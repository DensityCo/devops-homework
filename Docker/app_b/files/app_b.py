from flask import Flask, request
import sqlite3 as sql
application = Flask(__name__)


@application.route('/auth', methods=['POST'])
def auth():
    try:
        token = request.form['token']
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute(
            "SELECT username from users where token = (?) LIMIT 1",
            (token, ))
        username = cur.fetchone()[0]
        con.close()
        return username
    except:
        return 'fail'


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5001)
