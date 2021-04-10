import React, {Component} from 'react';
import Comments from './comments';


class RatingBox extends Component {
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
                fetch('http://' + process.env.REACT_APP_PUB_IP + ':5001/api/v1/resources/rating/', {method:"POST", headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin' : 'application/json'}, body: JSON.stringify({id: this.props.id, rating: this.state.inputValue})})
                .catch(console.log)
	}
};

class CommentBox extends Component {
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
                fetch('http://' + process.env.REACT_APP_PUB_IP + ':5001/api/v1/resources/comments/', {method:"POST", headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin' : 'application/json'}, body: JSON.stringify({id: this.props.id, comment: this.state.inputValue})})
                .catch(console.log)
	}
};

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
		<div>
		<Comments comments = {this.state.comments} />
		Add Comment:
		<CommentBox id={this.props.match.params.id}/>
		Add Rating:
		<RatingBox id={this.props.match.params.id}/>
		</div>
		</div>
	)
	}

}
