import mysql.connector

import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin



app = flask.Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

@app.route('/api/v1/resources/courses/<id>', methods=['GET'])
@cross_origin()
def get_course(id):
    print( "Ass")
    print(request.get_data())
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

@app.route('/api/v1/resources/comments/<id>', methods=['GET', 'POST'])
def comments(id):
    comments = []
    if request.method == 'POST':
        courseID = request.form['id']
        comment = request.form['comment']
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
app.run(host='0.0.0.0')
