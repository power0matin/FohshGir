from app import texts

def test_text_constants_are_strings():
    assert isinstance(texts.WELCOME_MESSAGE, str)
    assert isinstance(texts.ERROR_MESSAGE, str)

def test_texts_not_empty():
    for text in [texts.WELCOME_MESSAGE, texts.ERROR_MESSAGE]:
        assert text.strip() != ""
