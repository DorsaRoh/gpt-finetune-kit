import React, { useEffect, useState } from "react";

const Index: React.FC = () => {
  const [message, setMessage] = useState("Loading");
  const [people, setPeople] = useState<string[]>([]);
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  useEffect(() => {
    fetch("http://localhost:8080/api/home")
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
        setPeople(data.people);
      })
      .catch((error) => {
        console.error("Error fetching home data:", error);
        setMessage("Error loading data");
      });
  }, []);

  const handleGenerateText = () => {
    fetch("http://localhost:8080/api/text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.generated_text) {
          setResponse(data.generated_text);
        } else {
          console.error("Error generating text:", data.error);
        }
      })
      .catch((error) => console.error("Error generating text:", error));
  };

  return (
    <div>
      <div>{message}</div>
      <div>
        <h2>Enter prompt:</h2>
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt here"
        />
        <button onClick={handleGenerateText}>Generate Text</button>
        <p>{response}</p> {/* displays the generated text */}
      </div>
    </div>
  );
};

export default Index;
