// Final Project: Quiz Application with Microservices
// Date: 29-May-2023
// Authors:
//          A01752030 Juan Pablo Castañeda Serrano
//          A0752221 Omar Rodrigo Talavera Becerra
//          A01752013 Nadia Paola Ferro Gallegos
////////////////////////////////////////////////////////////////////////////////////
/*
UserRank.js
show the top number, name and score
*/
import "../Styles/UserRank.css";

const UserRank = (props) => {
    const {typeUser,numRank,name,score}=props;

  return (
    <div className={typeUser}>
        <div>{numRank}</div>
        <div>{name}</div>
        <div>{score}</div>
    </div>
  )
}

export default UserRank;