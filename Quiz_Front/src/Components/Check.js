// Final Project: Quiz Application with Microservices
// Date: 29-May-2023
// Authors:
//          A01752030 Juan Pablo Castañeda Serrano
//          A0752221 Omar Rodrigo Talavera Becerra
//          A01752013 Nadia Paola Ferro Gallegos
////////////////////////////////////////////////////////////////////////////////////
/*
Check.js
This part tell to the user if the coice is correct
*/

import React, { useState,useEffect } from 'react';
import '../Styles/Check.css';
import End from './End';


const Check = (props) => {
const { setShowCheck, contQuestionChange, ScoreChange, lastQuestion,fetchdata,selectedOption, correctAnswer,score,username,Qnum,dificultad } = props;
  const [showEnd, setShowEnd] = useState(false);

  useEffect(() => {
    if (selectedOption === 'A1') {
      ScoreChange(); // Call ScoreChange function if the selectedOption is 1 (correct answer)
    }
  }, []);  

  console.log(selectedOption)

  const handleNext = () => {              //Close the review and pass to the next question

      setShowCheck(false);
      contQuestionChange();
      fetchdata();
  };

  const handleTerminar = () => {          //Open the End.js
    //setShowPregunta(false);
    fetchdata();
    setShowEnd(true);
  };

  return (
    <div className="overlay">
      <div className="contenedor">
        <h1>Retroalimentación</h1>
        <div className="check">
        {selectedOption === 'A1' ? (
            <div>Well done!</div>
            
          ) : (
            <div>
              You were wrong, the correct answer was: {correctAnswer}
            </div>
          )}
        </div>
        <div className="btmt">
          {lastQuestion ? (
            <div className="btnt" onClick={handleNext}>
              Siguiente
            </div>
          ) : (
            <div className="btnt" onClick={handleTerminar}>
              Terminar
            </div>
          )}
          {showEnd && (
            <End 
            Score = {score}
            Username = {username}
            Total = {Qnum}
            dificultad = {dificultad}
            />
          )}
        </div>
      </div>
    </div>
  );
};

export default Check;
