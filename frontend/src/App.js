import React from 'react';
import Button  from '@material-ui/core/Button';

function App() {
  // Log hello world to the console when the button is clicked
  function my_logger() {
  console.log("second try");
  } 

  return (
    <div className="App">
        <Button  variant="contained" color="primary" onClick={my_logger}>hello World</Button>
    </div>
  );
}

export default App;
