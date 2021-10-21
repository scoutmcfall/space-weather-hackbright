'use strict';

class DoList extends React.Component{
    constructor(props){
        super(props);
        this.state = {value: ""};
        this.id = {key: ""}

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value : event.target.value});
    }

    handleSubmit(event) {
        const todo = this.state.value;
        alert("todo submitted:" + this.state.value);
        event.preventDefault();
        console.log(todo);

    }

    render() {
        return <React.Fragment>
            <form onSubmit = {this.handleSubmit}>
                <label> 
                What to do:
                <input type = "text" value = {this.state.value} onChange = {this.handleChange} placeholder = "do a thing" />
                </label>
                <input type = "submit" value = "add to-do" />
            </form>
        </React.Fragment>
    }
}

ReactDOM.render(<DoList />, document.getElementById('todolist'));