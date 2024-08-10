import { SmoothieChart, TimeSeries } from "smoothie";

const Chart = () => {
  // Data
  var line1 = new TimeSeries();
  var line2 = new TimeSeries();

  // Add a random value to each line every second
  setInterval(function () {
    line1.append(Date.now(), Math.random());
    line2.append(Date.now(), Math.random());
  }, 1000);

  // Add to SmoothieChart

  return (
    <div>
      <script>
        var smoothie = new SmoothieChart(); smoothie.addTimeSeries(line1);
        smoothie.addTimeSeries(line2);
        smoothie.streamTo(document.getElementById("mycanvas"));
      </script>
      <canvas id="mycanvas" width="400" height="100"></canvas>
    </div>
  );
};

export default Chart;
