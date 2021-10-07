'use strict';

function Homepage() {
  return <div>
    <p>Welcome!</p>
    <a href = "/cards.html">click here</a>
    <img src="/static/img/balloonicorn.jpg" height="15000" width="100"></img>
  </div>;
}

ReactDOM.render(<Homepage />, document.querySelector('#app'));