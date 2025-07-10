import { Link } from 'react-router-dom';

export default function SessionCard({ session }) {
  return (
    <div className="border p-4 rounded shadow bg-white flex flex-col">
      <h3 className="text-lg font-bold mb-2">Session #{session.id}</h3>
      <p className="mb-1">📅 Date : {new Date(session.date_heure).toLocaleString()}</p>
      <p className="mb-1">⏱️ Durée : {session.duree_minutes} min</p>
      <p className="mb-3">💰 Prix : {session.prix} €</p>
      
      <Link
        to={`/reservation/${session.id}`}
        className="bg-green-500 hover:bg-green-600 text-white py-2 px-4 rounded text-center"
      >
        Réserver
      </Link>
    </div>
  );
}
