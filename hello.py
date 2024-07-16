#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<div style=background:pink> <h1><center><i>Hello World</i></center></h1><br><h1><i>Hai..!</i></h1></div>"
if __name__=='__main__':
    app.run(debug=True)