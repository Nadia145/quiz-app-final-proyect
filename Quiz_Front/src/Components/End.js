// Final Project: Quiz Application with Microservices
// Date: 29-May-2023
// Authors:
//          A01752030 Juan Pablo Castañeda Serrano
//          A0752221 Omar Rodrigo Talavera Becerra
//          A01752013 Nadia Paola Ferro Gallegos
////////////////////////////////////////////////////////////////////////////////////
/*
End.js
Show to the user the score, and the button to show the global ranking
*/
import { useState } from "react";
import "../Styles/End.css";
import Ranking from "./Ranking";
import axios from 'axios';

const End = (props) => {
    const [showRank, setShowRank] = useState(false);
    const {Score, setScore} = props;
    const {Username,setUsername} = props;
    const {Dificultad} = props;
    const {Total} =props;


    function generateRandomString() {         //Create a random id to the user
        let result = '';
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        const charactersLength = characters.length;
      
        for (let i = 0; i < 10; i++) {
          const randomIndex = Math.floor(Math.random() * charactersLength);
          result += characters.charAt(randomIndex);
        }
      
        return result;
      }    

    const id = generateRandomString()  
    
    const dataUser = {                            //Create the datas for the DB
        "_id": id,
        "username": Username,
        "score": Score,
        "dificultad": Dificultad
      };

    axios.post('http://127.0.0.1:5000/AddUser', dataUser)
      .then(response => {
        console.log('Data added successfully');
      })
      .catch(error => {
        console.error('Error adding data:', error);
      });  




  return (
    <div className="overlay">
        <div className="contenedor">
            <div className="congratulations">
                <h1>¡¡¡ Thanks for playing !!!</h1>
            </div>
            <div className="score">
                <div >Tu puntaje fue:</div>
                <div className="score-points">{Score} de {Total}</div>
            </div>
            <div className="btm">
                <div className="btn" onClick={()=>window.location.reload()}>Terminar</div>
                <div className="btn" onClick={()=>setShowRank(true)}>Ranking</div>
                {showRank &&(
                    <Ranking setShowRank={setShowRank} dificultad = {Dificultad} />
                )}
            </div>
        </div>
    </div>
  )
}

export default End;