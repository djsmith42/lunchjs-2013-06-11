import simplejson, flask

app = flask.Flask('Angular Slider Demo')

@app.route("/")
def _root():
    return open("index.html").read()

@app.route("/partials/<filename>")
def _partial(filename):
    return open("partials/{0}".format(filename)).read()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
