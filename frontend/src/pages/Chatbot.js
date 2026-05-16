import React, { useState } from 'react';
import axios from 'axios';

function Chatbot() {

  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const askQuestion = async () => {

    try {

      const res = await axios.post(
        'http://127.0.0.1:8000/chatbot',
        {
          question
        }
      );

      setAnswer(res.data.answer);

    } catch (error) {

      console.log(error);

      alert('Chatbot Error');
    }
  };

  return (

    <div style={{ padding: '50px' }}>

      <h1>AI Security Chatbot</h1>

      <input
        type="text"
        placeholder="Ask cybersecurity question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={{
          width: '400px',
          padding: '10px'
        }}
      />

      <br /><br />

      <button
        onClick={askQuestion}
        style={{
          padding: '10px 20px'
        }}
      >
        Ask AI
      </button>

      <br /><br />

      <div
        style={{
          border: '1px solid black',
          padding: '20px',
          width: '500px'
        }}
      >

        <h3>AI Response:</h3>

        <p>{answer}</p>

      </div>

    </div>
  );
}

export default Chatbot;