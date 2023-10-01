import React, { useState } from 'react';
import '../stylesheets/NavBar.css'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import 'bootstrap/dist/css/bootstrap.min.css'

function NavBar({ games, user, setUser }) {

  function renderIfUser(user) {
    if (user) {
      const { username } = user
      return <>
        <NavDropdown title={`${username}`}>
          <NavDropdown.Item href={`/users/${username}`}>Profile</NavDropdown.Item>
          <NavDropdown.Item href={`/users/${username}/library`}>Library</NavDropdown.Item>
        </NavDropdown>
        <Nav.Link href="/logout">Logout</Nav.Link>
      </>
    } else {
      return <>
        <Nav.Link href="/login">Login</Nav.Link>
        <Nav.Link href="/account_signup">Sign Up</Nav.Link>
      </>
    }
  }

  return (
    <Navbar bg='dark' data-bs-theme='dark' expand="lg">
      <Container>
        <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <NavDropdown title="Dropdown" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">
                Another action
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">
                Separated link
              </NavDropdown.Item>
            </NavDropdown>
            {renderIfUser(user)}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;