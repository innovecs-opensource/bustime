from flask import Flask
app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/schedule")
def schedule():
    data = ""
    try:
        with open("schedule.json", "r") as myfile:
            data=myfile.read()
    except Exception, e:
        data = 'Exception in schedule: {}'.format(e.msg)
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0')
