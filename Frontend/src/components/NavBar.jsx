import { Link, useNavigate } from 'react-router-dom';

export default function NavBar({ userToken, coachToken, setUserToken, setCoachToken }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    setUserToken('');
    setCoachToken('');
    localStorage.removeItem('userToken');
    localStorage.removeItem('coachToken');
    navigate('/login');
  };

  return (
    <nav className="bg-gray-800 p-4 text-white flex flex-wrap items-center space-x-4">
      {(!userToken && !coachToken) && (
        <>
          <Link to="/register" className="hover:underline">Inscription</Link>
          <Link to="/login" className="hover:underline">Connexion</Link>
          <Link to="/coachs" className="hover:underline">Coachs</Link>
        </>
      )}

      {userToken && (
        <>
          <Link to="/coachs" className="hover:underline">Coachs</Link>
          <Link to="/profile" className="hover:underline">Profil</Link>
          <button onClick={handleLogout} className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded">
            Déconnexion
          </button>
        </>
      )}

      {coachToken && (
        <>
          <Link to="/coachs" className="hover:underline">Coachs</Link>
          <Link to="/coachpanel" className="hover:underline">Panneau</Link>
          <button onClick={handleLogout} className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded">
            Déconnexion
          </button>
        </>
      )}
    </nav>
  );
}
