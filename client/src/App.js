import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home.js';
import Signup from './components/Signup.js';
import Login from './components/Login.js';
import UserProfile from './components/UserProfile.js';
import UserLibrary from './components/UserLibrary.js';
import ShoppingCart from './components/ShoppingCart.js';
import './stylesheets/App.css';

function App() {
  const [user, setUser] = useState(null);
  const [games, setGames] = useState([]);
  const [platforms, setPlatforms] = useState([]);

  // useEffect(() => {
  //   fetch('/check_session').then(res => {
  //     if (res.ok) {
  //       res.json().then(user => 
  //         setUser(user),
  //         console.log(user)
  //       )
  //     };
  //   });
  // });

  useEffect(() => {
    fetch('/games').then(res => {
      if (res.ok) {
        res.json().then(games => 
          setGames(games),
        )
      };
    });
  }, []);

  useEffect(() => {
    fetch('/platforms').then(res => {
      if (res.ok) {
        res.json().then(platforms => 
          setPlatforms(platforms),
        )
      }
    })
  }, [])

  console.log(games)
  console.log(platforms)

  return <div>
    <main className="App">
      <Router>
        <Routes>
          <Route path='/'
            element={
            <Home user={user} games={games} platforms={platforms} setUser={setUser}></Home>
          }
          exact />
          {/* <Route path='/account_signup' element={
            <Signup user={user} />
          }
          exact /> */}
          <Route path ='/login' element={
            <Login user={user} setUser={setUser} />
          }
          exact />
          {/* <Route path={`/users/${username}`} element={
            <UserProfile user={user} />
          }
          exact />
          <Route path={`/users/${username}/library`} element={
            <UserLibrary user={user} game={games} />
          }
          exact />
          <Route path={`/users/${username}/shopping_cart`} element={
            <ShoppingCart user={user} />
          }
          exact /> */}
        </Routes>
      </Router>
    </main>
  </div>;
}

export default App;
