from flask import (Flask, g, render_template, flash, redirect, url_for, abort)
from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user,
                         login_required, current_user)

import forms
import models

DEBUG = True
PORT = 5000
HOST = "127.0.0.1"

app = Flask(__name__)
app.secret_key = "topsecret!"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route("/register", methods=("GET", "POST")) 
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        models.User.create_user(
            email=form.email.data,
            password=form.password.data,
            wsc=form.wsc.data,
        )
        return redirect(url_for("register_successful"))
    return render_template("register.html", form=form)


@app.route("/register_successful")
def register_successful():
    return render_template("register_successful.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Your email or password is incorrect!", "danger")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                #flash("You've been logged in!", "success")
                return redirect(url_for("qaform"))
            else:
                flash("Your email or password is incorrect!", "danger")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    #flash("You've been logged out!", "success")
    return redirect(url_for("index"))


@app.route("/qaform", methods=("GET", "POST"))
@login_required
def qaform():
    form = forms.QAForm()
    user = current_user 
    if form.validate_on_submit():
        models.QA.create(
            user=g.user._get_current_object(),
            responsibilities=form.responsibilities.data.strip(),
            safety=form.safety.data.strip(),
            stream_install=form.stream_install.data.strip(),
            station_desc=form.station_desc.data.strip(),
            station_photos=form.station_photos.data.strip()
        ) 
        return redirect(url_for("qaresults"))
    return render_template("qaform.html", form=form, user=user)


@app.route("/qaresults")
@login_required
def qaresults():
    data = current_user.get_qa_data()
    user = current_user 

    return render_template(
        "qaresults.html", 
        user=user, 
        data=data
    ) 


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    models.initialize()
    try:
        models.User.create_user(
            email="jlant@usgs.gov",
            password="password",
            wsc="Ohio-Kentucky-Indiana"
        )
    except ValueError:
        pass   

    app.run(debug=DEBUG, host=HOST, port=PORT)


