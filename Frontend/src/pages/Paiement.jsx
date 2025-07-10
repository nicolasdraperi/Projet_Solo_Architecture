import { useState } from 'react';
import axios from 'axios';

export default function Paiement({ token, sessionId }) {
  const [montant, setMontant] = useState('');
  const [message, setMessage] = useState('');

  const payer = async () => {
    try {
      await axios.post(`http://localhost:8000/joueur/session/${sessionId}/payer`, {
        session_id: sessionId,
        montant: parseFloat(montant)
      }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setMessage('Paiement effectué !');
    } catch {
      setMessage('Erreur lors du paiement');
    }
  };

  return (
    <div className="p-4 bg-white rounded shadow max-w-md mx-auto mt-6">
      <input className="border p-2 mb-2 w-full" placeholder="Montant" type="number" value={montant} onChange={e => setMontant(e.target.value)} />
      <button onClick={payer} className="bg-green-500 text-white p-2 rounded w-full">Payer</button>
      {message && <p className="mt-3">{message}</p>}
    </div>
  );
}
