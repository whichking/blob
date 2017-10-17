import React, { Component } from 'react';



export function Tag(props) {
    return (
        <div>
            <a href={`/tags/${props.tag.id}`}>{props.tag.name}</a>
        </div>
    )
}




function Tags(props) {
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
            {props.tags.map((tag) => <Tag id={tag.id} name={tag.name}/>)}
        </div>
    )
}