import './App.css';
import Numberbox from './components/Numberbox';
function App() {
  return (
   
    <div  className='formcontainer' align="center">
      <div className='formcontainer1'>
      <br></br><br></br>
      <h1>Guess the Number!</h1>
      <p>Guess a number from 1 to 100</p>
      <Numberbox/><br/>
      </div>
    </div>
   
  );
}

export default App;
