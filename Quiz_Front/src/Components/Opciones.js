// Final Project: Quiz Application with Microservices
// Date: 29-May-2023
// Authors:
//          A01752030 Juan Pablo Castañeda Serrano
//          A0752221 Omar Rodrigo Talavera Becerra
//          A01752013 Nadia Paola Ferro Gallegos
////////////////////////////////////////////////////////////////////////////////////
/*
Opciones.js
Create a table of options to the quiz
*/

import { useState } from 'react';
import '../Styles/Options.css';

const Opciones = (props) => {
  const { Text, onClick } = props;
  const [selected, setSelected] = useState(false);

  const handleClick = () => {               //function to select an answer
    setSelected(true);
    onClick();
  };

  return (
    <div className="opt">
      <div onClick={handleClick}>
        {Text}
      </div>
      <div className="checker">
        <input name="radio" type="radio" className="input" checked={selected} readOnly />
      </div>
    </div>
  );
};

export default Opciones;