import { useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

export default function Reservation({ token }) {
  const { sessionId } = useParams();
  const [message, setMessage] = useState('');

  const reserver = async () => {
    try {
      await axios.post(`http://localhost:8000/joueur/session/${sessionId}/reserver`, {}, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setMessage('Réservation réussie !');
    } catch {
      setMessage('Erreur lors de la réservation');
    }
  };

  return (
    <div className="p-4 bg-white rounded shadow max-w-md mx-auto mt-6">
      <h2 className="text-xl font-bold mb-4">Réserver la session #{sessionId}</h2>
      <button onClick={reserver} className="bg-blue-500 hover:bg-blue-600 text-white p-2 rounded">
        Réserver cette session
      </button>
      {message && <p className="mt-3">{message}</p>}
    </div>
  );
}
