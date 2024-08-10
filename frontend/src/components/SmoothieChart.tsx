import { SmoothieChart, TimeSeries } from "smoothie";

const Chart = () => {
  // Data
  let line1 = new TimeSeries();
  let line2 = new TimeSeries();

  // Add a random value to each line every second
  setInterval(function () {
    line1.append(Date.now(), Math.random());
    line2.append(Date.now(), Math.random());
  }, 1000);

  let smoothie = new SmoothieChart(); 
  smoothie.addTimeSeries(line1);
  smoothie.addTimeSeries(line2);

  smoothie.streamTo(document.getElementById("mycanvas"));

  return (    
    <div>
      <canvas id="mycanvas" width="400" height="100"></canvas>
    </div>
  );
};

export default Chart;
