
import React from 'react'


const Comments = ({comments}) => {
	return (
		<div class="hero-body">
			<div className="card">
			{comments.map((comment)=> (
				<div className="card-body">
				<h6 className="card-title">{comment.date}</h6>
				<p className="card-title">{comment.comment}</p>
				</div>
			))}
			</div>
		</div>
	)
};
export default Comments

