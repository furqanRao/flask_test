from flask import Flask, jsonify, render_template, send_file, make_response, request
import random
from pathlib import Path
import traceback

# on windows use this command to run project "set FLASK_APP=project_file" and then this command "flask run"

# on mac or linux use this command to run project "export FLASK_APP=project_file" and then this command "flask run"


app = Flask(__name__)


@app.route('/main_page/')
def main_page():
    return render_template('index.html')


@app.route('/generate_random/')
def generate_random():
    strings = ["hi", "how-are-you", "developing-a", "random-generator", "flask-app-test", "for-a-remote-job",
               "sorry-for-delay", "in-submission"]
    alphanumerics = ["hi1298sir", "5345how-are-you3rwr23", "sf43develrweopi2343ng-a566",
                     "w3345random437-gener57ator7457", "f45lask-app-64564test", "f5464or-a456-remote465-job",
                     "9657sorry-for35-delay111", "in345-submissi43o55n"]
    count = 0
    while Path('output.txt').stat().st_size < 190000:
        real_number = random.uniform(10, 100000)
        integer = random.randint(10, 1000000)
        alpha_numeric = random.choice(alphanumerics)
        string_ = random.choice(strings)
        print(real_number, ",", integer, ",", alpha_numeric, ",", string_)
        file_ = open('output.txt', 'a')
        string_line = '\n' + str(real_number) + "," + str(integer) + "," + alpha_numeric + "," + string_
        file_.write(string_line)
        file_.close()
        count += 1
    # print("output is:----------- ", output)
    content = Path('output.txt').read_text()
    print("content is:----------- ", content)
    print("size is:----------- ", Path('output.txt').stat().st_size)
    if count != 0:
        resp = make_response(render_template('index.html'))
        resp.set_cookie('real_number', str(count))
        resp.set_cookie('integer', str(count))
        resp.set_cookie('alpha_numeric', str(count))
        resp.set_cookie('string_', str(count))
        return resp
    else:
        return render_template('index.html')


@app.route('/download')
def download_file():
    try:
        if Path('output.txt').stat().st_size < 200000:
            path = 'output.txt'
            return send_file(path, as_attachment=True)
        else:
            return render_template('index.html', message="Please generate random numbers before downloading file!")
    except:
        print(traceback.print_exc())
        return render_template('index.html', message="Please generate random numbers before downloading file!")


@app.route('/report/', methods=['POST', 'GET'])
def report():
    try:
        real_number = request.cookies.get('real_number')
        integer = request.cookies.get('integer')
        alpha_numeric = request.cookies.get('alpha_numeric')
        string_ = request.cookies.get('string_')
    except:
        return render_template('index.html', message="Please generate random numbers before getting report!")
    return render_template('index.html', real_number=real_number, integer=integer,
                           alpha_numeric=alpha_numeric, string_=string_)
