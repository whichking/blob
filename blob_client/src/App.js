import React, { Component } from 'react';
import logo from './logo.svg';
import ReactMarkdown from 'react-markdown';
import './App.css';
import { getBlogPosts } from './api.js';
import { Tags } from "./components/tags"


let input = '# heading! \n\n**bold!** \n\n*italics!* \n\n![cow](http://www.healthbasics.net/wp-content/uploads/2015/07/cow-400x400.jpg "cow") \n\n```code block!```';


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {'posts': []};
    }
    componentWillMount() {
        getBlogPosts().then(posts => this.setState({'posts': posts}));
    }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
          <div>
              {this.state.posts.map(post => <p>{JSON.stringify(post)}</p>)}
          </div>
          <ReactMarkdown source={input} />
          <Tags tags={[{'id': 1, 'name': 'great_tag'}, {'id': 2, 'name': 'okay tag'}]} />
      </div>
    );
  }
}

export default App;
