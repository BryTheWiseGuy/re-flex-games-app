import React from 'react';
import NavBar from './NavBar.js';

function Signup({ games, user, setUser }) {

  return (
    <>
      <NavBar games={games} user={user} setUser={setUser} />
      <div className='login-form-page'>
        <form className='login-form'>
          <h1 className='form-title'>Re:Flex Games</h1>
          <label className='form-label' htmlFor='username'>Username: </label>
          <input
            type='text'
            id='username'
            placeholder='Enter username'
            autoComplete='off'
            >
          </input>
          <label className='form-label' htmlFor='password'>Password: </label>
          <input 
            type='text'
            id='password'
            placeholder='Enter password'
            autoComplete='current-password'
            >
          </input>
          <button id='login-button' type='submit' value='Login'>Login</button>
          <span className="signup-link">Don't have an account? <a href="/account_signup">Sign up!</a></span>
        </form>
      </div>
    </>
  );

}

export default Signup;
