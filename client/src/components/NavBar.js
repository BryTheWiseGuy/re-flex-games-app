import React from "react";
import NavDropdown from "react-bootstrap/NavDropdown";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import logo from "../media-assets/neon-controller-logo.png";
import "../stylesheets/NavBar.css";
import "bootstrap/dist/css/bootstrap.min.css";

function NavBar({ games, user, setUser }) {
  
  const handleLogout = async ()  => {
    const response = await fetch("/logout", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json"
      }
    }).then((res) => {
      if (response.ok) {
        setUser(null);
      }
    }).catch((error) => {
      console.error('Error during logout:', error);
    });
  }

  function renderIfUser(user) {
    if (user) {
      const { username } = user;

      return (
        <>
          <NavDropdown title={`${username}`}>
            <NavDropdown.Item
              href={`/users/${username}`}
              style={{ fontSize: "24px", display: "flex", alignItems: "center" }}
            >
              Profile <i className="fa-solid fa-user fa-xs" style={{marginLeft: '8px'}}></i>
            </NavDropdown.Item>
            <NavDropdown.Item
              href={`/users/${username}/library`}
              style={{ fontSize: "24px", display: "flex", alignItems: "center" }}
            >
              Library<i className="fa-solid fa-gamepad" style={{marginLeft: '8px'}}></i>
            </NavDropdown.Item>
            <NavDropdown.Item
              href={`/users/${username}/shopping_cart`}
              style={{ fontSize: "24px", display: "flex", alignItems: "center" }}
            >
              Shopping Cart <i className="fa-solid fa-cart-shopping fa-xs" style={{marginLeft: '8px'}}></i>
            </NavDropdown.Item>
          </NavDropdown>
          <Nav.Link 
            href="/" onClick={handleLogout}
            style={{ display: "flex", alignItems: "center" }}
          >
            Logout <i className="fa-solid fa-arrow-right-from-bracket fa-2xs" style={{marginLeft: '10px'}}></i>
          </Nav.Link>
        </>
      );
    } else {
      return (
        <>
          <Nav.Link href="/login">Login</Nav.Link>
          <Nav.Link href="/account_signup">Sign Up</Nav.Link>
        </>
      );
    }
  }

  return (
    <Navbar bg="dark" data-bs-theme="dark" expand="lg" sticky="top">
      <Container>
        <Navbar.Brand href="/">
          <img className="nav-logo" src={logo} alt='logo'/>
          Re:Flex Games
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link 
              href="/"
              style={{ display: "flex", alignItems: "center" }}
            >
              Home <i className="fa-solid fa-house fa-2xs" style={{marginLeft: '10px'}}></i>
            </Nav.Link>
            <NavDropdown title="Games" id="basic-nav-dropdown">
              {games.map((game) => {
                const { id, title } = game;
                return (
                  <NavDropdown.Item
                    key={id}
                    href={`/games/${id}`}
                    style={{ fontSize: "24px" }}
                  >
                    {title}
                  </NavDropdown.Item>
                );
              })}
            </NavDropdown>
            {renderIfUser(user)}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;
