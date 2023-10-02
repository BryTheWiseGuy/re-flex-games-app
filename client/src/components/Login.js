import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import NavBar from './NavBar';
import '../stylesheets/LoginForm.css';

function Login({ setUser, games, user }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/login", {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password}),
    }).then((res) => {
      if (res.ok) {
        res.json().then((newUser) =>{
          setUser(newUser);
        });
      } else {
        res.json().then((err) => setErrors(err.errors))
      }
    })
  }

  return (
    <>
      <NavBar games={games} user={user}/>
      <div className='login-form-page'>
        <form className='login-form' onSubmit={handleSubmit}>
          <h1 className='form-title'>Re:Flex Games</h1>
          <label className='form-label' htmlFor='username'>Username: </label>
          <input
            type='text'
            id='username'
            placeholder='Enter username'
            autoComplete='off'
            value={username}
            onChange={(e) => setUsername(e.target.value)}>
          </input>
          <label className='form-label' htmlFor='password'>Password: </label>
          <input 
            type='text'
            id='password'
            placeholder='Enter password'
            autoComplete='current-password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}>
          </input>
          <Link href={`/users/${username}`}>
            <button id='login-button' type='submit' value='Login'>Login</button>
          </Link>
          <span className="signup-link">Don't have an account? <a href="/account_signup">Sign up!</a></span>
        </form>
      </div>
    </>
  );
}

export default Login;