'use strict';

//this is a component
function ListItem(props) {
  //make a listitem object out of userInput
    //function to clear the task from the array on click
    const clearTask = (evt) => {
      evt.preventDefault();
      console.log(props.listItems);
      props.listItems.pop(evt.target.value);//part of the state of todolist parent
      console.log(props.listItems);
    }
  return (<div className = "todo">
    {/* <p>key = {props.key}</p> */}
    
    <p><button onClick = {clearTask} value = {props.task} done = {false}> {props.task}</button></p>
  </div>
  );

}

//add a property of done or not done
//parent component has a function that evaluates every object in my list
//and takes out/pops the ones which are done


//this is a component
function ToDoList() {

  //this is a hook
  const [userInput, setUserInput] = React.useState('');
  
  //this is a big arrow function
  const handleChange = (evt) => {
    setUserInput(evt.target.value);
    console.log(userInput);
  }

  //this is a hook
  const [listItems, setListItems] = React.useState([]);

  //another big arrow function
  const handleSubmit = (evt) => {
    evt.preventDefault();
    //call set list items to update the list items array by adding the userinput
    setListItems((listItems) => [...listItems, userInput]); //js spread operator
    console.log(listItems);
    console.log(typeof(listItems));
    console.log(evt);
    setUserInput('');
  }
  // const listObjects = [];
  // for (const currentListItem of listItems) {
  //     listObjects.push(
  //       <ListItem
  //       task = {currentListItem.task}
  //     />
  //       );
  // }


//return a react fragment containing ListItem in the return statement
  return <React.Fragment>
    {/* //form getting userInput */}
      <form onSubmit = {handleSubmit}>
        <input type = "text" value = {userInput} placeholder = "do more" onChange = {handleChange} />
        <button type = "submit">add item</button>
      </form>
    {/* //up to date list */}
      <div className = "todo">To-Do List:
      {/* user .map method on the list, copies each element in a list but can also pass it a callback fxn
      that tells it what each copy should look like so you can create elements */}

        
    <ul>
      {listItems.map((listItem, index) => (
        <ListItem key = {index}task = {listItem} listItems = {listItems} /> //can add more properties to it if i need to
        // <p><button onClick = {clearTask} value = {listItem}> {listItem}</button></p>
      ))}
    </ul>
        

{/* 
        <button onClick = {clearTask} value = {listItems}>{listItems}</button>
        <ListItem task = {userInput} /> */}
      </div>
       
      </React.Fragment>
  }

ReactDOM.render(<ToDoList />, document.getElementById('todolist'));


// ---------------------------------------

// //function for the form
// function Form(props) { //should props be in there instead of userInput?

//   const [userInput, setUserInput] = React.useState('');
  
//   const handleChange = (evt) => {
//     setUserInput(evt.target.value);
//   }

//   const handleSubmit = (evt) => {
//     evt.preventDefault();
//     //pass the userInput to the ListItem function as props? 
//     ListItem(evt.target.value);
//     setUserInput('');
//   }
// }
// ---------------------------------------

// function ToDo(props) {
   
//     return (
//       <div className="todo">
//         <p>Id: {props.id} </p>
//         <p>Task: {props.task}</p>
//       </div>
//     );
//   }
  

// function ToDoListContainer() {
     
//   const exampleToDo = ["a task"];
//   const toDoList = [];
  
//   // for (const currentToDo of userInput) {
//   //   console.log(currentToDo);
//   //   toDoList.push(currentToDo);
//   //   console.log(toDoList);
//   // }
//     // make an example that tells state what to do
//     // const exampleToDo = {
//     //   id: 'Id',
//     //   task: 'Example',
//     // };
    
// //     const [toDos, setToDos] = React.useState([exampleToDo]);
// const setUserInput = (evt) => {

// }
 
// // // set empty state for form
//     const [userInput, setUserInput] = React.useState('');

// // //fxn to handle change to the form
//   const handleChange = (evt) => {
//     setUserInput(evt.target.value);
//   }

// // //put form contents in array, then render todo objs from the array
// //     // const toDos = []
// //     const addTask = () => {
// //       // is passed the form contents via handlesubmit
// //       // put form contents into list called toDos
// //       toDos.push(userInput);
// //     }

// // // fxn to handle submit form that gets the user input
//     const handleSubmit = (evt) => {
//         evt.preventDefault();
//         // addTask(userInput);
//         toDoList.push(userInput);
//         // reset the form to empty.
//         setUserInput('');
//     }
       

// //  // make an array of todo components to render
// //    const toDosToRender = [];
// //    for (const currentToDo of toDos) {
// //      console.log(currentToDo.toDoId)
// //      toDosToRender.push(
// //        <ToDo
// //          key={currentToDo.toDoId}
// //          task={currentToDo.task}
// //        />
// //      );
// //    }


// //   here's what this whole container renders: should be the up to date todo list
//     return <React.Fragment>
//       <div className = "todo"> {toDoList}</div>
//         {/* <div className="todo">{toDosToRender}</div> */}
//         (<form onSubmit = {handleSubmit}>
//             <input value = "userInput" type = "text" placeholder = "do more" onChange = {handleChange}/>
//             <button type = "submit">do it</button>
//         </form>);
//         </React.Fragment>
//   }
  