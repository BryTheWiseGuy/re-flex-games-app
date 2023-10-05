import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import NavBar from "./NavBar";
import "../stylesheets/LoginForm.css";

function Login({ games, user, setUser }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  // Set state for error and use to conditionally render message beneath password element
  const [error, setError] = useState("");

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    }).then((res) => {
      if (res.ok) {
        res.json().then((user) => {
          setUser(user);
          navigate(`/users/${user.username}`);
        });
      } else {
        return res.json()
        .then(() => {
          setError("Error: Please enter a valid username and password.")
        })
        .catch((error) => {
          console.log("Network error:", error);
          alert("Network Error. Please try again later.");
        });
      }
    });
  };

  return (
    <>
      <NavBar games={games} user={user} />
      <div className="login-form-page">
        <form className="login-form" onSubmit={handleSubmit}>
          <h1 className="form-title">Re:Flex Games</h1>
          <label className="form-label" htmlFor="username">
            Username:{" "}
          </label>
          <input
            type="text"
            id="username"
            placeholder="Enter username"
            autoComplete="off"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          ></input>
          <label className="form-label" htmlFor="password">
            Password:{" "}
          </label>
          <input
            type="password"
            id="password"
            placeholder="Enter password"
            autoComplete="current-password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          ></input>
          {error ? <p className="error-text">{error}</p> : null}
          <button id="login-button" type="submit" value="Login">
            Login
          </button>
          <span className="signup-link">
            Don't have an account? <a href="/account_signup">Sign up!</a>
          </span>
        </form>
      </div>
    </>
  );
}

export default Login;
