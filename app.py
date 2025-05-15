from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    weekday_map = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%Y-%m-%d")
    weekday_str = weekday_map[now.weekday()]

    return render_template("index.html", time=time_str, date=date_str, weekday=weekday_str)

if __name__ == "__main__":
    app.run(debug=True)
