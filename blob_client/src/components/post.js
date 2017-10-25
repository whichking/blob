import React, { Component } from 'react'
import ReactMarkdown from 'react-markdown'
import { Tags } from './tags.js'
import { getBlogPosts } from '../api.js'

export function PostBody(props) {
    return (
        <div>
            <ReactMarkdown source={props.text}/>
        </div>
    )
}




export function Post(props) {
    /*
    expected props:
        * post: a blog post object, example:

    Example:
    {
        'content': 'foo',
        'id': 1,
        'created': '01-01-1900',
        'tags': [
            {'id': 1, 'name': 'a tag'},
            {'id': 2, 'name': 'another tag'}
        ]
    };
    */
    return (
        <div>
            <PostBody text={props.post.content} />
            <Tags tags={props.post.tags} />
        </div>
    )
}


export function Posts(props) {
    const divStyle = {display: "flex", flexFlow: "column"};
    debugger
    return (
       <div style={divStyle}>
           {props.posts.map((post) => <Post post={{'content':post.content, 'tags':post.tags}}/>)}
       </div>
   )
}


export class PostContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {posts: []}
    }
    componentWillMount() {
        getBlogPosts().then(posts => this.setState({posts: posts}));
    }
    render() {
        return (
            <Posts posts={this.state.posts} />
        );
    }
}
