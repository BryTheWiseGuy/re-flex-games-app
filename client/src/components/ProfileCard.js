import React, { useState, useEffect } from 'react';
import Spinner from 'react-bootstrap/Spinner';
import Button from 'react-bootstrap/esm/Button';
import '../stylesheets/ProfilePage.css'

function ProfileCard({ user, setUser }) {
  const [isEditing, setIsEditing] = useState(false);
  const [isAddingImage, setIsAddingImage] = useState(false);
  const [profileImage, setProfileImage] = useState(null)
  const [editedAboutMe, setEditedAboutMe] = useState("")
  const [error, setError] = useState("")

  useEffect(() => {
    fetch("/check_session").then((res) => {
      if (res.ok) {
        res.json().then((user) => setUser(user));
      }
    });
  }, []);

  function handleSaveProfileImage(e) {
    e.preventDefault()
    fetch(`/users/${user.username}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ profile_image: profileImage })
    }).then((res) => {
      if (res.ok) {
        res.json().then((updatedUser) => {
          setUser(updatedUser)
          setIsAddingImage(false);
        })
      }
    })
  }

  function handleSaveAboutMe(e) {
    e.preventDefault()
    fetch(`/users/${user.username}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ about_me: editedAboutMe })
    }).then((res) => {
      if (res.ok) {
        res.json().then((updatedUser) => {
          setUser(updatedUser)
          setIsEditing(false);
        })
      }
    })
  }

  if (user) {
    const { username, profile_image, about_me } = user
    return <div className='profile-card-container'>
      <h1 className='username'>{username}</h1>
      {isAddingImage ? (
        <div className='profile-image-container'>
          {profileImage ? (
              <img src={profile_image} alt='profile picture' />
            ) : (
              <img src='https://beforeigosolutions.com/wp-content/uploads/2021/12/dummy-profile-pic-300x300-1.png' alt='profile picture placeholder' />
          )}
          <input
            className='text-input'
            type="text"
            onChange={(e) => setProfileImage(e.target.value)}
          />
          <Button variant='info' className='save-button' onClick={handleSaveProfileImage}>Save</Button>
          <Button className='cancel-button' onClick={() => setIsAddingImage(false)}>Cancel</Button>
        </div>
      ) : (
        <div className='profile-image-container'>
          {profile_image ? (
            <img src={profile_image} alt='profile picture' />
          ) : (
            <img src='https://beforeigosolutions.com/wp-content/uploads/2021/12/dummy-profile-pic-300x300-1.png' alt='profile picture placeholder' />
          )}
          <Button className='change-button' onClick={() => setIsAddingImage(true)}>Change Profile Image</Button>
        </div>
      )}
      <section className='about-me-section'>
      <h1 className='about-me-label'>About Me</h1>
        {isEditing ? (
          <div className='profile-bio-container'>
            <div className='text-area-container'>
              <textarea
                className='text-area'
                type='text'
                value={editedAboutMe}
                onChange={(e) => setEditedAboutMe(e.target.value)}
                rows={4}
                maxLength="250"
              />
              <div className='character-counter'>
                {editedAboutMe.length}/{250}
              </div>
            </div>
            {error ? <p></p> : null}
            <Button variant='info' className='save-button' onClick={handleSaveAboutMe}>Save Changes</Button>
            <Button className='cancel-button' onClick={() => setIsEditing(false)}>Cancel</Button>
          </div>       
        ) : (
          <div className='profile-bio-container'>
            <p>{about_me}</p>
            <Button className='change-button' onClick={() => setIsEditing(true)}>Edit</Button>
          </div>
        )}
      </section>
    </div>
  } else {
    return (
      <div className='spinner-container'>
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </div>
    )
  }

}

export default ProfileCard;