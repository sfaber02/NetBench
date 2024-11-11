import React, { useEffect, useRef } from "react";
import { TimeSeries, SmoothieChart } from "smoothie";
import "./App.css";

const App: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    if (canvasRef.current) {
      const line1 = new TimeSeries();
      const line2 = new TimeSeries();

      const updateData = () => {
        line1.append(Date.now(), Math.random());
        line2.append(Date.now(), Math.random());
      };

      const dataInterval = setInterval(updateData, 10);

      const smoothie = new SmoothieChart({
        grid: {
          strokeStyle: 'rgb(125, 0, 0)',
          fillStyle: 'rgb(60, 0, 0)',
          lineWidth: 10,
          millisPerLine: 25,
          verticalSections: 2
        }
      });

      smoothie.addTimeSeries(line1, {
        strokeStyle: 'rgb(0, 255, 0)',
        fillStyle: 'rgba(0, 255, 0, 0.4)',
        lineWidth: 1
      });

      smoothie.addTimeSeries(line2, {
        strokeStyle: 'rgb(255, 0, 255)',
        fillStyle: 'rgba(255, 0, 255, 0.3)',
        lineWidth: 1
      });

      smoothie.streamTo(canvasRef.current, 1000);

      return () => {
        clearInterval(dataInterval);
        smoothie.stop();
      };
    }
  }, []);

  return (
    <div>
      <canvas ref={canvasRef} width="400" height="100" />
    </div>
  );
};

export default App;
