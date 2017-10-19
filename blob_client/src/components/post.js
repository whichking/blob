import React, { Component } from 'react'
import ReactMarkdown from 'react-markdown'

export function PostBody(props) {
    return(
        <div>
            <ReactMarkdown source={props.text}/>
        </div>
    )
}