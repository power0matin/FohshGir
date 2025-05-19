from app import texts

def test_texts_have_content():
    assert hasattr(texts, "WELCOME_MESSAGE")
    assert isinstance(texts.WELCOME_MESSAGE, str)
    assert texts.WELCOME_MESSAGE.strip() != ""
