import caesar_cipher

def test_get_encrypted_character():
    assert caesar_cipher.get_encrypted_character("a") == "c"
    assert caesar_cipher.get_encrypted_character("b") == "d"
    assert caesar_cipher.get_encrypted_character("π") == "π"
    assert caesar_cipher.get_encrypted_character("`") == "`"
    assert caesar_cipher.get_encrypted_character("{") == "{"
    assert caesar_cipher.get_encrypted_character("z") == "b"

def test_get_encrypted_string():  
    assert caesar_cipher.get_encrypted_string("cipher") == "ekrjgt"
    assert caesar_cipher.get_encrypted_string("caesar") == "ecguct"
    assert caesar_cipher.get_encrypted_string("zambia") == "bcodkc"
    assert caesar_cipher.get_encrypted_string("!iwant$π∑! .") == "!kycpv$π∑! ."

def test_get_decrypted_character():
    assert caesar_cipher.get_decrypted_character("c") == "a"
    assert caesar_cipher.get_decrypted_character("d") == "b"
    assert caesar_cipher.get_decrypted_character("π") == "π"
    assert caesar_cipher.get_decrypted_character("a") == "y"

def test_get_decrypted_string():
    assert caesar_cipher.get_decrypted_string("ekrjgt") == "cipher"
    assert caesar_cipher.get_decrypted_string("bcodkc") == "zambia"
    assert caesar_cipher.get_decrypted_string("!kycpv$π∑! .") == "!iwant$π∑! ."