import Contactt from './Contactt.jpg';

function Contact(){
    return(
        <div className="div1">
            <img src={Contactt} width="200px" height="140px" alt="logo"/>
            <h1>Contact</h1>
            <hr></hr>
            <p>This is my Contact<br></br>
            Email: amalanagha2006@gmail.com<br></br>
            <br></br>Return to <a href="http://localhost:3000">Home</a></p>
            
        </div>
    );
}

export default Contact;