from main import add


def test_add() -> None:
    # GWT

    # Given
    a = 3
    b = -1

    # When
    result = add(a, b)

    # Then
    assert result == 2
