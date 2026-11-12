from shopcart.cli import main


def test_cart_accepts_lowercase_code_with_spaces(capsys):
    assert main(["cart", "--add", "BLU-001", "--code", "  lato10  "]) == 0
    assert "Do zapłaty: 176,01 zł" in capsys.readouterr().out


def test_cart_unknown_code_prints_readable_error(capsys):
    assert main(["cart", "--add", "KUB-001", "--code", "XYZ"]) == 1
    assert capsys.readouterr().err.strip() == "Błąd: Nieznany kod rabatowy: XYZ"
