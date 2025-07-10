import { BrowserRouter, Routes, Route, Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';

import Register from './pages/Register';
import Login from './pages/Login';
import CoachLogin from './pages/CoachLogin';
import Profile from './pages/Profile';
import Coachs from './pages/Coachs';
import CoachDetail from './pages/CoachDetail';
import Reservation from './pages/Reservation';
import Paiement from './pages/Paiement';
import CoachPanel from './pages/CoachPanel';



function AppWrapper() {
  return (
    <BrowserRouter>
      <App />
    </BrowserRouter>
  );
}

export default AppWrapper;

function App() {
  const navigate = useNavigate();
  const [joueurToken, setJoueurToken] = useState(localStorage.getItem('joueurToken') || '');
  const [coachToken, setCoachToken] = useState(localStorage.getItem('coachToken') || '');

  const isJoueurConnected = Boolean(joueurToken);
  const isCoachConnected = Boolean(coachToken);

  const handleJoueurLogin = (token) => {
    setJoueurToken(token);
    localStorage.setItem('joueurToken', token);
  };

  const handleCoachLogin = (token) => {
    setCoachToken(token);
    localStorage.setItem('coachToken', token);
  };

  const handleLogout = () => {
    setJoueurToken('');
    setCoachToken('');
    localStorage.removeItem('joueurToken');
    localStorage.removeItem('coachToken');
    navigate('/login');
  };

  return (
    <>
      <nav className="bg-gray-800 p-4 text-white flex flex-wrap items-center space-x-4">
        {!isJoueurConnected && !isCoachConnected && (
          <>
            <Link to="/register" className="hover:underline">Inscription</Link>
            <Link to="/login" className="hover:underline">Connexion</Link>
          </>
        )}

        <Link to="/coachs" className="hover:underline">Coachs</Link>

        {isJoueurConnected && (
          <>
            <Link to="/profile" className="hover:underline">Profil</Link>
            <button
              onClick={handleLogout}
              className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded"
            >
              Déconnexion
            </button>
          </>
        )}

{isCoachConnected && (
  <>
    <Link to="/coach/panel" className="hover:underline">Panneau</Link>
    <button
      onClick={handleLogout}
      className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded"
    >
      Déconnexion
    </button>
  </>
)}

      </nav>

      <div className="p-4">
        <Routes>
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login setToken={handleJoueurLogin} />} />
          <Route path="/coach-login" element={<CoachLogin setCoachToken={handleCoachLogin} />} />
          <Route path="/profile" element={<Profile token={joueurToken} />} />
          <Route path="/coachs" element={<Coachs />} />
          <Route path="/coach/:id" element={<CoachDetail />} />
          <Route path="/reservation/:sessionId" element={<Reservation token={joueurToken} />} />
          <Route path="/paiement/:sessionId" element={<Paiement token={joueurToken} />} />
          <Route path="/coach/panel" element={<CoachPanel token={coachToken} />} />
        </Routes>
      </div>
    </>
  );
}
