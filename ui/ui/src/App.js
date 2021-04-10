import "bulma";
import React, {Component} from 'react';
import Courses from './courses';


class CourseBox extends Component {
  constructor(props) {
    super(props);
          console.log(props);
    this.state = {
      inputValue: ''
    };
  }

  render() {
    return (
            <div>
            <input value={this.state.inputValue} onChange={evt => this.updateInputValue(evt)}/><br/>
            <button type="button" onClick={e =>this.handleClick(e)}>Submit</button>
            </div>
    );
  }


  updateInputValue(evt) {
    this.setState({
      inputValue: evt.target.value
    });
  }
  handleClick(e) {
                console.log(this.state.inputValue);
                fetch('http://' + process.env.REACT_APP_PUB_IP + ':5001/api/v1/resources/course/', {method:"POST", headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin' : 'application/json'}, body: JSON.stringify({course: this.state.inputValue})})
                .catch(console.log)
        }
};


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
			<div>
			<Courses courses={this.state.courses} />
			Add course:
			<CourseBox />
			</div>
		)
	}
}

export default App;
