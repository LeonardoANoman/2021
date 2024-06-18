import "./styles.css";

import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="home-container">
      <h1>Zombie Survival Social Network</h1>
      <div className="home-links-container">
        <Link to="/localizacao">
          <div className="home-localization-container">
            <span>Localização</span>
          </div>
        </Link>
        <Link to="/escambo">
          <div className="home-trade-container">
            <span>Escambo</span>
          </div>
        </Link>
      </div>
    </div>
  );
};

export default Home;
