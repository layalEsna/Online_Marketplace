import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Import BrowserRouter
import Sellers from "./Sellers";
import EditForm from "./EditForm";

function App() {

  return (
    <Router>
      <main>

        <h1>Wellcome to Online Market</h1>
        <Routes>
          <Route path="/sellers" element={<Sellers />} />
          {/* <Route path="/sellers/:username/:productId" element={<EditForm/>} /> */}
          <Route path="/sellers/:username" element={<EditForm/>} />
        </Routes>
      </main>
    </Router>
  )

}

export default App;
