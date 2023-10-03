import React, { useEffect} from "react";
import GameCarousel from "./GameCarousel";
import GameCard from "./GameCard";
import NavBar from "./NavBar";
import '../stylesheets/HomePage.css';

function Home({ user, games, setUser }) {
  
  useEffect(() => {
    fetch("/check_session").then((res) => {
      if (res.ok) {
        res.json().then((user) => setUser(user));
      }
    });
  }, []);

  return (
    <div>
      <GameCarousel games={games} />
      <NavBar games={games} user={user} setUser={setUser} />
      <div className='grid-container'>
      {games.map((game) => {
        return <GameCard key={game.id} game={game} />
        })}
      </div>
    </div>
  );
}

export default Home;
