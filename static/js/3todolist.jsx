'use strict';


function Todo(){
    //set the todos state as empty array
    const [todos, setTodos] = React.useState([]);
    //set the new item state as empty string
    const [newTodo, setNewTodo] = React.useState("");
    //fxn that saves new todo strings in local storage as json
    const saveData = (newTodos) =>{
        localStorage.setItem("todos", JSON.stringify(newTodos));
    };
    //useeffect if statement gets json in storage and makes it js again
    //then sets state based on the info stored
    React.useEffect(() => {
        if (localStorage.getItem("todos")) {
            setTodos(JSON.parse(localStorage.getItem("todos")));
        }
    }, []);
    //big arrow fxn, trim removes whitespace, updates new todos array with the user input
    // with the attributes todo and id (set as the date)
    //sets a new state including the new todo
    //resets the form as empty
    //and saves the data in local storage
    const addTodo = () => {
        if (newTodo.trim()) {
            let newTodos = [...todos, { todo: newTodo.trim(), id: Date.now()}];
            setTodos(newTodos);
            setNewTodo("");
            saveData(newTodos);
        }
    };
//takes in the id(date) and creates a new newtodos array excluding todos with the argument id
//sets a new state with the new newtodos array
//then saves the data in local storage
    const deleTodo = (id) => {
        let newTodos = todos.filter((todo) => todo.id !== id);
        setTodos(newTodos);
        saveData(newTodos);
    };
    //here's what's actually rendered on the page:
    return (
        <div class="container">
	    <div class="d-flex justify-content-center h-100">
		<div class="card">
        <div>
        <h2>To-Do List:</h2>
        <table>
            <thead>
                <tr>
                    <th>
                        <input
                        type = "text"
                        id = "todoinput"
                        className = "formcontrol"
                        placeholder = "do more"
                        value = {newTodo}
                        onChange = {(e) => setNewTodo(e.target.value)}
                        />
                    </th>
                    <th> 
                        <button className = "btn btn-outline-light" onClick = {addTodo} >
                            {" "}
                            Add
                            </button>
                    </th>
                </tr>
            </thead>
            <thead>
          <tr>
            <th scope="col" colSpan="2">
              Tasks:
            </th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody id = "table">
            {todos.map((todo) => (
                <tr key = {todo.id}>
                    <td>{todo.todo}</td>
                    <td>
                        <button className = "btn btn-outline-light"  onClick = {() => deleTodo(todo.id)}>
                            {" "}
                            Delete{" "}
                            </button>{" "}
                    </td>
                </tr>
            ))}
        </tbody>
    </table>
    </div>
    </div>

    </div>
    </div>

    );
}

// export default Todo;


ReactDOM.render(<Todo />, document.getElementById('todolist'));