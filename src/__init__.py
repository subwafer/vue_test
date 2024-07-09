from flask import Flask, jsonify, render_template, request, redirect, url_for
import time

def create_app(config=None) -> Flask:
    app = Flask(__name__)
    app.logged_in = False;
    app.username = None;

    if config is not None:
        print("Loading config not implemented yet.")

    @app.get("/")
    def index():
        if request.method == 'GET':
            if app.logged_in == False:
                return render_template("login.html")

        page_name = "Robot Admin"

        return render_template("index.html", page_name=page_name)

    @app.post("/__robots")
    def demo_data():
        demo_data = [
            {
                "id": 0,
                "name": "Robot 1",
                "job": "butler",
                "assigned_home_id": 0
            },
            {
                "id": 1,
                "name": "Robot 2",
                "job": "butler",
                "assigned_home_id": 1
            },
            {
                "id": 2,
                "name": "Robot 3",
                "job": "butler",
                "assigned_home_id": 2
            }
        ]

        time.sleep(2)

        return jsonify(demo_data)

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            if app.logged_in == False:
                return render_template("login.html")
            else:
                return redirect(url_for("index"))
        if request.method == "POST":
            print("logging in user")
            time.sleep(2)
            app.logged_in = True
            app.username = "admin"

            return redirect(url_for("index"))

    @app.route("/logout", methods=['GET', 'POST'])
    def logout():
        if (app.logged_in == False):
            return redirect(url_for("login"))
        else:
            print("Logging out user")
            app.logged_in = False
            return redirect(url_for("login"))

    return app
