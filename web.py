from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    link = "<h1>歡迎進入許芷嫙的網站首頁</h1>"
    link += "<a href=/mis>課程</a><hr>"
    link += "<a href=/today>今天日期</a><hr>"
    link += "<a href=/about>關於芷嫙</a><hr>"
    link += "<a href=/welcome?u=芷嫙&dep=靜宜資管>GET傳值</a><hr>"
    link += "<a href=/account>POST傳值(帳號密碼)</a><hr>"
    link += "<a href=/math>POST傳值(數字運算)</a><hr>"
    return link

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1><a href=/>回到網站首頁</a>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    now = year + "年" + month + "月" + day + "日"
    return render_template("today.html", datetime=now)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/welcome", methods=["GET"])
def welcome():
    x = request.values.get("u")
    y = request.values.get("dep")
    return render_template("welcome.html", name=x, dep=y)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/math", methods=["GET", "POST"])
def math():
    if request.method == "POST":
        a_str = request.form["a"] 
        opt = request.form["opt"]
        b_str = request.form["b"] 
        
        a = int(a_str)
        b = int(b_str)

        if opt == "/" and b == 0:
            return "除數不能為0"
        else:
            if opt == "+":
                Result = a + b
            elif opt == "-":
                Result = a - b
            elif opt == "*":
                Result = a * b
            elif opt == "/":
                Result = a / b

            result = f"{a} {opt} {b} 的結果是 {Result}"
            return result
    else:
        return render_template("math.html")

if __name__ == "__main__":
    app.run()