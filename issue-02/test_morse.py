from morse import decode
import pytest


@pytest.mark.parametrize(
    'source_string, decoded_string',
    [
        ('... --- ...', 'SOS'),
        ('..--- --- ..--- -....   .. ...   -.-. .-. .. -- .', '2O26ISCRIME'),
        ('.- .-. . -.-- --- ..- ... .- -.. ..--..', 'AREYOUSAD?'),
        ('...-- ...-- ..... -.- --- .--. --- -... -.--.-', '335KOPOB)'),
        ('-.--. -....- -....- -.--.- -....- -.--. -.--.- -....-', '(--)-()-')
    ]
)
def test_decode_morse(source_string: str, decoded_string: str):
    assert decode(source_string) == decoded_string
