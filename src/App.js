import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';


function App() {
  const [isListening, setisListening] = useState(false);

  return (
    <div className="App">
      <header className="App-header">
        <div className="hed">

        <h1>voiceGPT</h1>
        <div className='adil'>

          <input type="text" id="text" />
          {/* <input type="button" id="voice" value="&#127897;" onClick={()=>{setisListening(true)}}/> */}

          { !isListening ?  <input type="button" id="voice" value="&#127897;" onClick={()=>{setisListening(true)}}/> :  <input type="button" id="voice" value="&#128721;" onClick={()=>{setisListening(false)}}/>  }


        </div>
        
        {isListening ? <div style={{fontSize: ".9rem" }} id="notification">Listening</div>  :  <div style={{fontSize: ".9rem" }} id="notification">Not Listening</div>} 
         
        
         
         

        </div>


        <div className="out">
          {/* <p>blahh</p>
          <p>blahhhhh</p>
          <p>adil</p>
          <p>adil</p>
          <p>adil</p>
          <p>adil</p>
          <p>adil</p>
          <p>adil</p> */}

        </div>
        </header>
          <footer>&copy; Adil Saju</footer>
    </div>
  );
}

export default App;
