import { useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendPrompt = async () => {
    if (!prompt) return;

    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt })
      });

      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      setResponse("Error connecting to server");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "auto" }}>
      <h1>Recipe Generator</h1>

      <textarea
        rows="5"
        style={{ width: "100%" }}
        placeholder="List your ingredients..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button onClick={sendPrompt} style={{ marginTop: "10px" }}>
        Generate
      </button>

      {loading && <p>Loading...</p>}

      <div style={{ marginTop: "20px", whiteSpace: "pre-wrap" }}>
        {response}
      </div>
    </div>
  );
}

export default App;