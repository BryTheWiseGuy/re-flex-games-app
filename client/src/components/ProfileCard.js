import React, { useState, useEffect } from 'react';

function ProfileCard({ user, setUser }) {
  const [isEditing, setIsEditing] = useState(false);
  const [editedAboutMe, setEditedAboutMe] = useState("")
  const [error, setError] = useState("")

  function handleSave(e) {
    (e).preventDefault()
    fetch(`/users/${user.username}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ about_me: editedAboutMe })
    }).then((res) => {
      if (res.ok) {
        res.json().then((about_me) => {
          setIsEditing(false);
          setEditedAboutMe(about_me);
          setUser(user);
        })
      }
    })
  }

  console.log(user)
  
  const { username } = user

  return <div className='profile-card-container'>
      <div className='profile-image-container'>
        <img alt='profile picture' />
      </div>
      <h1></h1>
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
          <p></p>
          <button onClick={() => setIsEditing(true)}>Edit</button>
        </div>
      )}
    </div>
}

export default ProfileCard;