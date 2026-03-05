# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import pytest

from digestible import digest

CASES = [
    (None, "97d-9qSWUtYSPKjlMnlWbxE8"),
    (True, "97fkPAmhLdLd7jre7Jrrf0RF"),
    (False, "97eO8qKY_t7EeY8lNAph4OTN"),
    (0, "97ccocUUr0bVGyCXZJho0MFC"),
    (42, "97f3vEnfUhC2FbZj4gHf5W9j"),
    (3.14, "97fbjnIwXU2TqnKAc3h0kkWJ"),
    ("", "97eySbZxnyd1xkN_e37yQFR3"),
    ("hello", "97f7PfQ6E3lNhyboe5m76DGh"),
    ([], "97dxLi1zrc5CNazSdOUBW_lS"),
    ([1, 2, 3], "97fuFQ_6Sr-kkHSvhHrRhR6o"),
    ({}, "97ecpWx_vL2YyaS-B1ThHz4q"),
    ({"a": {"b": 1}}, "97dMETvVOksC0S2Y5XLdTXu4"),
    ({"x": [1, {"y": 2}]}, "97d2VnVjd6ndeSx884oKLM3Z"),
    ([{"a": 1}, {"b": [2, 3]}], "97eocE501BP5dQbKp3oKyhg4"),
]


@pytest.mark.parametrize("value, expected", CASES)
def test_digest(value, expected):
    assert digest(value) == expected
    assert digest(value).startswith("97")
    assert not digest(value).endswith("==")
