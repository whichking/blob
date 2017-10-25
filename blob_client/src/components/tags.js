import React, { Component } from 'react';
import {getTags} from "../api";



function Tag(props) {
    return (
        <div>
            <a href={`/tags/${props.tag.id}`}>{props.tag.name}</a>
        </div>
    )
}




export function Tags(props) {
    const divStyle = {display: "flex"};
    if (!("direction" in props) || (props.direction === "horizontal")) {
        divStyle.flexFlow = "row wrap"
    }
    else if (props.direction === "vertical") {
        divStyle.flexFlow = "column"
    }
    else {
        throw "Invalid direction"
    }

    return(
        <div style={divStyle}>
            {props.tags.map((tag) => <Tag tag={{'id':tag.id, 'name':tag.name}}/>)}
        </div>
    )
}


export class TagContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {tags: []}
    }
    componentWillMount() {
        getTags().then(tags => this.setState({tags: tags}));
    }
    render() {
        return (
            <Tags tags={this.state.tags}/>
        )
    }
}