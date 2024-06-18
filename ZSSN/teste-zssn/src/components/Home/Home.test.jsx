import Home from ".";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { BrowserRouter as Router } from "react-router-dom";
import { createMemoryHistory } from "history";

describe("<Home />", () => {
  test("renders Zombie Survival Social Network", () => {
    render(
      <Router>
        <Home />
      </Router>
    );

    expect(
      screen.getByText(/Zombie Survival Social Network/i)
    ).toBeInTheDocument();
  });

  //   test("redirects to /localizacao route", () => {
  //     const history = createMemoryHistory();

  //     render(
  //       <Router history={history}>
  //         <Home />
  //       </Router>
  //     );

  //     const localizationDiv = screen.getByText(/Localização/i);
  //     const leftClick = { button: 0 };
  //     userEvent.click(localizationDiv, leftClick);
  //     expect(screen.getByText(/Atualize sua localização/i)).toBeInTheDocument();
  //   });
});
