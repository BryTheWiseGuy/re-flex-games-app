import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../stylesheets/GameCard.css'

function GameCard({ game }) {

  const navigate = useNavigate();
  const [clicked, setClicked] = useState(false)

  const { id, title, game_image } = game

  const handleGameSelect = () => {
    setClicked(!clicked)
    navigate(`/games/${id}`);
  }

  return <div className='game-container'>
      <img onClick={() => navigate(`/games/${id}`)} className='game-image' src={game_image} alt={title} />
      <button 
        className={clicked ? 'game-button-clicked' : 'game-button'} 
        onClick={handleGameSelect}>{ title }</button>
  </div>
}

export default GameCard