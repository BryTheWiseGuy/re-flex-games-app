import React, { useEffect, useState } from "react";
import NavBar from './NavBar.js';
import { useParams } from "react-router-dom";
import Spinner from "react-bootstrap/esm/Spinner";
import Ratio from 'react-bootstrap/Ratio';
import ReactPlayer from 'react-player';
import '../stylesheets/GamePage.css';

function GamePage({ games, user, setUser }) {
  const { id } = useParams();

  const game = games.find((game) => game.id = id)

  if (game) {
    const { title, description, genre, release_date, publisher, price, carousel_image, game_trailer } = game;
    return (
      <>
        <NavBar games={games} user={user} setUser={setUser} />
        <img className='banner-image' src={carousel_image} />
        <div className='game-page-container'>
          <h1 className="game-title-header">{title}</h1>
          <section className='game-card'>
            <p>{description}</p>
            <p>Genre: {genre}</p>
            <p>Publisher: {publisher}</p>
            <p>Release Date: {release_date}</p>
          </section>
          <Ratio aspectRatio="16x9">
            <iframe 
              width="1280" 
              height="720" 
              src={game_trailer} 
              title="ELDEN RING – Rise, Tarnished | Official Launch Trailer" 
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen
            ></iframe>
          </Ratio>
        </div>
      </>
    )
  } else {
    return (
      <div className='spinner-container'>
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </div>
    )
  }
}

export default GamePage;
