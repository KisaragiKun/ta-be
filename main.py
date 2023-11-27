from flask import Flask
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "loker"

mysql = MySQL(app)
bcrypt = Bcrypt(app)

@app.get("/")
def home():
    cur = mysql.connection.cursor()
    username = "maul"
    cur.execute("""SELECT * FROM user WHERE username=%s""",(username,))
    rv = cur.fetchone()

    isTrue = bcrypt.check_password_hash(rv[2], "admin")

    return {
        "status": "oke",
        "message": "Welcome Home",
        "data": isTrue
    }

app.run(debug=True, port=3000)