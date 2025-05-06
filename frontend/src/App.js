// src/App.jsx
import React from 'react';
import UploadDocument from './components/UploadDocument';
import SearchDocument from './components/SearchDocument';

function App() {
  return (
    <div className="App">
      <h1>Document Search Bot</h1>
      <UploadDocument />
      <SearchDocument />
    </div>
  );
}

export default App;
