import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Button from "react-bootstrap/Button";
import "../stylesheets/ShoppingCart.css";

function ShoppingCartPage({ user, setUser }) {
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/check_session").then((res) => {
      if (res.ok) {
        res.json().then((user) => setUser(user));
      } else {
        navigate('/login');
      }
    });
  }, []);

  function calculateTotal(shoppingCart) {
    let totalPrice = 0;
    if (shoppingCart) {
      shoppingCart[0].forEach((item) => {
        totalPrice += item.price;
      });
    }
    return totalPrice;
  }

  if (user) {
    const { user_shopping_cart } = user

    return (
      <section className="shopping-cart-page">
        <div className="shopping-cart-container">
          {user_shopping_cart
            ? user_shopping_cart[0].map((game) => {
                const { id, title, game_image, price } = game;

                function handleDelete(e) {
                  e.preventDefault()
                  fetch(`/users/${user.username}/shopping_cart/items`, {
                    method: 'DELETE',
                    headers: {
                      'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ game_id: id })
                  }).then(() => {
                    setUser((prevUser) => ({
                      ...prevUser,
                      user_shopping_cart: [prevUser.user_shopping_cart[0].filter((item) => item.id !== id)],
                    }));
                })};

                return (
                  <div className="cart-item-container">
                    <img
                      onClick={() => navigate(`/games/${id}`)}
                      className="shopping-cart-image"
                      src={game_image}
                      alt={title}
                    />
                    <div className="button-details-container">
                      <div className="details">
                        <p>{title}</p>
                        <p>{price}</p>
                      </div>
                      <Button variant="danger" className="remove-button" onClick={handleDelete}>
                        Remove from cart
                      </Button>
                    </div>
                  </div>
                );
              })
            : null}
        </div>
        <div className="sticky-bottom">
          <Button variant="danger" className="checkout-button">
            Complete Purchase: {calculateTotal(user_shopping_cart)}
          </Button>
        </div>
      </section>
    );
  }
}

export default ShoppingCartPage;
