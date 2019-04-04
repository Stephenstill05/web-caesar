from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/rotate" method="POST" />
        
            <label>
                Rotate by:
                <input type="text" name="rot" value="0"/>
            </label>

            <br>
            <label>
                <textarea name="text"></textarea>
            </label>
            <br>
            <input type="submit" Value="Submit"/>
        </form>

    </body>
</html>
"""


@app.route("/")
def index():
    return form

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


@app.route("/rotate", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']


    rot_error=''
    if not is_integer(rot):
        rot_error='Not a valid integer'
    else:
        rot=int(rot)

    if not rot_error:
        return "<h1>"+rotate_string(text,rot)+"</h1>"
    else:
        return form.format(rot_error=rot_error)

app.run()