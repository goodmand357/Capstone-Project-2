import React, { useState } from 'react';
import axios from 'axios';

const StockSearch = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState(null);

  const search = async () => {
    const res = await axios.get(`http://127.0.0.1:5000/search?q=${query}`);
    setResults(res.data);
  };

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)} />
      <button onClick={search}>Search</button>
      <pre>{JSON.stringify(results, null, 2)}</pre>
    </div>
  );
};

export default StockSearch;
