import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import "../stylesheets/ShoppingCart.css";

function ShoppingCartPage({ user, setUser }) {
  const [showModal, setShowModal] = useState(false);

  const navigate = useNavigate();
  const closeModal = () => setShowModal(false);

  useEffect(() => {
    fetch("/check_session").then((res) => {
      if (res.ok) {
        res.json().then((user) => setUser(user));
      } else {
        navigate("/login");
      }
    });
  }, []);

  function calculateTotal(shoppingCart) {
    let totalPrice = 0;
    if (shoppingCart) {
      shoppingCart.forEach((item) => {
        totalPrice += item.game.price;
      });
    }
    return totalPrice;
  }

  if (user) {
    const { user_shopping_cart } = user;

    function handlePurchase(e) {
      e.preventDefault();
      fetch(`/checkout/${user_shopping_cart[0][0].shopping_cart_id}`)
        .then((res) => res.json())
        .then((updatedUser) => {
          setUser(updatedUser);
          setShowModal(true);
        });
    }

    return (
      <section className="shopping-cart-page">
        <div className="shopping-cart-container">
          {user_shopping_cart
            ? user_shopping_cart[0].map((game) => {
                const { id, title, game_image, price } = game.game;

                function handleDelete(e) {
                  e.preventDefault();
                  fetch(`/users/${user.username}/shopping_cart/items`, {
                    method: "DELETE",
                    headers: {
                      "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ game_id: id }),
                  }).then((res) => {
                    if (res.ok) {
                      res.json().then((updatedUser) => {
                        setUser(updatedUser);
                      });
                    }
                  });
                }

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
                        <p className="title">{title}</p>
                        <p className="price">{price}</p>
                      </div>
                      <Button
                        variant="danger"
                        className="remove-button"
                        onClick={handleDelete}
                      >
                        Remove from cart
                      </Button>
                    </div>
                  </div>
                );
              })
            : null}
        </div>
        <div className="sticky-bottom">
          {user_shopping_cart[0].length > 0 ? (
            <Button
              variant="danger"
              className="checkout-button"
              onClick={handlePurchase}
            >
              Complete Purchase: ${calculateTotal(user_shopping_cart[0])}
            </Button>
          ) : (
            <Button variant="danger" className="checkout-button" disabled>
              Complete Purchase: ${calculateTotal(user_shopping_cart[0])}
            </Button>
          )}
          <Modal
            show={showModal}
            onHide={closeModal}
            variant="dark"
            className="custom-modal"
          >
            <Modal.Header>
              <Modal.Title>
                <i
                  class="fa-regular fa-circle-check"
                  style={{ marginRight: "8px" }}
                ></i>
                Purchase Successful!
              </Modal.Title>
            </Modal.Header>
            <Modal.Body>
              Games have been successfully added to your library!
            </Modal.Body>
          </Modal>
        </div>
      </section>
    );
  }
}

export default ShoppingCartPage;
