import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

/*
read react docs and go through tutorials 
Li's udemy videos

*/
const Header = props => { 
  return <h1>{props.title}</h1>
 }

class ControlledForm extends Component {
	constructor( props ) {
		super(props);
		this.state = { name:'', color:''};
		this.handleNameChange = this.handleNameChange.bind(this);
		this.handleColorChange = this.handleColorChange.bind(this);
	}

	handleNameChange( event ) { 
		this.setState({ name:event.target.value });
		console.log(`name changed to: ${event.target.value}`);
	}

	handleColorChange( event ) {
		this.setState({ color:event.target.value });
		console.log(`color changed to: ${event.target.value}`);
		document.querySelector(".result").style.background = event.target.value;
	}




	render() {
		return (
			// everything goes here
			<div className='Container'>
			<form> 
				<input type="text" placeholder="Name" value={this.state.name} onChange={this.handleNameChange} />
				<br />
				<input type="text" placeholder="Favorite Color" value={this.state.color} onChange={this.handleColorChange} />
			</form>
			<Result color={this.state.color} name={this.state.name} />
			</div> 
		);
	}
}

const Result = props => { 
	//name will make Header 'Name's' controlled form
	//color will make header and result div change color
	return <div className="result" style={{background:props.color}}>{props.name}</div>
} 

class App extends Component {
  render() {
    return (
      <div className="App">
        <Header title="Controlled Form"/>
      	<ControlledForm />
      </div>
    );
  }
}

export default App;
