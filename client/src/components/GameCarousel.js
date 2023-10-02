import React from 'react';
import Carousel from 'react-bootstrap/Carousel';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../stylesheets/GameCard.css'
import { v4 as uuidv4 } from 'uuid'

function GameCarousel({ games }) {

	return (
		<Carousel fade>
			{games.map((game) => {
				const { id, game_image, title, description } = game
				return (<Carousel.Item key={id}>
					<div className='carousel-image-container'>
						<img className='carousel-image' src={game_image} alt='Carousel Images' />
					</div>
					<Carousel.Caption>
						<div className='bottom-carousel-banner'>
							<h3>{title}</h3>
							<p>{description}</p>
						</div>
					</Carousel.Caption>
				</Carousel.Item>
				)
			})}
		</Carousel>
	);
}

export default GameCarousel;