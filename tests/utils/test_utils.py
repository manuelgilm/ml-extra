from ml_extra.utils.utils import get_root_path
from ml_extra.utils.utils import encode_file
from ml_extra.utils.utils import decode_filename

def test_get_root_path():
    root_path = get_root_path()
    assert root_path.is_dir()

def test_encode_file():
    name = "file.txt"
    encoded_name = encode_file(name)
    assert name != encoded_name

def test_decode_filename():
    name = "file.txt"
    encoded_name = encode_file(name)
    decoded_name, _ = decode_filename(encoded_name)
    assert name == decoded_name