import React from 'react';
import Fade from 'react-reveal/Fade';
import '../App.css'
class Features extends React.Component {
  render() {
    return (
        <div id='features'>
                    <Fade bottom cascade>
                       <div id="one"><img src={require('./one.png')} />
                       <h3>SENTIMENT ANALYSIS</h3>
                       <p id='features'>A streamlit based python application running SENTIMENT ANALYSIS on the latest news scraped from a trusted news page FINVIZ</p>
                       <button id='start'><a href='http://parapluie.herokuapp.com' target="_blank">GET STARTED</a></button>
</div>
                       <div id="two"><img src={require('./two.png')} />
                       
                       <h3>TECHNICAL ANALYSIS</h3>
                       <p id='features'>Golden Cross and Death Cross is a famous strategy used for basic technical analysis by investors. By using st.pyplot() , a chart has been provided in the application which tells when to buy/sell based on close-to-real-time data</p>
                       <button id='start'><a href='http://parapluie.herokuapp.com' target="_blank">GET STARTED</a></button>

                       
                       </div>
        </Fade>
      </div>
    );
  }
}

export default Features;
 