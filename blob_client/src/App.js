import React, { Component } from 'react';
import logo from './logo.svg';
import ReactMarkdown from 'react-markdown';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import './App.css';
import { getBlogPosts } from './api.js';
import { Tags, TagContainer } from "./components/tags";
import { PostBody, Post, Posts, PostContainer } from "./components/post";
import { PostsView, PostView } from "./containers/posts"
import { TagsView, TagView } from "./containers/tags"


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
                 <div>
                     <ul>
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/posts">Posts</Link></li>
                        <li><Link to="/tags">Tags</Link></li>
                         <li><Link to="/tags/1">Tag1</Link></li>
                     </ul>

                     <Route exact path="/" component={PostsView}/>
                     <Route path="/posts" component={PostsView}/>
                     <Route path="/tags" component={TagsView}/>
                     <Route path="tags/:id" component={TagView}/>
                     <Route path="posts/:id" component={PostView}/>
                 </div>
             </Router>
         </div>
    );
  }
}

export default App;
