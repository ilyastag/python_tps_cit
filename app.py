from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import sys
import os
sys.path.append(os.path.dirname(__file__))
from config_db1 import Config



app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = "secret_key"

# Connexion MySQL
mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"]
        city = request.form["city"]
        email = request.form["email"]

        # Insertion dans la base de données
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (full_name, city, email) VALUES (%s, %s, %s)", (full_name, city, email))
        mysql.connection.commit()
        cur.close()

        flash("Inscription réussie !", "success")
        return redirect(url_for("register"))

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
