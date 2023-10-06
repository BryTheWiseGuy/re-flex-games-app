import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import Spinner from "react-bootstrap/esm/Spinner";
import Ratio from "react-bootstrap/Ratio";
import Button from "react-bootstrap/Button";
import "../stylesheets/GamePage.css";

function GamePage({ user, setUser }) {
  const [purchased, setPurchased] = useState(false);
  const [game, setGame] = useState({});
  const { id } = useParams();

  const navigate = useNavigate();

  useEffect(() => {
    fetch("/check_session").then((res) => {
      if (res.ok) {
        res.json().then((user) => setUser(user));
      }
    });
  }, []);

  useEffect(() => {
    fetch(`/games/${id}`)
      .then((res) => res.json())
      .then((game) => {
        setGame(game);
      });
  }, []);

  const handlePurchase = (e) => {
    e.preventDefault();
    if (user) {
      fetch(`/users/${user.username}/shopping_cart/items`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ game_id: game.id }),
      })
        .then(setPurchased(true))
        .catch((error) => {
          console.log("Network error:", error);
          alert("Network Error. Please try again later.");
        });
    } else {
      navigate("/login");
    }
  };

  if (game) {
    const {
      title,
      description,
      genre,
      release_date,
      publisher,
      price,
      carousel_image,
      game_trailer,
      platforms,
    } = game;

    return (
      <div className="game-page-container">
        <img className="banner-image" src={carousel_image} alt={title} />
        <h1 className="game-title-header">{title}</h1>
        <section className="game-information">
          <p key={crypto.randomUUID()} className="game-description">
            {description}
          </p>
          <section className="game-details">
            <article className="genre-publisher">
              <div className="genre">
                <h4>Genre</h4>
                <p>{genre}</p>
              </div>
              <div className="publisher">
                <h4>Publisher</h4>
                <p key={crypto.randomUUID()}>{publisher}</p>
              </div>
            </article>
            <article className="platform-release-date">
              <div className="release-date">
                <h4>Release Date: </h4>
                <p key={crypto.randomUUID()}>{release_date}</p>
              </div>
              <h4>Platforms: </h4>
              {platforms ? (
                <div className="platforms">
                  {platforms.map((platform) => {
                    return (
                      <p key={crypto.randomUUID()} className="platform">
                        {platform.platform}
                      </p>
                    );
                  })}
                </div>
              ) : null}
            </article>
          </section>
        </section>
        <div className="video-container">
          <Ratio aspectRatio="16x9">
            <iframe
              width="1280"
              height="720"
              src={game_trailer}
              title={title}
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              allowFullScreen
            ></iframe>
          </Ratio>
        </div>
        {purchased ? (
          <div className="sticky-bottom">
            <Button className="purchase-button" variant="danger" disabled>
              Purchase: {price}
            </Button>
          </div>
        ) : (
          <div className="sticky-bottom">
            <Button
              onClick={handlePurchase}
              className="purchase-button"
              variant="danger"
            >
              Add To Cart: {price}
            </Button>
          </div>
        )}
      </div>
    );
  } else {
    return (
      <div className="spinner-container">
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </div>
    );
  }
}

export default GamePage;
