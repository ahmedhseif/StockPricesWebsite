from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request
import requests

API_KEY = "bdccb7d37bbdb0b238dc697356b4aa3b"
app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/prices', methods=["GET", "POST"])
def prices():

    symbol = request.form['symbol']
    parameters = {
        "symbols": symbol
    }
    response = requests.get(f"http://api.marketstack.com/v1/eod?access_key={API_KEY}", params=parameters)
    response.raise_for_status()
    data = response.json()
    price_data = data["data"]
    header = ["Open", "High", "Low", "Close", "Volume", "Adj_High", "Adj_Low", "Adj_Close", "Adj_Open", "Adj_Volume",
              "Split_Factor", "Dividend", "Exchange", "Date"]
    return render_template('prices.html', prices=price_data, header=header)


if __name__ == '__main__':
    app.run(debug=True)