import React from 'react'
import { PostContainer } from "../components/post"

export function PostsView(props) {
    return (
        <div>
            <PostContainer />
        </div>
    )
}

export const PostView = ({ match }) => (

    <div>
        <h3>ID: {match.params.id}</h3>
    </div>
)