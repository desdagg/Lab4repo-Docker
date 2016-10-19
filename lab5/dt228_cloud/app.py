from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Index File\n"

@app.route("/hello")
def hi():
	return "hello\n"

@app.route("/user/<username>")
def user(username):
	return 'user %s \n' % username

@app.route("/post/80")
def post():
	return "Post 80\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

