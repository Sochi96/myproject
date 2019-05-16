from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/<userInputName>")
def hello_someone(userInputName):
	return render_template("hello.html", myname=userInputName.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    send_message(form_data["email"])
    return "All OK"

@app.route("/weather", methods=["POST"])
def weatherIn():
    form_data = request.form
    return weatherInCity(form_data["city"])

def send_message(email):
	print(email)
	return requests.post("https://api.mailgun.net/v3/sandbox6034c92187544ffcafd04b755931de3d.mailgun.org/messages",
        auth=("api", "94a9c795a5a820d5d1675e0430c17c84-e566273b-0da24ad2"),
        data={"from": "Excited User test1@gmail.com",
              "to": [email],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

def weatherInCity(city):
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": city, "units":"metric", "appid":"b11b2e54cafc8b93d89b381ef5fe11eb"}

	response = requests.get(endpoint, params=payload)

	print(response.url)
	print(response.status_code)
	print(response.headers["content-type"])
	return response.json



app.run(debug=True)
