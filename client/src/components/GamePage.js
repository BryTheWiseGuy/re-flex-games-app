import React, { useEffect, useState } from "react";
import NavBar from '../components/NavBar.js';
import { useParams } from "react-router-dom";
import Spinner from "react-bootstrap/esm/Spinner";

function GamePage({ games, user, setUser }) {
  const { id } = useParams();

  const game = games.find((game) => game.id = id)

  if (game) {
    const { title } = game;
    return (
      <div>
        <NavBar games={games} user={user} setUser={setUser} />
        <h1>{title}</h1>
      </div>
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
