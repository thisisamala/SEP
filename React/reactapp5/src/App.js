import { useState } from 'react';
import './App.css';
import InputDisplay from './components/InputDisplay';
import Greeting from './components/Greeting';
import ThemeSwitcher from './components/ThemeSwitcher';
function App() {
  
    const [user,setUser] = useState("Sara") ;
    return (
    <div className="App">
      <Greeting name = "John"/>
      <Greeting name={user}/>
      <InputDisplay/>
      <ThemeSwitcher/>
    </div>
  );
}

export default App;
