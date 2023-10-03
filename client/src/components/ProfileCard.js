import React, { useState, useEffect } from 'react';

function ProfileCard({ user, setUser }) {
  const [isEditing, setIsEditing] = useState(false);
  const [editedAboutMe, setEditedAboutMe] = useState("")
  const [error, setError] = useState("")

  useEffect(() => {
    fetch("/check_session").then((res) => {
      if (res.ok) {
        res.json().then((user) => setUser(user));
      }
    });
  }, []);

  function handleSave(e) {
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
      <div className='profile-image-container'>
        <img src={profile_image} alt='profile picture' />
      </div>
      <h1>{username}</h1>
      {isEditing ? (
        <div className='profile-bio-container'>
          <div className='text-area-container'>
            <textarea
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
          <button onClick={handleSave}>Save Changes</button>
          <button onClick={() => setIsEditing(false)}>Cancel</button>
        </div>
      ) : (
        <div className='profile-bio-container'>
          <p>{about_me}</p>
          <button onClick={() => setIsEditing(true)}>Edit</button>
        </div>
      )}
    </div>
  } else {
    return <h1>User not logged in.</h1>
  }

}

export default ProfileCard;