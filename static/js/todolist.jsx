'use strict';

// const { array } = require("prop-types");

//this is a component
function ListItem(props) {
  //make a listitem object out of userInput
  // props.listItems.push(props);
  //pass a fxn to this component from the parent
  
  console.log(props.listItems)

    const markDone = (evt) => {
      evt.preventDefault();
      console.log("this is evt target value");
      console.log (evt.target.value);
      // setDoneItems(evt.target.value);
      console.log(props.doneItems);
      console.log(props.setDoneItems);
      // props.setDoneItems((doneItems) => [...props.doneItems, evt.target.value]);
      console.log("this is props.task:");
      // console.log(doneItems);
      //takes in a key
      //eventually i will want to make this a toggle fxn
      console.log(props.task);
      evt.target.done = 'true';
      console.log(evt.target.value);
    }
  return (<div className = "list">    
      {/* <button onClick={() => markDone(props.key)} value = {props.task} className = "btn btn-outline-light"> {props.task}</button> */}
      <button onClick = {()=>{props.doneToDo(props.idx)}} done = {props.done} className = "btn btn-outline-light"> {props.task}</button>

  </div>
  );
}

//this is a component
function ToDoList() {
  const doneToDo = (idx) => {
    //pass in the key prop from where i'm rendering the todo item
    console.log("this is the idx");
    console.log(idx);
    const  newList = listItems.filter((item, index) => {
     if (index !== idx) {
      return item;
     }
    //new list excludes the item at the idx
    setListItems(newList);
    console.log(newList);

    })}
  //useEffect takes in a fxn to run whenever a change is made in the dependency array
  // const todo = React.useEffect(
  //   <ul className = 'list'>
  //   {listItems.map((listItem, index) => (
  //     <ListItem key = {index} task = {listItem.task} listItems = {listItems} className = 'false' doneItems = {doneItems} setDoneItems = {setDoneItems}/> 
  //     //can add more properties to it if i need to
  //   ))}
  // </ul>
  // )
  
  //this is a hook
  const [userInput, setUserInput] = React.useState('');
  
  //this is a big arrow function
  const handleChange = (evt) => {
    setUserInput(evt.target.value);
    // console.log(userInput);
  }

  //this is a hook
  const [listItems, setListItems] = React.useState([]);
  const [doneItems, setDoneItems] = React.useState([]);
  


  //for some reason the last two tasks from the list 
  //items array are being cleared instead of the completed task
  // const doneItems = [];
  const clearDone = (evt) => {
    //use filter to return a new and filtered list
    console.log(listItems); //an array of strings
    //filter fxn takes in each item from the original array and makes  
    //new array of the ones where the boolean returns true
    const newList = listItems.filter((item) => {
      console.log("item.done:")
      console.log(item.done)
      return item.done !== true;
    });
    console.log(newList);
    setListItems(newList);
  }

  // listItems.filter(item => item.includes('true')).map(filteredItem => (
  //   <li>
  //     {filteredItem}
  //   </li>
  // ))

    // for (let item of listItems) {
    //     if (item.className == 'true');
    //       // console.log (item);
    //       doneItems.push({item});
    //       // listItems.pop({item});
    //       console.log(listItems);
    // }
  // }

  //another big arrow function
  const handleSubmit = (evt) => {
    evt.preventDefault();
    //call set list items to update the list items array by adding the userinput
    setListItems((listItems) => [...listItems, {task: userInput, done: false}]); //js spread operator
    // console.log(listItems);
    // console.log(typeof(listItems));
    // console.log(evt);
    setUserInput('');
  }

//return a react fragment containing ListItem in the return statement
    return <React.Fragment>

      {/* //form getting userInput */}
        <form onSubmit = {handleSubmit} className = "form-control form-control-lg">
          <input type = "text" value = {userInput} placeholder = "do more" onChange = {handleChange} />
          <p>
            <button type = "submit" className = "btn btn-outline-light">add item</button>
            </p>
        </form>
      {/* //up to date list */}
        <div className = "todo"><h1>To-Do List:</h1>
        {/* user .map method on the list, copies each element in a list but can also pass it a callback fxn
        that tells it what each copy should look like so you can create elements */}

      <ul className = 'list'>
        {listItems.map((listItem, index) => (
          <ListItem key = {index} idx = {index} task = {listItem.task} listItems = {listItems} className = 'false' doneToDo = {doneToDo}/> 
          //can add more properties to it if i need to
        ))}
      </ul>
      {/* <p><button onClick = {clearDone} value = 'clear completed' key ={listItem.key} > clear completed </button></p> */}
      <p><button onClick = {clearDone} value = 'clear completed' > clear completed </button></p>

        </div>
        
        </React.Fragment>
  }

ReactDOM.render(<ToDoList />, document.getElementById('todolist'));
