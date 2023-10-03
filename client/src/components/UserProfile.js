import React, { useEffect } from 'react';
import Navbar from '../components/NavBar.js'
import ProfileCard from '../components/ProfileCard.js';
import { useNavigate } from 'react-router-dom';

function UserProfile({ user, games, setUser }) {

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
    <section>
      <div className='profile-page'>
        <ProfileCard user={user} setUser={setUser} />
      </div>
    </section>
  </>
};

export default UserProfile;