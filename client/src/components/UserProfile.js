import React, { useEffect } from 'react';
import Navbar from '../components/NavBar.js'
import { useParams, useNavigate } from 'react-router-dom';

function UserProfile({ user, games, setUser }) {
  const { username } = useParams()
  const navigate = useNavigate()

  useEffect(() => {
    fetch('/check_session').then(res => {
      if (res.ok) {
        res.json().then(user => 
          setUser(user),
        )
      } else {
        navigate('/login');
      };
    });
  }, []);

  return <>
    <Navbar user={user} games={games} setUser={setUser}/>
    <h1>Welcome to poopy profile page!!</h1>
  </>
};

export default UserProfile;