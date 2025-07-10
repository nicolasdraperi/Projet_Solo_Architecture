import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import SessionCard from '../components/SessionCard';

export default function CoachDetail() {
  const { id } = useParams();
  const [creneaux, setCreneaux] = useState([]);

  useEffect(() => {
    axios.get(`http://localhost:8000/joueur/coach/${id}/creneaux`)
      .then(res => setCreneaux(res.data));
  }, [id]);

  return (
    <div className="max-w-4xl mx-auto mt-10">
      <h2 className="text-2xl font-bold mb-4">Créneaux disponibles</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {creneaux.map(session => <SessionCard key={session.id} session={session} />)}
      </div>
    </div>
  );
}
