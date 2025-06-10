import { useState } from "react";

function Counter(){
    const [username,setUsername] = useState("John");
    return(
        <div>
            <h2>Hello {username}</h2>
        </div>
    );
}
export default Counter;