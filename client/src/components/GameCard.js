import React from 'react';
import '../stylesheets/GameCard.css'

function GameCard({ game }) {
    
    const { id, title, description, release_date, 
        publisher, game_image, price, platforms} = game

    return <div className='game-information-panel'>
            <div className='game-image-container'>
                <img className='game-image' src={game_image} alt={title} />
            </div>
        <section className='game-information'>
            <h1 className='game-title'>{title}</h1>
            <h2>{publisher}</h2>
            {platforms.map((platform) => {
                return <p>{platform.platform}</p>
            })}
            <p>{description}</p>
            <p>{release_date}</p>
            <p>{price}</p>
        </section>
    </div>
}

export default GameCard