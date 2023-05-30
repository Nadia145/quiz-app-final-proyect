// Final Project: Quiz Application with Microservices
// Date: 29-May-2023
// Authors:
//          A01752030 Juan Pablo Castañeda Serrano
//          A0752221 Omar Rodrigo Talavera Becerra
//          A01752013 Nadia Paola Ferro Gallegos
/*
Button.js
Is a special button to start the quizz, thus button posees a animation and a condition.
That only apears when the name and numQuestions are diferent of " "(null).
*/

import React from 'react';
import '../Styles/Button.css';

const Button = (props) => {
  const { type, text, content, onClick } = props;

  return (
    <div className={type} onClick={onClick}>
      <h1 className={content}>
        {text}
      </h1>
    </div>
  );
};

export default Button;
