import React, {Component} from 'react';
import Comments from './comments';

export default class ViewCourse extends Component {
	state = {
                courses: [],
		comments: []
        }
        // This is the mechanism to make the rest call
        componentDidMount() {

                fetch('http://' + process.env.REACT_APP_PUB_IP + ':5001/api/v1/resources/courses/' + this.props.match.params.id)
                .then(res => res.json())
                .then((data) => {
                        this.setState({ courses: data })
                })
                .catch(console.log)

                fetch('http://' + process.env.REACT_APP_PUB_IP + ':5001/api/v1/resources/comments/' + this.props.match.params.id)
                .then(res => res.json())
                .then((data) => {
                        this.setState({ comments: data })
                })
                .catch(console.log)
        }

	render() {
	return (
		<div>
		<div>
		<center><h1 class="title">{this.state.courses[0]}</h1></center>
		</div>
		<Comments comments = {this.state.comments} />
		</div>
	)
	}

}
