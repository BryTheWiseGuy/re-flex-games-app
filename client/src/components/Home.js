import React from 'react';
import GameCarousel from './GameCarousel';
import GameCard from './GameCard';
import NavBar from './NavBar';
import { v4 as uuidv4 } from 'uuid'

function Home({ user, games, setUser }) {

    return <div>
        <GameCarousel games={games} />
        <NavBar games={games} user={user} setUser={setUser}/>
        {games.map((game) => {
            return <GameCard 
                key={uuidv4()}
                game={game} />
        })}
    </div>
}


export default Home