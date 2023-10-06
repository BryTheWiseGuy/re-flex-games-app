import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../stylesheets/App.css";
import "../stylesheets/SignUpForm.css";

function Signup({ setUser }) {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmed_password, setConfirmedPassword] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate();

  function handleSignup(e) {
    e.preventDefault();
    fetch("/account_signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        email,
        password,
        confirmed_password,
        about_me: "",
        profile_image: "",
      }),
    })
      .then((res) => {
        if (res.ok) {
          res.json().then((user) => {
            setUser(user);
            navigate(`/users/${username}`);
          });
        } else {
          handleSignupErrors();
        }
      })
      .catch((error) => {
        console.log("Network error:", error);
        alert("Network Error. Please try again later.");
      });
  }

  function handleSignupErrors() {
    if (!username) {
      return setError("Error: Please enter a valid username.");
    } else if (!email) {
      return setError("Error: Please enter a valid email.");
    } else if (!password) {
      return setError("Error: Please enter a valid password.");
    } else if (password != confirmed_password) {
      return setError("Error: Passwords do not match.");
    } else if (!confirmed_password) {
      return setError("Error: Please confirm your password.");
    } else {
      return null;
    }
  }

  return (
    <>
      <section className="signup-form-page">
        <form className="signup-form" onSubmit={handleSignup}>
          <h1 className="form-title">Create Your Account</h1>
          <p className="slogan">Power Up Your Re:Flex</p>
          <label className="form-label" htmlFor="username">
            Username{" "}
          </label>
          <input
            type="text"
            id="username"
            placeholder="Username"
            autoComplete="off"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          ></input>
          <label className="form-label" htmlFor="email">
            Email{" "}
          </label>
          <input
            type="text"
            id="email"
            placeholder="name@company.com"
            autoComplete="off"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          ></input>
          <label className="form-label" htmlFor="password">
            Password{" "}
          </label>
          <input
            type="password"
            id="password"
            placeholder="Password"
            autoComplete="off"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          ></input>
          <label className="form-label" htmlFor="password_confirm">
            Confirm Password{" "}
          </label>
          <input
            type="password"
            id="password_confirm"
            placeholder="Confirm Password"
            autoComplete="off"
            value={confirmed_password}
            onChange={(e) => setConfirmedPassword(e.target.value)}
          ></input>
          {error ? <p className="error-text">{error}</p> : null}
          <button id="signup-button" type="submit" value="Signup">
            Sign Up!
          </button>
          <span className="login-link">
            Already have an account? <a href="/login">Login</a>
          </span>
        </form>
      </section>
    </>
  );
}

export default Signup;
