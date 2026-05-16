import React, { useState } from 'react';
import axios from 'axios';

function Login() {

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const login = async () => {

    try {

      const res = await axios.post(
        'http://127.0.0.1:8000/login',
        {
          email,
          password
        }
      );

      alert('Login Success');

      console.log(res.data);

    } catch (error) {

      console.log(error);

      alert('Login Failed');
    }
  };

  return (

    <div style={{ padding: '50px' }}>

      <h1>AI Threat Intelligence Login</h1>

      <input
        type="text"
        placeholder="Enter Email"
        onChange={(e) => setEmail(e.target.value)}
        style={{
          padding: '10px',
          marginTop: '20px',
          width: '300px'
        }}
      />

      <br /><br />

      <input
        type="password"
        placeholder="Enter Password"
        onChange={(e) => setPassword(e.target.value)}
        style={{
          padding: '10px',
          width: '300px'
        }}
      />

      <br /><br />

      <button
        onClick={login}
        style={{
          padding: '10px 20px',
          cursor: 'pointer'
        }}
      >
        Login
      </button>

    </div>
  );
}

export default Login;