import { useEffect, useState } from 'react';
import axios from 'axios';
import CoachCard from '../components/CoachCard';

export default function Coachs() {
  const [coachs, setCoachs] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/joueur/coachs')
      .then(res => setCoachs(res.data));
  }, []);

  return (
    <div className="max-w-4xl mx-auto mt-10">
      <h2 className="text-2xl font-bold mb-4">Liste des Coachs</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {coachs.map(coach => <CoachCard key={coach.id} coach={coach} />)}
      </div>
    </div>
  );
}
