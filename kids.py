from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import random, time, random_word

# initialize a flask application (app)
app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')  # Allow all origins (*)

# ... your existing Flask
test_data={}
rand = 0
# add an api endpoint to flask app
  
@app.route('/api/data', methods=["GET"])
def get_data():
    global test_data
    global rand
    global start
    dictionary = open("words.txt", "r")
    temp = dictionary.readlines()
    dictionary.close()
    listwords = []
    for i in temp:
        listwords.append(i.strip())
    start = time.perf_counter()
    test_data = []
    usedlist = []
    while True:
        temp2 = random.randint(0, len(listwords))
        print(temp2)
        if temp2 not in usedlist:
            usedlist.append(temp2)
            test_data.append(listwords[temp2])
        if len(test_data) == 50:
            break
    rand = random.randint(0,len(test_data)-1)
    temp3 = ''
    for i in test_data:
        temp3 += i + ' '
    return (temp3+render_template('wtf.md'))

@app.route('/inputdata', methods=["POST"])
def inputdata():
    html_content = """<html>
    <head>
        <title>Hellox</title>
    </head>
    <body>
    <style>
    .headerbutton {
    border: 1px solid #5f73b8;
    background: #424549;
    color: white;
    width: 270px;
    padding: 15px 20px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 15px;
    transition-duration: 0.1s;
    cursor: pointer;
    font-family: serif;
    }
    .headerbutton:hover{
    background:  #7e92d6;
    /* color: rgb(78, 3, 66); */
    }
    body {
    text-align: center;
    padding: 25px;
    background-color: #121212;
    color: #7e92d6;
    font-size: 24px;
    font-weight: bold;
    transition-duration: 0.2s;
   }
    </style>
    <button id="border"type="button" class="headerbutton" onclick="window.location.href='/api/data';">Do the test again</button> <br \>  
    </body>
    </html>"""
    print(test_data[rand])
    words = request.form['a']
    end = time.perf_counter();
    totalTime = end - start;
    print("Completed in " + str(totalTime) + " seconds");
    print(words);
    total = 0;
    word = words
    words = words.split();
    data = test_data;
    all = min(len(words), len(data))
    untotal = 0

    for i in words:
        if i not in data:
            untotal += 1
    print(untotal)

    total = all - untotal
    print("WPM: " + str(total/(totalTime)*60));
    try:
        print("Accuracy: " + str(total/all*100)+ "%")
    except:
        pass;
    html_content += "<br> <br><br>"
    html_content+= "Accuracy: " + str((total/all*100)//1)+ "%" + '\n'
    html_content += "WPM: " + str((total/(totalTime)*60)//1) + '\n'
    return html_content


# add an HTML endpoint to flask app
@app.route('/')
def say_hello():
    return render_template('main.md')
if __name__ == '__main__':
    # starts flask server on default port, http://127.0.0.1:5001
    app.run(port=5001)
