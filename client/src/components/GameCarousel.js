import React from 'react';
import Carousel from 'react-bootstrap/Carousel';
import EldenRingImage from '../media-assets/Carousel Images/elden-ring-carousel.jpg';
import GenshinImpactImage from '../media-assets/Carousel Images/genshin-impact-carousel.jpg';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../stylesheets/GameCard.css'

function GameCarousel({ games }) {

	return (
		<Carousel fade>
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
          <img className='carousel-image' src={GenshinImpactImage} alt='genshin-impact-carousel-image' />
				</div>
				<Carousel.Caption>
					<div className='bottom-carousel-banner'>
						{/* <h3>{title}</h3>
						<p>{description}</p> */}
					</div>
				</Carousel.Caption>
			</Carousel.Item>
		</Carousel>
	);
}

export default GameCarousel;