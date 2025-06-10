import OIP from './OIP.jpg';
function About(){
    return(
        <div className="div1">
            <img src={OIP} width="200px" height="100px" alt="logo"/>
            <h1>About</h1>
            <hr></hr>
            <p>This is my About<br></br><br></br>Return to <a href="http://localhost:3000">Home</a></p>
            
        </div>
    );
}

export default About;