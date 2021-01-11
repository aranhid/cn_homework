from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://i.giphy.com/media/3o6Zt481isNVuQI1l6/source.gif",
    "https://i.giphy.com/media/vFKqnCdLPNOKc/source.gif",
    "https://i.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif",
    "https://i.giphy.com/media/q1MeAPDDMb43K/giphy.gif",
    "https://i.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif",
    "https://i.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif",
    "https://i.giphy.com/media/13CoXDiaCcCoyk/giphy.gif",
    "https://i.giphy.com/media/Lq0h93752f6J9tijrh/giphy.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")