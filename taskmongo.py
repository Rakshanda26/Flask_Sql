from flask import Flask,request

app = Flask(__name__)

@app.route("/testfun")
def test():
    return  "this is my first function for get "

if __name__ == "__main__":
    app.run(port= 5002)