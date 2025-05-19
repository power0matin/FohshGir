from app import bot

def test_bot_and_dispatcher_exist():
    assert hasattr(bot, "bot")
    assert hasattr(bot, "dp")

def test_bot_token_format():
    assert bot.bot.token is not None
    assert isinstance(bot.bot.token, str)
