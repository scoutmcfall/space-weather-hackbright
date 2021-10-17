//state logic is held here and passed down to children components 
import React from 'react';
import React, { useState } from 'react';
import './todolist.css';
import data from “./data.json”;
// basic syntax for useState:
// const [ variable, setVariable ] = useState(<initState?>); 

//components
import Header from "./Header";
import ToDoList from "./ToDoList";
import toDoForm from "./todoForm";

function App() {
  const [ toDoList, setToDoList ] = useState(data);
  //when a user clicks on a task, we want to change the state of complete to true if it’s false or vice versa
  //pass in the id of the item that was clicked
  const handleToggle=(id) => {
      let mapped = toDoList.map(task =>{
          return task.id == id ? {...task, complete: !task.complete}
      });
      setToDoList(mapped);
      //Mapping over the toDoList creates a new array
  }
  //delete completed items: take the toDoList and filter through it, 
  //return all items that are not completed, and then set the filtered array onto toDoList.
  const handleFilter = () => {
      let filtered = toDoList.filter(task =>{
          return !task.complete;
      });
      setToDoList(filtered);
  }

  //This function takes in userInput that we gathered from our form component’s state.
  const addTask = (userInput) =>{
        let copy = [...toDoList];
        //reassign copy to a new array, with copy spread in and the new list item tagged on the end.
        copy = [...copy, {id: toDoList.length + 1 , task:userInput, complete: false}];
        setToDoList(copy);
  }
 return (
   <div className="App">
     <Header />
     <ToDoList toDoList={toDoList} handleToggle = {handleToggle} handleFilter = {handleFilter}/>
     <ToDoForm addTask ={addTask}/>
   </div>
 );
}
 
export default App;