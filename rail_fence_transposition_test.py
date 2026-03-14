import rail_fence_transposition

def test_get_transposed_string():
    assert rail_fence_transposition.get_transposed_string("abc") == "acb"
    assert rail_fence_transposition.get_transposed_string("wxyz") == "wyxz"
    assert rail_fence_transposition.get_transposed_string("ihopethisworks πD@¥") == "ioehsok D¥hptiwrsπ@"

def test_get_original_string():
    assert rail_fence_transposition.get_original_string("prqs") == "pqrs"
    assert rail_fence_transposition.get_original_string("wyxz") == "wxyz"
    assert rail_fence_transposition.get_original_string("ioehsok D¥hptiwrsπ@") == "ihopethisworks πD@¥"