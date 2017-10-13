import React, { Component } from 'react';



export function Tag(props) {
    return (
        <div>
            <a href={`/tags/${props.tag.id}`}>{props.tag.name}</a>
        </div>
    )
