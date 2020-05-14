import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Main } from "./components/Main";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="pageContainer">
        <nav>
          <a href="/">
            <h1>
              When&nbsp;to&nbsp;shop&nbsp;
              <span role="img" aria-label="mask emoji">
                😷
              </span>
            </h1>
          </a>
        </nav>
        <Switch>
          <Route exact path="/">
            <Main />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
