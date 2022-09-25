import  React from 'react';
import './App.css';
import AuthorList from './components/Author.js'
import axios from 'axios'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
        .then(response => {
            const authors = response.data
                this.setState(
                    {
                        'authors': authors,
                    }
                )
        }).catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <h3>
                    <strong>
                        Main app
                    </strong>
                </h3>
                <div>
		    <AuthorList authors={this.state.authors} />
                </div>
            </div>
        )
    }
}

export default App;