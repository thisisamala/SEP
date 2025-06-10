import "./Count.css";
import { useState } from "react";

function Count(){
    const [usercount,setCount] = useState(0);
    function increment(){
        setCount(usercount+1);
    }
    function decrement(){
        setCount(usercount-1);
    }
    return(
        <div className="div1">
            <h1> you clicked {usercount} times</h1>
            <button onClick={increment}>Click</button><br></br><br></br>
            <button onClick={decrement}>Not Me</button><br></br><br></br>
        </div>
    );
}
export default Count;