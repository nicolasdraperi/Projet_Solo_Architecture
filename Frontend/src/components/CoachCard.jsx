import { Link } from 'react-router-dom';

export default function CoachCard({ coach }) {
  return (
    <div className="border p-4 rounded shadow bg-white">
      <h3 className="text-xl font-semibold">{coach.nom}</h3>
      <p className="text-gray-600">Spécialité : {coach.specialite}</p>
      <p className="text-gray-600">Email : {coach.email}</p>
      <Link to={`/coach/${coach.id}`} className="text-blue-500 mt-2 inline-block">Voir les créneaux</Link>
    </div>
  );
}
