# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import pytest

from digestible import digest

CASES = [
    (None, "KtLhiM3tliLbJ-hWaj3sMQ=="),
    (True, "9pqHQJRzn-fsbYwTTZkT9Q=="),
    (False, "z7kb3NcFWLXrrPXWZ5W0dg=="),
    (0, "Yo55z3lIzRyhVs7nYxo0Rg=="),
    (42, "YE7Zd-POmhwrvXqiP8tozg=="),
    (3.14, "GsQFicPO3fpRsbx63XtozQ=="),
    ("", "bd0H2eAFLX4ZcalQ9Ip_yw=="),
    ("hello", "IfgaF7i8mVVAl2kylWfqOw=="),
    ([], "wyM70eXPE_VqGMKFEwfzQw=="),
    ([1, 2, 3], "hHwtSRMxaRKf12HM1jsW0Q=="),
    ({}, "RoBn8-L4hTHbJUyclrDjNQ=="),
]


@pytest.mark.parametrize("value, expected", CASES)
def test_digest(value, expected):
    assert digest(value) == expected
    assert len(digest(value)) == 24
