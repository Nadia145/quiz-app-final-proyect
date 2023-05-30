// Final Project: Quiz Application with Microservices
// Date: 29-May-2023
// Authors:
//          A01752030 Juan Pablo Castañeda Serrano
//          A0752221 Omar Rodrigo Talavera Becerra
//          A01752013 Nadia Paola Ferro Gallegos
////////////////////////////////////////////////////////////////////////////////////
/*
Pregunta.js
obtain the questions and the posible answers

*/

import React, { useState,useEffect } from 'react';
import '../Styles/Preguntas.css';
import Opciones from './Opciones';
import Check from './Check';
import axios from 'axios';

const Pregunta = (props) => {
  const { numQuestions, setShowPregunta } = props;
  const {username, setUsername} = props;
  const [score,setScore] = useState(0);
  const [Q,setQ] = useState('')
  const [A0,setA0]= useState('')
  const [A1,setA1]= useState('')
  const [A2,setA2]= useState('')
  const [A3,setA3]= useState('')
  const [dificultad,setdificultad] = useState('')
  const [cont, setCont] = useState(0);
  const [lastQuestion, setLastQuestion] = useState(true);
  const [showCheck, setShowCheck] = useState(false);
  const [randArr, setrandArr] = useState([1,2,3,4])
  const [selectedOption, setSelectedOption] = useState(null);


  useEffect(() => {             //Create an array of answers 
    fetchData();
  }, []);

  function scrambleArray(array) {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
  }

  function getRandomNumber(max) {
    return Math.floor(Math.random() * max);
  }
  const fetchData = () => {                 //Get the number of questions
    setrandArr(scrambleArray(randArr))
    console.log(randArr)
    if (numQuestions < 5){
      setdificultad("hard")
      const url = 'http://127.0.0.1:5000/hardqs';
      axios.get(url)
      .then(response => {
        // Handle the response data
        const RQ = getRandomNumber(numQuestions)
        setQ(response.data[0][RQ])
        setA0(response.data[1][RQ].correct_answer);
        setA1(response.data[1][RQ].incorrect_answer[0])
        setA2(response.data[1][RQ].incorrect_answer[1])
        setA3(response.data[1][RQ].incorrect_answer[2])
      })
      .catch(error => {
        // Handle any errors that occurred during the request
        console.error(error);
      });
  }else if(numQuestions >= 5 && numQuestions <= 7){
    setdificultad("medium")
    const url = 'http://127.0.0.1:5000/mediumqs';
    const RQ = getRandomNumber(numQuestions)
    axios.get(url)
    .then(response => {
      // Handle the response data
      setQ(response.data[0][RQ])
      setA0(response.data[1][RQ].correct_answer);
      setA1(response.data[1][RQ].incorrect_answer[0])
      setA2(response.data[1][RQ].incorrect_answer[1])
      setA3(response.data[1][RQ].incorrect_answer[2])
    })
    .catch(error => {
      // Handle any errors that occurred during the request
      console.error(error);
    });
  }else{
    setdificultad("easy")
    const url = 'http://127.0.0.1:5000/easyqs';
    axios.get(url)
    .then(response => {
      // Handle the response data
      const RQ = getRandomNumber(numQuestions)
      setQ(response.data[0][RQ])
      setA0(response.data[1][RQ].correct_answer);
      setA1(response.data[1][RQ].incorrect_answer[0])
      setA2(response.data[1][RQ].incorrect_answer[1])
      setA3(response.data[1][RQ].incorrect_answer[2])
    })
    .catch(error => {
      // Handle any errors that occurred during the request
      console.error(error);
    });
  };  
    }
  

  const contQuestionChange = () => {          //Count the number of questions
    if (cont  >= numQuestions -2) {
      setLastQuestion(false);
    }
    setCont(cont + 1);
  };

  function ScoreChange(correct){              //Get and update the score of the user
    console.log(score)
    setScore(score + 1)

  }

  return (
    <div className="overlay">
      <div className="contenedor">
        <h1>
          {Q}<br/>
          Pregunta {cont+1}/{numQuestions}<br/>
          Tu dificultad es {dificultad}

        </h1>
        <div className="incs">
        <Opciones
         Text={A0.replace(/\d+$/, randArr[0])}
         onClick={() => setSelectedOption(randArr[0])}
        />
        <Opciones 
        Text={A1.replace(/\d+$/, randArr[1])} 
        onClick={() => setSelectedOption(randArr[1])}
        />
        <Opciones 
        Text={A2.replace(/\d+$/, randArr[2])} 
        onClick={() => setSelectedOption(randArr[2])}
        />
        <Opciones 
        Text={A3.replace(/\d+$/, randArr[3])} 
        onClick={() => setSelectedOption(randArr[3])}
        />
        </div>
        <div className="btmt">
          <div className="btnt" onClick={() => setShowCheck(true)}>
            Checar
          </div>
          {console.log(selectedOption)}
          {showCheck && (
            <Check 
              setShowCheck={setShowCheck}
              contQuestionChange={contQuestionChange} 
              fetchdata = {fetchData}
              setShowPregunta={setShowPregunta}
              lastQuestion={lastQuestion}
              ScoreChange = {ScoreChange}
              score = {score}
              selectedOption={`A${selectedOption}`}
              correctAnswer = {A0}
              username = {username}
              Qnum = {numQuestions}
              dificultad = {dificultad}
            />
          )}
        </div>
      </div>
    </div>
  );
};

export default Pregunta;
