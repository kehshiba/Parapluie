import React from 'react';
import Fade from 'react-reveal/Fade';
import '../App.css'
class About extends React.Component {
  render() {
    return (
      <div>
        <Fade bottom >
          <div id='info'>
          <div id ="about"><span id='bold-italic'>PARAPLUIE</span> IS A NEW-AGE <span id='light-italic'>TRADING ANALYSIS</span> DASHBOARD
FOR TRADERS WHO DO EVERYTHING <span id='bold'>LASY.</span> THEY DON’T NEED
TO SPEND TIME LEARNING INDICATORS AND ANALYSING THEM.
WE GOT THEM <span id ="big"> COVERED.</span>

<p id='about-content'>WE USE MACHINE LEARNING MODELS WHICH ANALYSE YOUR STOCKS ON REAL-TIME USING
SOME OF THE MOST SUCCESSFUL TECHNICAL INDICATORS TO DATE.

 WITH A SENTIMENT ANALYSIS KIT, YOU GET TO KNOW THE EMOTION BEHIND THE MARKET,
ALL POWERED BY SOCIAL-MEDIA.
</p>
</div>
</div>
    
        </Fade>
      </div>
    );
  }
}

export default About;
 