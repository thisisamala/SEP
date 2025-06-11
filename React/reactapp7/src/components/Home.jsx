import Oggy from './Oggy.jpg';
import './Home.css';
function Home(){
    return(
        <div >
            <div className='div1'>
                <img src={Oggy} width="200px" height="100px" alt="logo"/>
                <h1>Home</h1>
                <hr></hr>
                <p>This is my home page</p>
                <br></br><br></br>
            </div>
        </div>
    );

}

export default Home;