import React, { useEffect, useState } from "react";

function App() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5050/messages")
      .then((res) => res.json())
      .then((data) => setMessages(data));
  }, []);

  return (
    <div>
      <h1>📨 Messages depuis la base :</h1>
      <ul>
        {messages.map((msg) => (
          <li key={msg.id}>{msg.text}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
