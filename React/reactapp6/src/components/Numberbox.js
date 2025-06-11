import './Numberbox.css';
import { useState } from "react";

function Numberbox() {
    const [number, setNumber] = useState(null);
    const [guess, setGuess  ] =useState(null);
    const [result, setResult ] = useState(null);
    const [attempts, setAttempts ] = useState(0);
    const [randomNumber, setRandomNumber ] = useState(Math.floor(Math.random() * (100 + 1)));

    function handleChange(event) {
        setNumber(event.target.value);
    }
    function Randomm(guess) {
        setAttempts(attempts+1);
          
        if (guess==randomNumber) {
            setResult(" Correct.Please Click Reset...");
                
        } else if (guess > randomNumber) {
        setResult("Hint: It's Lower Than This");
                
        } else if (guess < randomNumber) {
            setResult("Hint: It's Higher Than This");
        }
        
    }
    function Reset() {
        setRandomNumber(Math.floor(Math.random() * (100 + 1)));
        setNumber("");
        setAttempts(0);
        setResult("");
    }
    return(
        <div>
            <h2>You have attempted {attempts} times</h2>
            <input type="number" value={number} onChange={handleChange}/>
            <br/><br/><div className='hide'>
            <button onClick={() => Randomm(number)}>Submit</button>%n <button onClick={Reset}>Reset</button></div>
            <br></br><br/>
            {result}
        </div>
    );
}

export default Numberbox;