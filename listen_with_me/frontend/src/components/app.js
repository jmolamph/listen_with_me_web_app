import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    // renders the html on the page
    render() {
        return ( <div>
            <HomePage />
        </div>
        );
    }
}

// render App component in the div
const appDiv = document.getElementById("app");
render(<App />, appDiv);
