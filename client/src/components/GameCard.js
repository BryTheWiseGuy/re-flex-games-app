import React from 'react';
import { useNavigate } from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import '../stylesheets/GameCard.css'

function GameCard({ game }) {
  const navigate = useNavigate();

  const { id, title, game_image } = game

  return <div className='game-container'>
      <img onClick={() => navigate(`/games/${id}`)} className='game-image' src={game_image} alt={title} />
      <Button 
        className='game-button'
        variant='danger'
        onClick={() => navigate(`/games/${id}`)}
      >{title}</Button>
  </div>
}

export default GameCard