import React from 'react'
import { TagContainer } from "../components/tags"

export function TagsView(props) {
    return (
        <div>
            <TagContainer />
        </div>
    )
}

export const TagView = ({ match }) => (
    <div>
        <h3>ID: {match.params.id}</h3>
    </div>
);
