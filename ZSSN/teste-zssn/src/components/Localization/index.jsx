import "./styles.css";
import { Button } from "@material-ui/core";
import { useState } from "react";
import { Link } from "react-router-dom";

const Localization = () => {
  const [oldLat, setOldLat] = useState(545);
  const [oldLng, setOldLng] = useState(232);
  const [currentLat, setCurrentLat] = useState("");
  const [currentLng, setCurrentLng] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    setOldLat(currentLat);
    setOldLng(currentLng);
    setCurrentLng("");
    setCurrentLat("");
  };

  return (
    <div className="localization-container">
      <h1>Localização</h1>
      <h4>Atualize sua localização informando latitude e longitude</h4>
      <div className="localization-input-container">
        <div className="localization-old">
          <p>Antiga</p>
          <input type="number" value={oldLat} disabled />
          <br />
          <br />

          <input type="number" value={oldLng} disabled />
        </div>
        <div className="localization-current">
          <p>Atual </p>

          <input
            type="number"
            value={currentLat}
            onChange={(e) => setCurrentLat(e.target.value)}
            placeholder="Latitude"
          />
          <br />
          <br />
          <input
            type="number"
            value={currentLng}
            onChange={(e) => setCurrentLng(e.target.value)}
            placeholder="Longitude"
          />
        </div>
      </div>
      <div className="localization-button">
        <Button variant="contained" color="primary" onClick={handleSubmit}>
          Atualizar
        </Button>
      </div>
      <Link to="/">
        <div className="localization-button">
          <Button variant="contained" color="primary">
            Voltar
          </Button>
        </div>
      </Link>
    </div>
  );
};

export default Localization;
