from flask import Flask, render_template, request

app = Flask(__name__)


# ================= HOME =================

@app.route("/")
def home():
    return render_template("index.html")


# ================= LOGIN =================

@app.route("/login")
def login():
    return render_template("login.html")


# ================= DASHBOARD =================

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ================= SMART SEARCH =================

@app.route("/search")
def search():
    place = request.args.get("place", "CSE Lab")
    return render_template("search.html", place=place)


# ================= CAMPUS MAP =================

@app.route("/map")
def campus_map():
    return render_template("map.html")


# ================= NAVIGATION =================

@app.route("/navigation")
def navigation():
    place = request.args.get("place", "CSE Lab")
    return render_template("navigation.html", place=place)


# ================= LOCATION DETAILS =================

@app.route("/location-details")
def location_details():
    place = request.args.get("place", "CSE Lab")
    return render_template("location_details.html", place=place)


# ================= DEPARTMENTS =================

@app.route("/departments")
def departments():
    return render_template("departments.html")


# ================= FACILITIES =================

@app.route("/facilities")
def facilities():
    return render_template("facilities.html")


# ================= CAMPUS INFORMATION =================

@app.route("/information")
def information():
    return render_template("information.html")


# ================= EMERGENCY =================

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")


# ================= RUN APPLICATION =================

if __name__ == "__main__":
    app.run(debug=True)