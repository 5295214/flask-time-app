from flask import Flask, render_template
from datetime import datetime
import os
import pytz
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # 设置北京时间
    tz = pytz.timezone("Asia/Shanghai")
    now = datetime.now(tz)
    weekday_map = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%Y-%m-%d")
    weekday_str = weekday_map[now.weekday()]

    # 获取天气信息（以北京为例）
    city = "Beijing"
    api_key = "3b89404d432736981e6df7d4e8cf9edd"  # <- 请替换为你自己的 API KEY
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=zh_cn"

    try:
        response = requests.get(weather_url, timeout=3)
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        weather_info = f"{city}：{weather}，{temp:.1f}℃"
    except:
        weather_info = "天气信息获取失败"

    return render_template("index.html",
                           time=time_str,
                           date=date_str,
                           weekday=weekday_str,
                           weather=weather_info)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
