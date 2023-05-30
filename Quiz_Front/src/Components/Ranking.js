// Final Project: Quiz Application with Microservices
// Date: 29-May-2023
// Authors:
//          A01752030 Juan Pablo Castañeda Serrano
//          A0752221 Omar Rodrigo Talavera Becerra
//          A01752013 Nadia Paola Ferro Gallegos
////////////////////////////////////////////////////////////////////////////////////
/*
Ranking.js
Get the best users and show in a table

*/
import "../Styles/Ranking.css";
import "../Styles/CloseBtn.css";
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import UserRank from "./UserRank";

const Ranking = (props) => {
  const setShowRank = props.setShowRank;
  const { dificultad } = props;
  const [ranking, setRanking] = useState([]);

  useEffect(() => {               //Get the names and sort the positions
    DisplayRanks();
  }, []);

  const DisplayRanks = () => {

      axios.get('http://127.0.0.1:5000/10Hard')
        .then(response => {
          setRanking(response.data); // Assuming the scores are in the "data" property
        })
        .catch(error => {
          console.log(error);
        });
  }

  return (
    <div className="overlay">
      <div className="button" onClick={() => setShowRank(false)}>
        X
      </div>
      <div className="content">
        <div className="top-title">
          <div>Top</div>
          <div>Name</div>
          <div>Score</div>
        </div>
        <div className="ranks">
          {ranking.map((user, index) => (
            <UserRank
              typeUser={index === 0 ? "user-a" : "user-b"}
              numRank={index + 1}
              name={user.username}
              score={user.score}
            />
          ))}
        </div>
      </div>
    </div>
  )
}

export default Ranking;