import { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

export default function Login({ setToken }) {
  const [form, setForm] = useState({ email: '', password: '' });
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:8000/joueur/login', form);
      setToken(res.data.access_token);
      setMessage('Connecté !');
    } catch {
      setMessage('Email ou mot de passe incorrect.');
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded shadow">
      <h2 className="text-xl font-bold mb-4">Connexion Joueur</h2>
      <form className="flex flex-col space-y-3" onSubmit={handleSubmit}>
        <input
          className="border p-2"
          placeholder="Email"
          type="email"
          onChange={e => setForm({ ...form, email: e.target.value })}
        />
        <input
          className="border p-2"
          placeholder="Mot de passe"
          type="password"
          onChange={e => setForm({ ...form, password: e.target.value })}
        />
        <button className="bg-green-500 text-white p-2 rounded">Se connecter</button>
      </form>

      {message && <p className="mt-3 text-red-500">{message}</p>}

      <div className="mt-4 text-center">
        <Link to="/coach-login" className="text-blue-600 hover:underline">
          Vous êtes un coach ? Connectez-vous ici
        </Link>
      </div>
    </div>
  );
}
