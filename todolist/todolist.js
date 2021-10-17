//the container that holds all of our todos
import React from 'react';
import ToDo from './ToDo';
 
//pass down the functions from app.s as props to this child component 
const ToDoList = ({toDoList, handleToggle, handleFilter}) => {
   return (
       <div>
           {toDoList.map(todo => {
               return (
                   <ToDo todo={todo} handleToggle = {handleToggle} handleFilter = {handleFilter}/>
               )
           })}
           <button style = {{margin : '20px'}} onClick ={handleFilter}>Clear Completed Tasks</button>
       </div>
   );
};
 
export default ToDoList;
