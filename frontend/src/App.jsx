import React, { useState } from "react";

const App = () => {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSend() {
    try {
      setLoading(true);

      const res = await fetch("http://localhost:5000/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });

      const data = await res.json();

      setResponse(data.reply || data.error);
    } catch (err) {
      console.log(err);
      setResponse("Error occurred");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>MCP AI Bot</h1>

      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Ask something..."
        style={{ width: "300px", padding: "10px" }}
      />

      <button onClick={handleSend} style={{ marginLeft: "10px" }}>
        Send
      </button>

      {loading && <p>Loading...</p>}

      <pre>{response}</pre>
    </div>
  );
};

export default App;
