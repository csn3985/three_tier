import mysql.connector

import flask
from flask import request, jsonify, redirect, url_for
from flask_cors import CORS, cross_origin



app = flask.Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

@app.route('/api/v1/resources/courses/<id>', methods=['GET'])
@cross_origin()
def get_course(id):
    courseID = id
    data = []
    try:
        cnx = mysql.connector.connect(user='root', password='password', host='db', database='courses', port=3306);

        query = "SELECT * FROM courses WHERE ID=" + courseID
        cursor= cnx.cursor()
        cursor.execute(query)
        for (id, name, rating, numratings) in cursor:
            data.append(name)
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.close()
    return jsonify(data)

@app.route('/api/v1/resources/course/', methods=['POST'])
@cross_origin()
def add_course():
    course = request.json['course']
    try:
        cnx = mysql.connector.connect(user='root', password='password', host='db', database='courses', port=3306);

        query = "INSERT INTO courses(NAME, RATING, NUMRATINGS) VALUES('" + course + "', 0, 0)"
        cursor= cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cursor= cnx.cursor()
        query = "SELECT * FROM courses";
        cursor.execute(query)

        courses = []

        for (id, name, rating, numratings) in cursor:
            courses.append({'name': name})
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.close()
    return jsonify(courses)

@app.route('/api/v1/resources/rating/', methods=['POST'])
@cross_origin()
def add_rating():
    comments = []
    courseID = request.json['id']
    rating = request.json['rating']
    
    if not rating.isnumeric():
        return jsonify({'status': 'False'})
    if float(rating) < 0 or float(rating) > 5:
        return jsonify({'status': 'True'})
    
    rating = float(rating)

    try:
        cnx = mysql.connector.connect(user='root', password='password', host='db', database='courses', port=3306);
        cursor= cnx.cursor()
        query = "SELECT * FROM courses WHERE ID=" + courseID
        cursor.execute(query)
        numratings = 0
        oldrating = 0
        for (_, _, rating_, numrating_) in cursor:
            numratings = numrating_
            oldrating = rating_
        print(oldrating, numratings)
        cnx.commit()
        query = "UPDATE courses set RATING = " + str((numratings*oldrating+rating)/(numratings+1))  + ", NUMRATINGS = " + str(numratings+1) + " WHERE ID=" + courseID
        cursor.execute(query)
        cnx.commit()

        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.close()

    return jsonify({'status': 'True'})

@app.route('/api/v1/resources/courses/all', methods=['GET'])
def api_all():
    courses = []    
    try:
        cnx = mysql.connector.connect(user='root', password='password', host='db', database='courses', port=3306);
        query = "SELECT * FROM courses"
        cursor= cnx.cursor()
        cursor.execute(query)
        for (id, name, rating, numratings)  in cursor:
            courses.append({'id': id, 'name': name, 'rating': rating, 'numratings': numratings})
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.close()
    return jsonify(courses)

@app.route('/api/v1/resources/comments/<id>', methods=['GET'])
def comments(id):
    comments = []
    if request.method == 'GET':
        courseID = id
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='db', database='courses', port=3306);

            cursor= cnx.cursor()
            query = "SELECT * FROM comments WHERE COURSE_ID=" + courseID
            cursor.execute(query)

            comments = []

            for (id, course_id, comment, date)  in cursor:
                comments.append({'date': date, 'comment': comment})

            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(err)
        else:
            cnx.close()

        return jsonify(comments)
@app.route('/api/v1/resources/comments/', methods=['POST'])
def post_comment():
    comments = []
    courseID = request.json['id']
    comment = request.json['comment']
    try:
        cnx = mysql.connector.connect(user='root', password='password', host='db', database='courses', port=3306);

        query = "INSERT INTO comments(COURSE_ID, COMMENT) VALUES(" + courseID + ", '" + comment + "')"
        cursor= cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cursor= cnx.cursor()
        query = "SELECT * FROM comments WHERE COURSE_ID=" + courseID
        cursor.execute(query)

        comments = []

        for (id, course_id, comment, date)  in cursor:
            comments.append({'date': date, 'comment': comment})
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.close()
    return jsonify(comments)
app.run(host='0.0.0.0')
