import "./styles.css";
import { useState } from "react";
import { Button } from "@material-ui/core";
import { Link } from "react-router-dom";

const Trade = () => {
  const [agua, setAgua] = useState(0);
  const [comida, setComida] = useState(0);
  const [remedio, setRemedio] = useState(0);
  const [municao, setMunicao] = useState(0);

  const [aguaUnit, comidaUnit, remedioUnit, municaoUnit] = [4, 3, 2, 1];
  const [aguaTotal, comidaTotal, remedioTotal, municaoTotal] = [
    agua * aguaUnit,
    comida * comidaUnit,
    remedio * remedioUnit,
    municao * municaoUnit,
  ];
  const total = aguaTotal + comidaTotal + remedioTotal + municaoTotal;

  const incAgua = () => {
    setAgua(agua + 1);
  };

  const decAgua = () => {
    if (agua === 0) {
      return;
    } else {
      setAgua(agua - 1);
    }
  };

  const incComida = () => {
    setComida(comida + 1);
  };

  const decComida = () => {
    if (comida === 0) {
      return;
    } else {
      setComida(comida - 1);
    }
  };

  const incRemedio = () => {
    setRemedio(remedio + 1);
  };

  const decRemedio = () => {
    if (remedio === 0) {
      return;
    } else {
      setRemedio(remedio - 1);
    }
  };

  const incMunicao = () => {
    setMunicao(municao + 1);
  };

  const decMunicao = () => {
    if (municao === 0) {
      return;
    } else {
      setMunicao(municao - 1);
    }
  };

  const handleSubmit = (e) => {
    setAgua(0);
    setComida(0);
    setMunicao(0);
    setRemedio(0);
  };

  let equalPoints = false;
  if (total === 20) {
    equalPoints = true;
  }

  return (
    <div className="trade-container">
      <h1>Escambo</h1>
      <h4>Faça aqui suas trocas</h4>
      <div className="trade-offer">
        <span>Sua oferta: {total}</span>
        <table>
          <thead>
            <tr>
              <th>Quantidade</th>
              <th>Item</th>
              <th>Pontos por item</th>
              <th>Total de pontos</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                {agua}
                <button
                  className="trade-input-button"
                  aria-label="aguaIncButton"
                  onClick={incAgua}
                >
                  +
                </button>
                <button
                  className="trade-input-button"
                  aria-label="aguaDecButton"
                  onClick={decAgua}
                >
                  -
                </button>
              </td>
              <td>Água</td>
              <td>{aguaUnit}</td>
              <td>{aguaTotal}</td>
            </tr>
            <tr>
              <td>
                {comida}
                <button
                  className="trade-input-button"
                  aria-label="comidaIncButton"
                  onClick={incComida}
                >
                  +
                </button>
                <button
                  className="trade-input-button"
                  aria-label="comidaDecButton"
                  onClick={decComida}
                >
                  -
                </button>
              </td>
              <td>Comida</td>
              <td>{comidaUnit}</td>
              <td>{comidaTotal}</td>
            </tr>
            <tr>
              <td>
                {remedio}
                <button
                  className="trade-input-button"
                  aria-label="remedioIncButton"
                  onClick={incRemedio}
                >
                  +
                </button>
                <button
                  className="trade-input-button"
                  aria-label="remedioDecButton"
                  onClick={decRemedio}
                >
                  -
                </button>
              </td>
              <td>Remédio</td>
              <td>{remedioUnit}</td>
              <td>{remedioTotal}</td>
            </tr>
            <tr>
              <td>
                {municao}
                <button
                  className="trade-input-button"
                  aria-label="municaoIncButton"
                  onClick={incMunicao}
                >
                  +
                </button>
                <button
                  className="trade-input-button"
                  aria-label="municaoDecButton"
                  onClick={decMunicao}
                >
                  -
                </button>
              </td>
              <td>Munição</td>
              <td>{municaoUnit}</td>
              <td>{municaoTotal}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div className="trade-return">
        <span>Seu retorno: 20</span>
        <table>
          <tbody>
            <tr>
              <th>Quantidade</th>
              <th>Item</th>
              <th>Pontos por item</th>
              <th>Total de pontos</th>
            </tr>
            <tr>
              <td>1</td>
              <td>Água</td>
              <td>4</td>
              <td>4</td>
            </tr>
            <tr>
              <td>2</td>
              <td>Comida</td>
              <td>3</td>
              <td>6</td>
            </tr>
            <tr>
              <td>3</td>
              <td>Remédio</td>
              <td>2</td>
              <td>6</td>
            </tr>
            <tr>
              <td>4</td>
              <td>Munição</td>
              <td>1</td>
              <td>4</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div className="trade-button">
        <Button
          variant="contained"
          color="primary"
          onClick={handleSubmit}
          disabled={!equalPoints}
        >
          Atualizar
        </Button>
      </div>
      <Link to="/">
        <div className="trade-button">
          <Button variant="contained" color="primary">
            Voltar
          </Button>
        </div>
      </Link>
    </div>
  );
};

export default Trade;
