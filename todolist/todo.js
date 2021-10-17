//one single row in our To Do List
//All we want from the ToDo component is the actual task that is on our list.
//We will also need to make use of the complete property on the todo object to 
//indicate whether or not something is decorated with a strikethrough.

import React from 'react';

const ToDo = ({todo, handleToggle}) => {
    e.preventDefault();
    handleToggle(e.currentTarget.id)
}
    return (
        //adding a class helps with styling and is set as equal to the js expression asking if the todo is complete
        <div id ={todo.id} key ={todo.id + todo.task} name = 'todo' value = 'todo.id' onClick ={handleClick}
        className = {todo.complete ? 'todo strike' : 'todo'}> 
            {todo.task}
        </div>
    );
};

export default ToDo;