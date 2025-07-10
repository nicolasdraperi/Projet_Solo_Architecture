import pytest
from unittest.mock import MagicMock
import bcrypt
from datetime import datetime, timezone
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services import coach_service
from models import session as models_session
from models import coach as models_coach

def test_authenticate_coach_ok():
    db = MagicMock()
    hashed = bcrypt.hashpw("mdp123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    fake_coach = models_coach.Coach(id=1, nom="Jean", email="jean@example.com", password=hashed)
    db.query().filter().first.return_value = fake_coach

    result = coach_service.authenticate_coach(db, "jean@example.com", "mdp123")

    assert result is not None
    assert result.email == "jean@example.com"

def test_authenticate_coach_bad_password():
    db = MagicMock()
    hashed = bcrypt.hashpw("autre".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    fake_coach = models_coach.Coach(id=1, nom="Jean", email="jean@example.com", password=hashed)
    db.query().filter().first.return_value = fake_coach

    result = coach_service.authenticate_coach(db, "jean@example.com", "mdp123")

    assert result is None

def test_create_coach():
    db = MagicMock()
    coach_data = MagicMock()
    coach_data.nom = "Jean"
    coach_data.email = "jean@example.com"
    coach_data.password = "mdp123"
    coach_data.specialite = "Stratégie"

    db.add.return_value = None
    db.commit.return_value = None
    db.refresh.side_effect = lambda x: setattr(x, 'id', 1)

    result = coach_service.create_coach(db, coach_data)

    assert result.id == 1
    assert result.nom == coach_data.nom
    assert bcrypt.checkpw(coach_data.password.encode('utf-8'), result.password.encode('utf-8'))

def test_create_creneau():
    db = MagicMock()
    creneau_data = MagicMock()
    creneau_data.date_heure = datetime(2025, 7, 12, 15, 0, tzinfo=timezone.utc)
    creneau_data.duree_minutes = 60
    creneau_data.prix = 50.0

    db.add.return_value = None
    db.commit.return_value = None
    db.refresh.side_effect = lambda x: setattr(x, 'id', 1)

    result = coach_service.create_creneau(db, coach_id=1, creneau=creneau_data)

    assert result.coach_id == 1
    assert result.date_heure == creneau_data.date_heure
    assert result.statut == "disponible"

def test_update_creneau_success():
    db = MagicMock()
    creneau = MagicMock()
    db.query().filter().first.return_value = creneau

    update_data = MagicMock()
    update_data.date_heure = datetime(2025, 7, 13, 16, 0, tzinfo=timezone.utc)
    update_data.duree_minutes = 90
    update_data.prix = 60.0

    result = coach_service.update_creneau(db, coach_id=1, creneau_id=1, creneau_update=update_data)

    assert creneau.date_heure == update_data.date_heure
    assert creneau.duree_minutes == update_data.duree_minutes
    assert creneau.prix == update_data.prix


def test_update_creneau_not_found():
    db = MagicMock()
    db.query().filter().first.return_value = None

    update_data = MagicMock()

    with pytest.raises(Exception) as e:
        coach_service.update_creneau(db, coach_id=1, creneau_id=1, creneau_update=update_data)

    assert "Créneau non trouvé" in str(e.value)

def test_delete_creneau_success():
    db = MagicMock()
    creneau = MagicMock()
    db.query().filter().first.return_value = creneau

    result = coach_service.delete_creneau(db, coach_id=1, creneau_id=1)

    db.delete.assert_called_once_with(creneau)
    db.commit.assert_called_once()
    assert result == {"detail": "Créneau supprimé"}


def test_delete_creneau_not_found():
    db = MagicMock()
    db.query().filter().first.return_value = None

    with pytest.raises(Exception):
        coach_service.delete_creneau(db, coach_id=1, creneau_id=1)

def test_changer_statut_reservation_success():
    db = MagicMock()
    session = MagicMock()
    session.joueur_id = 2
    db.query().filter().first.return_value = session

    result = coach_service.changer_statut_reservation(db, coach_id=1, session_id=1, nouveau_statut="confirmée")

    assert session.statut == "confirmée"
    db.commit.assert_called_once()


def test_changer_statut_reservation_invalid_status():
    db = MagicMock()

    with pytest.raises(Exception) as e:
        coach_service.changer_statut_reservation(db, coach_id=1, session_id=1, nouveau_statut="invalid")

    assert "Statut invalide" in str(e.value)

def test_get_planning():
    db = MagicMock()
    sessions = [MagicMock(), MagicMock()]
    db.query().filter().all.return_value = sessions

    result = coach_service.get_planning(db, coach_id=1)

    assert result == sessions
