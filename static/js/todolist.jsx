'use strict';


function ToDo(props) {
   
    return (
      <div className="todo">
        <p>Id: {props.id} </p>
        <p>Task: {props.task}</p>
      </div>
    );
  }
  


function ToDoListContainer() {
       
    // make an example that tells state what to do
    const exampleToDo = {
      id: 'Id',
      task: 'Example',
    };
    const [toDos, setToDos] = React.useState([exampleToDo]);
   
 
// set empty state for form
    const [userInput, setUserInput] = React.useState('');

//put form contents in array, then render todo objs from the array?
    const addTask = () => {
      // get form contents 
      // put form contents into list called toDos
    }

// fxn to handle submit form that gets the user input
    const handleSubmit = () => {
        React.createElement.preventDefault();
        addTask(userInput);
        // reset the form to empty.
        setUserInput('');
    }
       

 // make an array of todo components to render
   const toDosToRender = [];
   for (const currentToDo of toDos) {
     toDosToRender.push(
       <ToDo
         key={currentToDo.toDoId}
         task={currentToDo.task}
       />
     );
   }


//   here's what this whole container renders: should be the up to date todo list
    return <React.Fragment>
        <div className="todo">{toDosToRender}</div>
        (<form onSubmit = {handleSubmit}>
            <input value = {userInput} type = "text" placeholder = "do more" />
        </form>);
        {/* <h1 style={{ color: 'white' }}>I'm in the return statement! Can you hear me?</h1> */}
        </React.Fragment>
  }
  

ReactDOM.render(<ToDoListContainer />, document.getElementById('todolist'));