import './App.css';
import About from './components/About';
import Features from './components/Features';

function App() {
  return (
    <div className="App">
      <div id="center">
        <h1>PARA<span id='title'>PLUIE</span></h1>
        <p>FOR THE JESSE LIVERMOORE OF TODAY</p>
        <button id='start'><a href='http://parapluie.herokuapp.com' target="_blank">GET STARTED</a></button>
        <button id='scroll'><a href='#info'>↓</a></button>

    </div>

  <About />   
  <Features />
  <footer>By Abhishek A B | <a href="https://www.github.com/kehshiba">@kehshiba</a></footer>
    </div>
  );
}
  
export default App;
