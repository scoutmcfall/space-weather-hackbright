//a basic form that will allow for a user to input a task name, hit enter or click on a button, 
// and have a function fire to add the task. For a form to work correctly we have to keep track of the 
// changes as we go, so logically we have to handle what happens as the input changes.

// There are four main things that we need to have to make our forms work:

// Local state (so we will need to employ the useState() hook)
// Our form component with an input value that is assigned to the correct variable
// A function that handles the state’s changes
// A function to handle the form submission
import React from 'react';
import React, { useState } from 'react';

const toDoForm = ({addTask}) =>{
const [userInput, setUserInput] = useState('');

const handleChange = (e) => {
    setUserInput(e.currentTarget.value)
}

//When a user hits ‘Enter’ or clicks the 
//‘Submit’ button, this function will fire to add the task to the toDoList array.
const handleSubmit = (e) => {
    e.preventDefault();
    addTask(userInput);
    //the next line will set the form back to an empty input.
    setUserInput('');
}
//a form component that encapsulates an input and a button
//value should match the state variable (userInput)
return (
    <form onSubmit = {handleSubmit}>
    <input value={userInput} type = 'text' onChange ={handleChange} placeholder = 'whatcha gonna do' />
    </form>
    );
};
export default toDoForm;