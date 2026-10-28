from typing import Literal

MAX_LENGTH = 140
# Funkce kontroluje jenom krátké samohlásky, kdyby funkce měla zvládat i český text, rozšířil by se řetězec o "á", "ě", "í"...
VOWELS = "aeiou"

def edit_text(text: str) -> str | Literal[False]:
    """
    Edits the input text and removes numbers, or vowels if the text starts with "!".

    Parameters:
    text (str): The input text to edit.

    Returns:
    str: The edited text, or False if the text is longer than MAX_LENGTH.
    """
    result = ""

    # Podle zadání "Pokud text bude začínat vykřičníkem výstupem funkce bude text neobsahující žádné samohlásky" to beru tak, že v tomhle případě se čísla nemažou
    # Zadání neříká, že by se měl odstranit vykřičník, takže se jen kontroluje jestli je na začátku, pak se už nemaže
    if text.startswith("!"):
        for char in text:
            if char.lower() not in VOWELS:
                result += char
    else:
        for char in text:
            # Bere všechny číslice ("²"...) mohla by se použít funkce isdecimal() v případě, že by se měly odstranit jenom běžné číslice
            if not char.isdigit():
                result += char

    if len(result) > MAX_LENGTH:
        return False
    return result

def test_edit_text():
    assert edit_text("H1E2L3L4O5_6W7O8R9L0D") == "HELLO_WORLD"
    assert edit_text("!HELLO_world") == "!HLL_wrld"
    assert edit_text("a1" * 140) == "a" * 140
    assert edit_text("a1" * 141) is False
    assert edit_text("!" + "b" * 140) is False
    assert edit_text("!1") == "!1"
    assert edit_text("") == ""

if __name__ == "__main__":
    test_edit_text()