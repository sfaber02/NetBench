import React from "react";
import { useEffect, useRef } from "react";
import FormContainer from "./components/FormContainer";



import "./App.css";

const App: React.FC = () => {


  return (
    <div>
      <script type="text/javascript" src="smoothie.js"></script>
      <FormContainer />
      <div>
        <canvas id="mycanvas" width="400" height="100"></canvas>
        
        <script type="text/javascript">
          // Random data
          var line1 = new TimeSeries();
          var line2 = new TimeSeries();
          setInterval(function() {
            line1.append(Date.now(), Math.random()),
            line2.append(Date.now(), Math.random())
          }, 1000);

          var smoothie = new SmoothieChart({ grid: { strokeStyle: 'rgb(125, 0, 0)', fillStyle: 'rgb(60, 0, 0)', lineWidth: 1, millisPerLine: 250, verticalSections: 6 } });
          smoothie.addTimeSeries(line1, { strokeStyle: 'rgb(0, 255, 0)', fillStyle: 'rgba(0, 255, 0, 0.4)', lineWidth: 3 });
          smoothie.addTimeSeries(line2, { strokeStyle: 'rgb(255, 0, 255)', fillStyle: 'rgba(255, 0, 255, 0.3)', lineWidth: 3 });

          smoothie.streamTo(document.getElementById("mycanvas"), 1000);
        </script>
      </div>
    </div>
  );
};

export default App;
