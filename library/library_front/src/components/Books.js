import React from 'react'

const BookItem = ({item}) => {
    return (
        <tr>
            <th>{item.id}</th>
            <th>{item.name}</th>
            <th>{item.author.name}</th>
        </tr>
    )
}

const BookList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUTHOR</th>
            </tr>
            {items.map((item) => <BookItem item={item} />)}
        </table>
    )
}

export default BookList
