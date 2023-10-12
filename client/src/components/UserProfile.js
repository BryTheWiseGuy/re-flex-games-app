import React, { useEffect } from 'react';
import ProfileCard from '../components/ProfileCard.js';
import { useNavigate } from 'react-router-dom';
import '../stylesheets/ProfilePage.css';

function UserProfile({ user, setUser }) {

  const navigate = useNavigate()

  useEffect(() => {
    fetch('/api/check_session').then(res => {
      if (res.ok) {
        res.json().then(user => 
          setUser(user),
        )
      } else {
        navigate('/login');
      };
    });
  }, [navigate, setUser]);

  return <div className='profile-page-container'>
    <div className='profile-page'>
      <ProfileCard user={user} setUser={setUser} />
    </div>
  </div>
};

export default UserProfile;