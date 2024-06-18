import "./App.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Trade from "./components/Trade";
import Localization from "./components/Localization";
import Home from "./components/Home";

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact>
          <Home />
        </Route>
        <Route path="/localizacao" exact>
          <Localization />
        </Route>
        <Route path="/escambo" exact>
          <Trade />
        </Route>
      </Switch>
    </Router>
  );
};

export default App;
