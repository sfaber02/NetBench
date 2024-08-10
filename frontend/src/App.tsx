import React from "react";
import { useEffect, useRef } from "react";
import FormContainer from "./components/FormContainer";
import Chart from "./components/SmoothieChart";


import "./App.css";

const App: React.FC = () => {


  return (
    <div>
      <FormContainer />
      <Chart/>
    </div>
  );
};

export default App;
