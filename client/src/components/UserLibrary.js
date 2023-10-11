// Insert Fetch Request for /user/<username>/library/<int:id>
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Spinner from "react-bootstrap/Spinner";
import "../stylesheets/UserLibrary.css";

function UserLibrary({ user, setUser }) {
  const [showModal, setShowModal] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/check_session").then((res) => {
      if (res.ok) {
        res.json().then((user) => setUser(user));
      }
    });
  }, [setUser]);

  if (user) {
    const { library, username } = user;

    return (
      <>
        <div className="user-library-page">
          <div className="library-header">
            <p>Game Library</p>
          </div>
          <div className="user-library-grid">
            {library
              ? library.map((game) => {
                  const { game_image, title, id } = game;

                  async function handleDelete(e) {
                    e.preventDefault();
                    const response = await fetch(
                      `/users/${username}/library/${id}`,
                      {
                        method: "DELETE",
                        headers: {
                          "Content-Type": "application/json",
                        },
                      }
                    );

                    if (response.ok) {
                      const updatedUser = await response.json();
                      setUser(updatedUser);
                      setShowModal(true);
                    }
                  }

                  return (
                    <>
                      <Modal
                        show={showModal}
                        onHide={() => setShowModal(false)}
                        className="custom-modal"
                      >
                        <Modal.Header>
                          <Modal.Title>
                            <i
                              className="fa-regular fa-circle-check"
                              style={{ marginRight: "8px" }}
                            ></i>
                            Game Removed!
                          </Modal.Title>
                        </Modal.Header>
                        <Modal.Body>
                          Game has successfully been removed from your library!
                        </Modal.Body>
                      </Modal>
                      <div className="game-container">
                        <img
                          onClick={() => navigate(`/games/${id}`)}
                          className="library-game-image"
                          src={game_image}
                          alt={title}
                        />
                        <div className="button-container">
                          <Button className="library-play-button">
                            <i className="fa-solid fa-play"></i>
                          </Button>
                          <Button
                            className="library-remove-button"
                            variant="danger"
                            onClick={handleDelete}
                          >
                            <i className="fa-regular fa-trash-can fa-sm"></i>
                          </Button>
                        </div>
                      </div>
                    </>
                  );
                })
              : null}
          </div>
        </div>
      </>
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

export default UserLibrary;
