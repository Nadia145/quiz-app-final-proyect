import React, { useState } from 'react';
import './App.css';
import Button from './Components/Button';
import "./Styles/Start.css";
import Pregunta from './Components/Pregunta.js';

function App() {
  const [name, setName] = useState('');
  const [numQuestions, setNumQuestions] = useState('');
  const [showPregunta, setShowPregunta] = useState(false);

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handler = (event) => {
    const value = event.target.value;
    if (/^[1-9]|10$/.test(value)) {
      setNumQuestions(value);
    }
  };

  

  const isFormValid = name.trim() !== '' && numQuestions.trim() !== '';

  return (
    <div className='App-header'>
      <div className='Instrucciones'>
        <h1>Instrucciones</h1>
        <p>
          A continuación presentarás un quiz. La cantidad de preguntas que desees contestar
          será inversamente proporcional a la dificultad de las mismas <br/>
          1-4 preguntas serán difíciles<br/>
          5-7 preguntas serán medias<br/>
          8-10 preguntas serán fáciles<br/>
          Para iniciar el Quiz, por favor ingresa tu nombre y la dificultad.
        </p>
      </div>
      <div>
        <input
          placeholder="Nombre"
          className="Ints"
          name="name"
          type="text"
          value={name}
          onChange={handleNameChange}
        />
      </div>
      <div>
        <input
          placeholder="# Preguntas"
          className="Ints"
          name="numQuestions"
          type="text"
          value={numQuestions}
          onChange={handler} 
          pattern="^[1-9]|10$"
        />
      </div>
      {isFormValid && (
        <div>
          <Button
            type="Button-start"
            text="START"
            content="start-content"
            onClick={() => setShowPregunta(true)}
          />
          {showPregunta && (
            <Pregunta numQuestions={numQuestions} setShowPregunta={setShowPregunta}/>
          )}
        </div>
      )}
    </div>
  )
};

export default App;
////////////////////////////////////////////////