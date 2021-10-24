'use strict';

//this is a component
function ListItem(props) {
  //make a listitem object out of userInput
  // props.listItems.push(props);
  // console.log(props.listItems)

    const markDone = (evt) => {
      evt.preventDefault();
      //marks the done prop as true
      //eventually i will want to make this a toggle fxn
      // console.log(props.listItems);
      evt.target.value = 'good job!';
      evt.target.className = 'true';
      console.log(evt.target.className);
    }
  return (<div className = "todo">    
    <p>
      <button onClick = {markDone} value = {props.task} className = 'false'> {props.task}</button>
    </p>
  </div>
  );
}

//this is a component
function ToDoList() {
  
  //this is a hook
  const [userInput, setUserInput] = React.useState('');
  
  //this is a big arrow function
  const handleChange = (evt) => {
    setUserInput(evt.target.value);
    // console.log(userInput);
  }

  //this is a hook
  const [listItems, setListItems] = React.useState([]);


  //for some reason the last two tasks from the list 
  //items array are being cleared instead of the completed task
  const doneItems = [];
  const clearDone = (evt) =>{
    for (let item of listItems) {
        if (item.className == 'true');
          // console.log (item);
          doneItems.push({item});
          listItems.pop({item});
          //i think i need to map the list in order to remove items from it?
          console.log(listItems);
    }
  }

  //another big arrow function
  const handleSubmit = (evt) => {
    evt.preventDefault();
    //call set list items to update the list items array by adding the userinput
    setListItems((listItems) => [...listItems, userInput]); //js spread operator
    // console.log(listItems);
    // console.log(typeof(listItems));
    // console.log(evt);
    setUserInput('');
  }

//return a react fragment containing ListItem in the return statement
  return <React.Fragment>
    {/* call clear done each time I render? */}

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
        <ListItem key = {index}task = {listItem} listItems = {listItems} className = 'false'/> //can add more properties to it if i need to
      ))}
    </ul>
    <p><button onClick = {clearDone} value = 'clear completed'> clear completed </button></p>

      </div>
       
      </React.Fragment>
  }

ReactDOM.render(<ToDoList />, document.getElementById('todolist'));



  