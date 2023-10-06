import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar.js";
import Home from "./components/Home.js";
import Login from "./components/Login.js";
import Signup from "./components/Signup.js";
import UserProfile from "./components/UserProfile.js";
import UserLibrary from "./components/UserLibrary.js";
import ShoppingCart from "./components/ShoppingCart.js";
import GamePage from "./components/GamePage.js";
import "./stylesheets/App.css";

function App() {
  const [user, setUser] = useState(null);
  const [games, setGames] = useState([]);

  useEffect(() => {
    fetch("/games").then((res) => {
      if (res.ok) {
        res.json().then((games) => setGames(games));
      }
    });
  }, []);

  return (
    <div>
      <main className="App">
        <Router>
          <Routes>
            <Route
              path="/"
              element={<Home user={user} games={games} setUser={setUser} />}
              exact
            />
            <Route
              path="/login"
              element={
                <>
                  <NavBar user={user} games={games} setUser={setUser} />
                  <Login setUser={setUser} />
                </>
              }
              exact
            />
            <Route
              path="/account_signup"
              element={
                <>
                  <NavBar user={user} games={games} setUser={setUser} />
                  <Signup setUser={setUser} />
                </>
              }
              exact
            />
            <Route
              path="/users/:username"
              element={
                <>
                  <NavBar user={user} games={games} setUser={setUser} />
                  <UserProfile user={user} setUser={setUser} />
                </>
              }
              exact
            />
            <Route
              path="/games/:id"
              element={
                <>
                  <NavBar user={user} games={games} setUser={setUser} />
                  <GamePage user={user} setUser={setUser} />
                </>
              }
              exact
            />
            <Route
              path="/users/:username/shopping_cart"
              element={
                <>
                  <NavBar user={user} games={games} setUser={setUser} />
                  <ShoppingCart user={user} setUser={setUser} />
                </>
              }
              exact
            />
            <Route
              path="/users/:username/library"
              element={
                <>
                  <NavBar user={user} games={games} setUser={setUser} />
                  <UserLibrary user={user} setUser={setUser} />
                </>
              }
              exact
            />
          </Routes>
        </Router>
      </main>
    </div>
  );
}

export default App;
