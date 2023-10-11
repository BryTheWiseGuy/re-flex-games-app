import React from 'react';
import Carousel from 'react-bootstrap/Carousel';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../stylesheets/HomePage.css';

function GameCarousel({ games }) {
	
	return (
		<Carousel fade>
			{games.map((game) => {
				const { id, title, carousel_image } = game
				if (id <= 5){
					return (
						<Carousel.Item key={ crypto.randomUUID() }>
							<div className='carousel-image-container'>
								<img className='carousel-image' src={carousel_image} alt={title} />
							</div>
						</Carousel.Item>
				)} else {
					return null
				}
			})}
		</Carousel>
	);
}

export default GameCarousel;