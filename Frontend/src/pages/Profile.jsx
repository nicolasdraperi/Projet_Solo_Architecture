import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Profile({ token }) {
  const [profile, setProfile] = useState(null);
  const [reservations, setReservations] = useState([]);

  useEffect(() => {
    // Charger le profil
    axios.get('http://localhost:8000/joueur/profile', {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(res => setProfile(res.data));

    // Charger ses réservations
    axios.get('http://localhost:8000/joueur/mes-reservations', {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(res => setReservations(res.data));
  }, [token]);

  if (!profile) return <p className="text-center mt-10">Chargement...</p>;

  return (
    <div className="max-w-2xl mx-auto mt-10 p-6 bg-white rounded shadow">
      <h2 className="text-2xl font-bold mb-4">👤 Profil</h2>
      <p className="mb-2"><strong>Nom:</strong> {profile.nom}</p>
      <p className="mb-4"><strong>Email:</strong> {profile.email}</p>

      <h3 className="text-xl font-semibold mt-6 mb-2">📅 Mes réservations</h3>
      {reservations.length === 0 ? (
        <p className="text-gray-500">Vous n'avez encore aucune réservation.</p>
      ) : (
        <ul className="space-y-4">
          {reservations.map((session) => (
            <li key={session.id} className="border p-4 rounded bg-gray-50">
              <p><strong>Session ID:</strong> {session.id}</p>
              <p><strong>Date:</strong> {new Date(session.date_heure).toLocaleString()}</p>
              <p><strong>Durée:</strong> {session.duree_minutes} min</p>
              <p><strong>Prix:</strong> {session.prix} €</p>
              <p><strong>Statut:</strong> {session.statut}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
