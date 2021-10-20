'use strict';

function Todolist(){
    const [todolist, settodolist] = useState()
    
    const todo = [];
    
    const Header = () => {
        return (
            <header>
                Now that you know the space weather, what are you going to do?
            </header>
            )
    }
    // return <div>This is where my component goes</div>
}   //i can wrap everything i'm returning in a <React.Fragment>

function Todo(props) {
    // this is a child element of the list container 
    // it is passed the props from the todolist
    // the todolist keeps track of the state

}

ReactDOM.render(<Todolist />, document.querySelector("#todolist"));