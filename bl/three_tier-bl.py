import mysql.connector

import flask
from flask import request, jsonify
from flask_cors import CORS



app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.route('/api/v1/resources/courses/all', methods=['GET'])
def api_all():
    # make a request to the database here.
    # For now, use fake data for debug

    courses = []
    
    try:
        cnx = mysql.connector.connect(user='root', password='password', host='db', database='courses', port=3306);

        query = "SELECT * FROM courses"
        cursor= cnx.cursor()
        cursor.execute(query)
        for (id, name, rating, numratings, comments)  in cursor:
            courses.append({'id': id, 'name': name, 'rating': rating, 'numratings': numratings, 'comments': comments})
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.close()


    return jsonify(courses)

app.run(host='0.0.0.0')
