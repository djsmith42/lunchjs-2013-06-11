import simplejson, flask

app = flask.Flask('Angular Slider Demo')

@app.route("/")
def _root():
    return open("index.html").read()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
