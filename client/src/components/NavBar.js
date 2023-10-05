import React from 'react';
import '../stylesheets/NavBar.css'
import logo from '../media-assets/neon-controller-logo.png'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import 'bootstrap/dist/css/bootstrap.min.css'

function NavBar({ games, user, setUser }) {

  function handleLogout() {
    fetch('/logout', {
      method: "DELETE"
    }).then((r) => {
      if (r.ok) {
        setUser(null);
      }
    })
  }

  function renderIfUser(user) {
    if (user) {
      const { username } = user
      return <>
        <NavDropdown title={`${username}`}>
          <NavDropdown.Item href={`/users/${username}`}>Profile</NavDropdown.Item>
          <NavDropdown.Item href={`/users/${username}/library`}>Library</NavDropdown.Item>
        </NavDropdown>
        <Nav.Link href="/" onClick={handleLogout}>Logout</Nav.Link>
      </>
    } else {
      return <>
        <Nav.Link href="/login">Login</Nav.Link>
        <Nav.Link href="/account_signup">Sign Up</Nav.Link>
      </>
    }
  }

  return (
    <Navbar bg='dark' data-bs-theme='dark' expand="lg" sticky='top'>
      <Container>
        <Navbar.Brand href="/">
          <img className='nav-logo' src={logo} />
          Re:Flex Games
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <NavDropdown title="Games" id="basic-nav-dropdown">
              {games.map((game) => {
                const { id, title } = game
                return <NavDropdown.Item key={id} href={`/games/${id}`}>{title}</NavDropdown.Item>
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