import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Sellers from "./Sellers";

function App() {

  return (
    <div>
      <h1>Wellcome to Online Market</h1>
      
      <Sellers />
    </div>
  )
}

export default App;
