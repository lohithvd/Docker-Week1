import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Full URL with port
    fetch('http://localhost:5000/api/data')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => setData(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>Data from Flask API:</h1>
      <ul>
        {data.map((item, index) => (
          <li key={index}>{item[1]}</li>  
        ))}
      </ul>
    </div>
  );
}

export default App;
