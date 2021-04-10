
import ViewCourse from './ViewCourse';
import React from 'react'
import { Route, Link} from "react-router-dom";



function ViewCourseLink(course) {
	function handleClick(e) {
		e.preventDefault();
		console.log('Class was clicked.');
	}
	return (
		<Link to={"/course/"+course.id} >{course.name}</Link>
	);
}

const Courses = ({ courses }) => {
	return (
		<div>
		<center><h1 class="title">Company EDL</h1></center>
		<div class="hero-body">
		{courses.map((course) => (
			<div className="card">
			<div className="card-header">
			{ViewCourseLink(course)}
			</div>

			<div className="card-body">
			<h6 className="card-title">Rating: {course.rating}/5</h6>
			<h6 className="card-title">{course.numratings} ratings</h6>
			<p className="card-title">{course.comments}</p>
			</div>
			</div>
		))}
		</div>
		</div>
	)
};
export default Courses

