import "bulma";
import React, {Component} from 'react';
import Courses from './courses';

class App extends Component {
	state = {
		courses: []
	}
	// This is the mechanism to make the rest call
	componentDidMount() {
		fetch('http://' + process.env.REACT_APP_PUB_IP + ':5001/api/v1/resources/courses/all')
		.then(res => res.json())
		.then((data) => {
			this.setState({ courses: data })
		})
		.catch(console.log)
	}
	render() {
		console.log(this.state.courses)
		return(
			<Courses courses={this.state.courses} />
		)
	}
}

export default App;
