from flask import Flask, render_template, redirect, url_for, flash
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_a_Secret_key"


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/signup", methods=["GET", "POST"])
# we have written both GET and POST methods because if we write only POST then we'll get
# error, this is because for data to get POSTed on the server we first need to GET the data.
# POST will not work until we click on signup submit button, till then only GET method is working.
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # if validation is done and the result is true.
        flash(f"Successfully Registered {form.username.data}!")
        return redirect(url_for("home"))
    return render_template("signup.html", title="Sign Up", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    email = form.email.data
    pw = form.password.data

    if form.validate_on_submit():
        if email == "a@b.com" and pw == "12345":
            flash("Logged in Successfully")
            return redirect(url_for("home"))
        else:
            flash("Incorrect email or password")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
