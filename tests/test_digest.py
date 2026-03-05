# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import pytest

from digestible import digest

CASES = [
    (None, "fvakllLWEjyo5TJ5Vm8RPA=="),
    (True, "5DwJoS3S3e463uya639ERQ=="),
    (False, "jvKimP7exHmPJTQKYeDkzQ=="),
    (0, "HKHFFK9G1Rsgl2SYaNDBQg=="),
    (42, "97xJ31IQthW2Y-IB3-VvYw=="),
    (3.14, "245yMF1Nk6pygHN4dJJFiQ=="),
    ("", "skm2cZ8ndcZDf3t-8kBUdw=="),
    ("hello", "-z30OhN5TYcm6HuZu-gxoQ=="),
    ([], "cS4tc63OQjWs0nTlAVv5Ug=="),
    ([1, 2, 3], "7hUP-kq_pJB0r4R60YUeqA=="),
    ({}, "nKVsf7y9mMmkvgdU4R8-Kg=="),
    ({"a": {"b": 1}}, "TBE71TpLAtEtmOVy3U17uA=="),
    ({"x": [1, {"y": 2}]}, "dlZ1Y3ep3XksfPOKCizN2Q=="),
    ([{"a": 1}, {"b": [2, 3]}], "qHBOdNQT-XUGyqd6CsoYOA=="),
]


@pytest.mark.parametrize("value, expected", CASES)
def test_digest(value, expected):
    assert digest(value) == expected
    assert len(digest(value)) == 24
