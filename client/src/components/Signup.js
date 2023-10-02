import React from 'react';
import NavBar from './NavBar.js';
import '../stylesheets/SignUpForm.css'

function Signup({ games, user, setUser }) {

  return (
    <>
      <NavBar games={games} user={user} setUser={setUser} />
      <div className='signup-form-page'>
        <form className='signup-form'>
          <h1 className='form-title'>Create Your Account</h1>
          <p>Power Up Your Re:Flex</p>
          <label className='form-label' htmlFor='username'>Username </label>
          <input
            type='text'
            id='username'
            placeholder="Username"
            autoComplete='off'
            >
          </input>
          <label className='form-label' htmlFor='email'>Email </label>
          <input 
            type='text'
            id='email'
            placeholder='name@company.com'
            autoComplete='off'
            >
          </input>
          <label className='form-label' htmlFor='password'>Password </label>
          <input 
            type='text'
            id='password'
            placeholder='Password'
            autoComplete='off'
            >
          </input>
          <label className='form-label' htmlFor='password_confirm'>Confirm Password </label>
          <input 
            type='text'
            id='password_confirm'
            placeholder='Confirm Password'
            autoComplete='off'
            >
          </input>
          <button id='signup-button' type='submit' value='Login'>Sign Up!</button>
          <span className="login-link">Already have an account? <a href="/login">Login</a></span>
        </form>
      </div>
    </>
  );

}

export default Signup;
