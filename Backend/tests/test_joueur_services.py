# '''
import pytest
from unittest.mock import MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.models import joueur as models_joueur
from app.services import joueur_service

import bcrypt

# Exemple 1 : test de création de joueur
def test_create_joueur():
    db = MagicMock()
    joueur_data = MagicMock()
    joueur_data.nom = "Jean"
    joueur_data.email = "jean@example.com"
    joueur_data.password = "mdp123"

    result_mock = MagicMock()
    db.add.return_value = None
    db.commit.return_value = None
    db.refresh.side_effect = lambda x: setattr(x, 'id', 1)

    joueur = joueur_service.create_joueur(db, joueur_data)

    db.add.assert_called_once()
    db.commit.assert_called_once()
    assert joueur.id == 1
    assert joueur.nom == joueur_data.nom
    assert bcrypt.checkpw(joueur_data.password.encode('utf-8'), joueur.password.encode('utf-8'))


# Exemple 2 : test authentification joueur réussi
def test_authenticate_joueur_ok(mocker):
    db = MagicMock()
    hashed = bcrypt.hashpw("mdp123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    fake_user = models_joueur.Joueur(id=1, nom="Jean", email="jean@example.com", password=hashed)
    db.query().filter().first.return_value = fake_user

    user = joueur_service.authenticate_joueur(db, "jean@example.com", "mdp123")

    assert user is not None
    assert user.email == "jean@example.com"


# Exemple 3 : test authentification joueur mauvais mot de passe
def test_authenticate_joueur_bad_password(mocker):
    db = MagicMock()
    hashed = bcrypt.hashpw("autre".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    fake_user = models_joueur.Joueur(id=1, nom="Jean", email="jean@example.com", password=hashed)
    db.query().filter().first.return_value = fake_user

    user = joueur_service.authenticate_joueur(db, "jean@example.com", "mdp123")
    assert user is None


# Exemple 4 : test payer session
def test_payer_session():
    db = MagicMock()
    result = joueur_service.payer_session(db, session_id=1, montant=49.99)

    db.add.assert_called_once()
    db.commit.assert_called_once()
    assert result.session_id == 1
    assert result.montant == 49.99
    assert result.statut == "payé"

# '''