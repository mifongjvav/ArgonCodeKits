from ArgonCodeKits import md5, sha1, sha256, sha512


def test_md5():
    assert md5("argon") == "df119d4f6efe038ae92539fab8521779"


def test_sha1_length():
    assert len(sha1("argon")) == 40


def test_sha256_length():
    assert len(sha256("argon")) == 64


def test_sha512_length():
    assert len(sha512("argon")) == 128
