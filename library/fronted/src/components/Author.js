import React from 'react'



const AuthorItem = ({author}) => {
    return (
        <tr>
            <td class='col-6'>
                 {author.first_name}
            </td>
            <td class='col-6'>
                 {author.last_name}
            </td>
            <td class='col-3'>
                 {author.birthday_year}
            </td>
        </tr>
    )
}


const AuthorList =  ({authors}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}

export default AuthorList;