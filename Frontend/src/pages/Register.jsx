import { useState } from 'react';
import axios from 'axios';

export default function Register() {
  const [form, setForm] = useState({ nom: '', email: '', password: '' });
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/joueur/inscription', form);
      setMessage('Inscription réussie !');
    } catch {
      setMessage('Erreur lors de l\'inscription.');
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded shadow">
      <h2 className="text-xl font-bold mb-4">Inscription</h2>
      <form className="flex flex-col space-y-3" onSubmit={handleSubmit}>
        <input className="border p-2" placeholder="Nom" onChange={e => setForm({ ...form, nom: e.target.value })} />
        <input className="border p-2" placeholder="Email" type="email" onChange={e => setForm({ ...form, email: e.target.value })} />
        <input className="border p-2" placeholder="Mot de passe" type="password" onChange={e => setForm({ ...form, password: e.target.value })} />
        <button className="bg-blue-500 text-white p-2 rounded">S'inscrire</button>
      </form>
      {message && <p className="mt-3">{message}</p>}
    </div>
  );
}
