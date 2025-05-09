
# app.py

from flask import Flask
app= Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from Docker From kubernetes!<h1><p>Let me see if the changes have gone through v2 this are new</p><p>This is the new line added </p>"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)

