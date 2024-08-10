import React, {useState} from 'react';
import logo from './logo.svg';
import FormContainer from './components/InputForm';


import './App.css';
import {TestGrpcClientComponent} from "./components/TestGrpcClient";

const App: React.FC = () => {
  return (
      <div>
          {/*<FormContainer/>*/}
          <TestGrpcClientComponent/>
      </div>
  )
}

export default App;

