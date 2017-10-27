import React, { Component } from 'react';
import logo from './logo.svg';
import ReactMarkdown from 'react-markdown';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import './App.css';
import { getBlogPosts } from './api.js';
import { Tags, TagContainer } from "./components/tags";
import { PostBody, Post, Posts, PostContainer } from "./components/post";
import { PostsView } from "./containers/posts"
import { TagsView } from "./containers/tags"


let input = '# heading! \n\n**bold!** \n\n*italics!* \n\n![cow](http://www.healthbasics.net/wp-content/uploads/2015/07/cow-400x400.jpg "cow") \n\n```code block!```';

let testPosts =
    [
        {
            'content': 'foo',
            'id': 1,
            'created': '01-01-1900',
            'tags': [
                {'id': 1, 'name': 'a tag'},
                {'id': 2, 'name': 'another tag'}
            ]
        },
        {
            'content': 'bar',
            'id': 2,
            'created': '01-02-1900',
            'tags': [
                {'id': 1, 'name': 'a tag'},
                {'id': 2, 'name': 'another tag'}
            ]
        }
    ];


class App extends Component {
    constructor(props) {
        super(props);
    }
  render() {
    return (
         <div className="App">
             <header className="App-header">
                 <img src={logo} className="App-logo" alt="logo" />
                 <h1 className="App-title">Welcome to React</h1>
             </header>
             <Router>
                 <PostsView />
                 <TagsView />
             </Router>
         </div>
    );
  }
}

export default App;
