import React from "react";
import { useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import * as yup from "yup";
import "../stylesheets/LoginForm.css";

function Login({ setUser }) {
  const navigate = useNavigate();

  const formSchema = yup.object().shape({
    username: yup.string().required("Please enter your username"),
    password: yup.string().required("Please enter your password"),
  });

  const formik = useFormik({
    initialValues: {
      username: "",
      password: "",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values, null, 2),
      }).then((res) => {
        if (res.ok) {
          res.json().then((newUser) => {
            setUser(newUser);
            navigate(`/users/:username`);
          });
        }
      });
    },
  });

  return (
    <div className="login-container">
      <div className="login-form-page">
        <form className="login-form" onSubmit={formik.handleSubmit}>
          <h1 className="form-title">Re:Flex Games</h1>
          <label className="form-label" htmlFor="username">
            Username:{" "}
          </label>
          <input
            type="text"
            id="username"
            name="username"
            placeholder="Username"
            value={formik.values.username}
            onChange={formik.handleChange}
            onBlue={formik.handleBlur}
          ></input>
          <p className="error-text">
            {formik.touched.username && formik.errors.username}
          </p>
          <label className="form-label" htmlFor="password">
            Password:{" "}
          </label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Password"
            value={formik.values.password}
            onChange={formik.handleChange}
            onBlue={formik.handleBlur}
          ></input>
          <p className="error-text">
            {formik.touched.password && formik.errors.password}
          </p>
          <button id="login-button" type="submit" value="Login">
            Login
          </button>
          <span className="signup-link">
            Don't have an account? <a href="/account_signup">Sign up!</a>
          </span>
        </form>
      </div>
    </div>
  );
}

export default Login;
