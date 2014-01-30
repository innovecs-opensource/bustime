from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    data = ""
    try:
    with open("schedule.json", "r") as myfile:
        data=myfile.read()
    except Exception, e:
    print "Exception: ", e
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0')
