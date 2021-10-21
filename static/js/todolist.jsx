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
     
  const exampleToDo = ["a task"];
  const toDoList = [];
  
  // for (const currentToDo of userInput) {
  //   console.log(currentToDo);
  //   toDoList.push(currentToDo);
  //   console.log(toDoList);
  // }
    // make an example that tells state what to do
    // const exampleToDo = {
    //   id: 'Id',
    //   task: 'Example',
    // };
    
//     const [toDos, setToDos] = React.useState([exampleToDo]);
   
 
// // set empty state for form
//     const [userInput, setUserInput] = React.useState('');

// //fxn to handle change to the form
  const handleChange = (evt) => {
    setUserInput(evt.target.value);
  }

// //put form contents in array, then render todo objs from the array
//     // const toDos = []
//     const addTask = () => {
//       // is passed the form contents via handlesubmit
//       // put form contents into list called toDos
//       toDos.push(userInput);
//     }

// // fxn to handle submit form that gets the user input
    const handleSubmit = (evt) => {
        evt.preventDefault();
        // addTask(userInput);
        toDoList.push(userInput);
        // reset the form to empty.
        setUserInput('');
    }
       

//  // make an array of todo components to render
//    const toDosToRender = [];
//    for (const currentToDo of toDos) {
//      console.log(currentToDo.toDoId)
//      toDosToRender.push(
//        <ToDo
//          key={currentToDo.toDoId}
//          task={currentToDo.task}
//        />
//      );
//    }


//   here's what this whole container renders: should be the up to date todo list
    return <React.Fragment>
      <div className = "todo"> {toDoList}</div>
        {/* <div className="todo">{toDosToRender}</div> */}
        (<form onSubmit = {handleSubmit}>
            <input value = "userInput" type = "text" placeholder = "do more" onChange = {handleChange}/>
            <button type = "submit">do it</button>
        </form>);
        </React.Fragment>
  }
  

ReactDOM.render(<ToDoListContainer />, document.getElementById('todolist'));