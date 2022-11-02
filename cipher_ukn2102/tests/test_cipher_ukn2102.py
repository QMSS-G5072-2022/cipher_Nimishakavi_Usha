from cipher_ukn2102 import cipher_ukn2102


def test_cipher():
    expected = 'Hs vZr Z aZc cZx'
    result = cipher_ukn2102.cipher('It was a bad day',1,encrypt=False)
    assert expected == result