import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useFormik } from 'formik';
import * as yup from 'yup';
import "../stylesheets/App.css";
import "../stylesheets/SignUpForm.css";

function Signup({ setUser }) {
  const navigate = useNavigate();

  const formSchema = yup.object().shape({
    username: yup.string().required("Please enter a username").max(15),
    email: yup.string().email("Invalid email").required("Please enter a valid email address"),
    password: yup.string().required("Please enter a password"),
    confirmed_password: yup.string().oneOf([yup.ref('password'), null], 'Passwords must match').required("Please confirm your password")
  })

  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
      confirmed_password: ""
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch("/account_signup", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(values, null, 2)
      }).then((res) => {
        if (res.ok) {
          res.json().then((newUser) => {
            setUser(newUser)
            console.log(newUser)
            navigate(`/users/:username`);
          })
        }
      })
    }
  })

  return (
    <>
      <section className="signup-form-page">
        <form className="signup-form" onSubmit={formik.handleSubmit}>
          <h1 className="form-title">Create Your Account</h1>
          <p className="slogan">Power Up Your Re:Flex</p>
          <label className="form-label" htmlFor="username">
            Username{" "}
          </label>
          <input
            type="text"
            id="username"
            name="username"
            placeholder="Username"
            onChange={formik.handleChange}
            value={formik.values.username}
          ></input>
          <p className="error-text">{formik.errors.username}</p>
          <label className="form-label" htmlFor="email">
            Email{" "}
          </label>
          <input
            type="text"
            id="email"
            name="email"
            placeholder="name@company.com"
            onChange={formik.handleChange}
            value={formik.values.email}
          ></input>
          <p className="error-text">{formik.errors.email}</p>
          <label className="form-label" htmlFor="password">
            Password{" "}
          </label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Password"
            onChange={formik.handleChange}
            value={formik.values.password}
          ></input>
          <p className="error-text">{formik.errors.password}</p>
          <label className="form-label" htmlFor="confirmed_password">
            Confirm Password{" "}
          </label>
          <input
            type="password"
            id="confirmed_password"
            name="confirmed_password"
            placeholder="Confirm Password"
            onChange={formik.handleChange}
            value={formik.values.confirmed_password}
          ></input>
          <p className="error-text">{formik.errors.confirmed_password}</p>
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
