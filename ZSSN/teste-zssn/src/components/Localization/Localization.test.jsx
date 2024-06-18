import Localization from ".";
import { screen, render, fireEvent } from "@testing-library/react";
import { BrowserRouter as Router } from "react-router-dom";
import userEvent from "@testing-library/user-event";

describe("<Localization />", () => {
  test("renders Localização", () => {
    render(
      <Router>
        <Localization />
      </Router>
    );

    expect(
      screen.getByRole("heading", { name: "Localização" })
    ).toBeInTheDocument();
  });

  test("clears input after updating", () => {
    render(
      <Router>
        <Localization />
      </Router>
    );

    const currentLat = screen.getByPlaceholderText(/Latitude/i);
    const currentLng = screen.getByPlaceholderText(/Longitude/i);
    const valueLat = "327";
    const valueLng = "874";
    const uptadeButton = screen.getByText(/atualizar/i);

    fireEvent.change(currentLat, { target: { value: valueLat } });
    expect(currentLat.value).toMatch(valueLat);
    fireEvent.change(currentLng, { target: { value: valueLng } });
    expect(currentLng.value).toMatch(valueLng);
    userEvent.click(uptadeButton);

    expect(currentLat.value).toBe("");
    expect(currentLng.value).toBe("");
  });
});
