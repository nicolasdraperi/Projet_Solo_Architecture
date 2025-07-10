import { useEffect, useState } from 'react';
import axios from 'axios';

export default function CoachPanel({ token }) {
  const [creneaux, setCreneaux] = useState([]);
  const [planning, setPlanning] = useState([]);
  const [newCreneau, setNewCreneau] = useState({ date_heure: '', duree_minutes: 60, prix: 0 });

  // Appel initial
  useEffect(() => {
    fetchCreneaux();
    fetchPlanning();
  }, []);

  const authHeader = { headers: { Authorization: `Bearer ${token}` } };

  const fetchCreneaux = () => {
    axios.get('http://localhost:8000/coach/planning', authHeader)
      .then(res => setCreneaux(res.data));
  };

  const fetchPlanning = () => {
    axios.get('http://localhost:8000/coach/planning', authHeader)
      .then(res => setPlanning(res.data));
  };

  const handleAddCreneau = () => {
    axios.post('http://localhost:8000/coach/creneaux', newCreneau, authHeader)
      .then(() => {
        setNewCreneau({ date_heure: '', duree_minutes: 60, prix: 0 });
        fetchCreneaux();
      });
  };

  const handleDeleteCreneau = (id) => {
    axios.delete(`http://localhost:8000/coach/creneaux/${id}`, authHeader)
      .then(fetchCreneaux);
  };

  const handleChangeStatus = (sessionId, status) => {
    axios.put(`http://localhost:8000/coach/reservation/${sessionId}/statut?nouveau_statut=${status}`, {}, authHeader)
      .then(fetchPlanning);
  };

  return (
    <div className="max-w-4xl mx-auto mt-10 space-y-8">
      <h1 className="text-3xl font-bold mb-6">Panneau de gestion du coach</h1>

      {/* Section 1: Créer un créneau */}
      <section className="p-4 bg-white rounded shadow">
        <h2 className="text-xl font-bold mb-3">Ajouter un créneau</h2>
        <div className="flex flex-col space-y-2">
          <input
            type="datetime-local"
            value={newCreneau.date_heure}
            onChange={e => setNewCreneau({ ...newCreneau, date_heure: e.target.value })}
            className="border p-2 rounded"
          />
          <input
            type="number"
            value={newCreneau.duree_minutes}
            onChange={e => setNewCreneau({ ...newCreneau, duree_minutes: parseInt(e.target.value) })}
            className="border p-2 rounded"
            placeholder="Durée (minutes)"
          />
          <input
            type="number"
            value={newCreneau.prix}
            onChange={e => setNewCreneau({ ...newCreneau, prix: parseFloat(e.target.value) })}
            className="border p-2 rounded"
            placeholder="Prix"
          />
          <button onClick={handleAddCreneau} className="bg-green-500 text-white px-4 py-2 rounded">Ajouter</button>
        </div>
      </section>

      {/* Section 2: Liste des créneaux */}
      <section className="p-4 bg-white rounded shadow">
        <h2 className="text-xl font-bold mb-3">Mes créneaux</h2>
        <ul className="space-y-2">
          {creneaux.map(c => (
            <li key={c.id} className="flex justify-between items-center border p-2 rounded">
              <span>{c.date_heure} | {c.duree_minutes} min | {c.prix} €</span>
              <button onClick={() => handleDeleteCreneau(c.id)} className="bg-red-500 text-white px-3 py-1 rounded">Supprimer</button>
            </li>
          ))}
        </ul>
      </section>

      {/* Section 3: Planning des réservations */}
      <section className="p-4 bg-white rounded shadow">
        <h2 className="text-xl font-bold mb-3">Planning des réservations</h2>
        <ul className="space-y-2">
          {planning.filter(p => p.joueur_id).map(p => (
            <li key={p.id} className="flex justify-between items-center border p-2 rounded">
              <span>
                {p.date_heure} | Joueur ID: {p.joueur_id} | Statut: {p.statut}
              </span>
              <div className="space-x-2">
                <button onClick={() => handleChangeStatus(p.id, "confirmée")} className="bg-green-500 text-white px-3 py-1 rounded">Confirmer</button>
                <button onClick={() => handleChangeStatus(p.id, "refusée")} className="bg-yellow-500 text-white px-3 py-1 rounded">Refuser</button>
              </div>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
