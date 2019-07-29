from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
async def Index(request, path=""):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port = 3000, debug = True)