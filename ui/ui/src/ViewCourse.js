import React, {Component} from 'react';

export default class ViewCourse extends Component {
	render() {
	return (
		<div>
		<p>test viewing a course</p>
		<p>{this.props.match.params.id}</p>
		</div>
	)
	}

}
