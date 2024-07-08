from flask import Flask,render_template
from employees import employees_data
# create the flask app
app = Flask(__name__)
# __ is called DUNDER.

# home page
@app.route("/") #setting endpoint
@app.route("/home") #for the same funtion we can have multiple routes.
def home():
	return render_template("home.html", title="Home")

@app.route("/signup", methods=["GET","POST"])
def signup():
	form = SignupForm()
	return render_template("signup.html", title="Sign Up", form=form)

# about page
@app.route("/about") #setting endpoint
def about():
	return render_template("about.html", title="About")

# employee page
@app.route("/employees")
def employees():
	return render_template(
		"employees.html",
		title="Employees",
		emps=employees_data
	)

@app.route("/employees/managers")
def managers():
	return render_template(
		"managers.html",
		title="Managers",
		emps=employees_data
	)


# start the app
if __name__ == "__main__":
	app.run(debug=True)