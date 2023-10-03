import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home.js';
import Login from './components/Login.js';
import Signup from './components/Signup.js'
import UserProfile from './components/UserProfile.js';
import './stylesheets/App.css';
import GamePage from "./components/GamePage.js";

function App() {
  const [user, setUser] = useState(null);
  const [games, setGames] = useState([]);
  const [platforms, setPlatforms] = useState([]);

  useEffect(() => {
    fetch('/games').then(res => {
      if (res.ok) {
        res.json().then(games =>
          setGames(games),
        )
      };
    });
  }, []);

  console.log(user);

  return <div>
    <main className="App">
      <Router>
        <Routes>
          <Route path='/' element={<Home user={user} games={games} setUser={setUser} />} exact />
          <Route path='/login' element={<Login games={games} user={user} setUser={setUser} />} exact />
          <Route path='/account_signup' element={<Signup user={user} games={games} setUser={setUser}/>} exact />
          <Route path='/users/:username' element={<UserProfile user={user} games={games} setUser={setUser} />} exact />
          <Route path='/games/:id' element={<GamePage />} exact/>
        </Routes>
      </Router>
    </main>
  </div>;
}

  export default App;
