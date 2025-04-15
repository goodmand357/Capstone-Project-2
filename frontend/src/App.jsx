import React from 'react';
import StockSearch from './components/StockSearch';
import StockPredictor from './components/StockPredictor';

const App = () => {
  return (
    <div>
      <h1>📈 Stock Screener</h1>
      <StockSearch />
      <StockPredictor />
    </div>
  );
};

export default App;
