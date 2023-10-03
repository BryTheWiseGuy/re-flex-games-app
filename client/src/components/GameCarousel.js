import React from 'react';
import Carousel from 'react-bootstrap/Carousel';
import FinalFantasyImage from '../media-assets/Carousel Images/final-fantasy-carousel.jpg';
import EldenRingImage from '../media-assets/Carousel Images/elden-ring-carousel.jpg';
import CyberpunkImage from '../media-assets/Carousel Images/cyberpunk-carousel-image.jpg';
import StarfieldImage from '../media-assets/Carousel Images/starfield-carousel-image.jpg';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../stylesheets/GameCard.css'

function GameCarousel({ games }) {

	return (
		<Carousel fade>
			<Carousel.Item key={ crypto.randomUUID() }>
				<div className='carousel-image-container'>
          <img className='carousel-image' src={FinalFantasyImage} alt='starfield-carousel-image' />
				</div>
			</Carousel.Item>
			<Carousel.Item key={ crypto.randomUUID() }>
				<div className='carousel-image-container'>
					<img className='carousel-image' src={EldenRingImage} alt='elden-ring-carousel-image' />
				</div>
				<Carousel.Caption>
					<div className='bottom-carousel-banner'>
						{/* <h3>{title}</h3>
						<p>{description}</p> */}
					</div>
				</Carousel.Caption>
			</Carousel.Item>
      <Carousel.Item key={ crypto.randomUUID() }>
				<div className='carousel-image-container'>
          <img className='carousel-image' src={CyberpunkImage} alt='cyberpunk-2077-carousel-image' />
				</div>
			</Carousel.Item>
			<Carousel.Item key={ crypto.randomUUID() }>
				<div className='carousel-image-container'>
          <img className='carousel-image' src={StarfieldImage} alt='starfield-carousel-image' />
				</div>
			</Carousel.Item>
		</Carousel>
	);
}

export default GameCarousel;