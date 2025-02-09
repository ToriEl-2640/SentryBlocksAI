
import { useState, useEffect } from 'react';
import axios from 'axios';

export default function Home() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Simplified version without backend calls
    setData({ message: "Welcome to SentryBlocksAI!" });
      .catch(err => {
        console.error('Axios error:', err);
        setError(err.message);
      });
  }, []);

  if (error) return <div>Error: {error}</div>;
  
  return (
    <div>
      <h1>Welcome to SentryBlocksAI</h1>
      {data && <div>{JSON.stringify(data)}</div>}
    </div>
  );
}
