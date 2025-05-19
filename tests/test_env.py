import os
import pytest
from app import env

@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv("TOKEN", "123456")
    monkeypatch.setenv("DEBUG", "true")

def test_get_env_returns_dict(mock_env):
    config = env.get_env()
    assert isinstance(config, dict)
    assert config["TOKEN"] == "123456"
    assert config["DEBUG"] == "true"

def test_missing_env(monkeypatch):
    monkeypatch.delenv("TOKEN", raising=False)
    config = env.get_env()
    assert "TOKEN" not in config
