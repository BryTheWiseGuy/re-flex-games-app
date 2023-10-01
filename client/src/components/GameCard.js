import React from 'react';
import '../stylesheets/GameCard.css'

function GameCard({ game }) {
    
    const { id, title, description, release_date, 
        publisher, game_image, price, platforms} = game

    return <div class='game-information-panel'>
            <div class='game-image-container'>
                <img class='game-image' src={game_image} alt={title} />
            </div>
        <section class='game-information'>
            <h1 class='game-title'>{title}</h1>
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