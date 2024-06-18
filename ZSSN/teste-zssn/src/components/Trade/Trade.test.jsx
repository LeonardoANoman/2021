import Trade from ".";
import { screen, render } from "@testing-library/react";
import { BrowserRouter as Router } from "react-router-dom";
import userEvent from "@testing-library/user-event";

describe("<Trade />", () => {
  test("renders Escambo", () => {
    render(
      <Router>
        <Trade />
      </Router>
    );

    expect(screen.getByText(/Escambo/i)).toBeInTheDocument();
  });
  test("checks if every inc and dec button works", () => {
    render(
      <Router>
        <Trade />
      </Router>
    );

    const aguaIncButton = screen.getByLabelText(/aguaIncButton/i);
    const aguaDecButton = screen.getByLabelText(/aguaDecButton/i);
    userEvent.click(aguaIncButton);
    userEvent.click(aguaIncButton);
    expect(screen.getByText(/Sua oferta: 8/i)).toBeInTheDocument();
    userEvent.click(aguaDecButton);
    expect(screen.getByText(/Sua oferta: 4/i)).toBeInTheDocument();
    userEvent.click(aguaDecButton);
    userEvent.click(aguaDecButton);
    expect(screen.getByText(/Sua oferta: 0/i)).toBeInTheDocument();

    const comidaIncButton = screen.getByLabelText(/comidaIncButton/i);
    const comidaDecButton = screen.getByLabelText(/comidaDecButton/i);
    userEvent.click(comidaIncButton);
    userEvent.click(comidaIncButton);
    expect(screen.getByText(/Sua oferta: 6/i)).toBeInTheDocument();
    userEvent.click(comidaDecButton);
    expect(screen.getByText(/Sua oferta: 3/i)).toBeInTheDocument();
    userEvent.click(comidaDecButton);
    userEvent.click(comidaDecButton);
    expect(screen.getByText(/Sua oferta: 0/i)).toBeInTheDocument();

    const remedioIncButton = screen.getByLabelText(/remedioIncButton/i);
    const remedioDecButton = screen.getByLabelText(/remedioDecButton/i);
    userEvent.click(remedioIncButton);
    userEvent.click(remedioIncButton);
    expect(screen.getByText(/Sua oferta: 4/i)).toBeInTheDocument();
    userEvent.click(remedioDecButton);
    expect(screen.getByText(/Sua oferta: 2/i)).toBeInTheDocument();
    userEvent.click(remedioDecButton);
    userEvent.click(remedioDecButton);
    expect(screen.getByText(/Sua oferta: 0/i)).toBeInTheDocument();

    const municaoIncButton = screen.getByLabelText(/municaoIncButton/i);
    const municaoDecButton = screen.getByLabelText(/municaoDecButton/i);
    userEvent.click(municaoIncButton);
    userEvent.click(municaoIncButton);
    expect(screen.getByText(/Sua oferta: 2/i)).toBeInTheDocument();
    userEvent.click(municaoDecButton);
    expect(screen.getByText(/Sua oferta: 1/i)).toBeInTheDocument();
    userEvent.click(municaoDecButton);
    userEvent.click(municaoDecButton);
    expect(screen.getByText(/Sua oferta: 0/i)).toBeInTheDocument();
  });

  test("clears input when updated", () => {
    render(
      <Router>
        <Trade />
      </Router>
    );

    const aguaIncButton = screen.getByLabelText(/aguaIncButton/i);
    const atualizarButton = screen.getByText(/atualizar/i);

    // click event is fired 5 times so offered === return

    userEvent.click(aguaIncButton);
    userEvent.click(aguaIncButton);
    userEvent.click(aguaIncButton);
    userEvent.click(aguaIncButton);
    userEvent.click(aguaIncButton);

    userEvent.click(atualizarButton);
    expect(screen.getByText(/Sua oferta: 0/i)).toBeInTheDocument();
  });
});
