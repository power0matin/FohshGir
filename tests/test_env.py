from app import env

def test_env_loads():
    config = env.get_env()
    assert isinstance(config, dict)
    assert "TOKEN" in config or "API_KEY" in config  # اگر کلید متفاوتی داری، جایگزین کن
