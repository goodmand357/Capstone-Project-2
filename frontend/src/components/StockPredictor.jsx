import React, { useState } from 'react';
import axios from 'axios';

const StockPredictor = () => {
  const [features, setFeatures] = useState({
    price_momentum: 0,
    rsi: 50,
    macd: 0,
    volume_change: 0
  });
  const [prediction, setPrediction] = useState(null);

  const predict = async () => {
    const res = await axios.post('http://127.0.0.1:5000/predict', features);
    setPrediction(res.data);
  };

  return (
    <div>
      <h2> Stock Prediction</h2>
      {Object.keys(features).map(key => (
        <div key={key}>
          <label>{key}</label>
          <input
            type="number"
            value={features[key]}
            onChange={e =>
              setFeatures({ ...features, [key]: parseFloat(e.target.value) })
            }
          />
        </div>
      ))}
      <button onClick={predict}>Predict</button>
      {prediction && <pre>{JSON.stringify(prediction, null, 2)}</pre>}
    </div>
  );
};

export default StockPredictor;
