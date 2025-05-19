from app import bot

def test_bot_exists():
    assert hasattr(bot, "dp") or hasattr(bot, "bot")  # با توجه به ساختارت می‌تونه متفاوت باشه
