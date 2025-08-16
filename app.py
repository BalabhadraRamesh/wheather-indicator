import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "your_api_key_here"   # Replace with your OpenWeather API key

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if data.get("main"):
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title()
            }
        else:
            weather = {"error": "City not found!"}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
