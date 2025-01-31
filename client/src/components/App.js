import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Import BrowserRouter
import Sellers from "./Sellers";
import EditForm from "./EditForm";
import AuthenticationPage from "./AuthenticationPage";

function App() {

  return (
    <Router>
      <main>

        <h1>Wellcome to Online Marktet</h1>
        <Routes>
          <Route path="/sellers" element={<Sellers />} />

          <Route path="/sellers/:username/:product_id" element={<EditForm />} />

          <Route path="/sellers/:username/authentication/:product_id" element={<AuthenticationPage />} />
        </Routes>
      </main>
    </Router>
  )

}

export default App;
