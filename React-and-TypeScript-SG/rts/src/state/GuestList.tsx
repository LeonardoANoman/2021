import { useState } from "react";

const GuestList: React.FC = () => {
  const [name, setName] = useState("");
  const [guest, setGuests] = useState<string[]>([]);

  const onClick = () => {
    setName("");

    setGuests([...guest, name]);
  };

  return (
    <div>
      <h3>Guest List</h3>
      <ul>
        {guest.map((guest) => (
          <li key={guest}>{guest}</li>
        ))}
      </ul>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button onClick={onClick}>Add guest</button>
    </div>
  );
};

export default GuestList;
