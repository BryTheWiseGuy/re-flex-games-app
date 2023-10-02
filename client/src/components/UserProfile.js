import React from 'react';
import Navbar from '../components/NavBar.js'
import { useParams } from 'react-router-dom';

function UserProfile({ user, games, setUser }) {
  const { username } = useParams()
  return <>
    <Navbar user={user} games={games} setUser={setUser}/>
    <h1>Welcome to poopy profile page!!</h1>
  </>
};

export default UserProfile;