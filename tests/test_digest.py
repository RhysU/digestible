# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import pytest

from digestible import digest

CASES = [
    (None, "ICYq0uGIze2WItsn6FZqPewx"),
    (True, "ICb2modAlHOf5-xtjBNNmRP1"),
    (False, "ICbPuRvc1wVYteus9dZnlbR2"),
    (0, "ICZijnnPeUjNHKFWzudjGjRG"),
    (42, "ICZgTtl3486aHCu9eqI_y2jO"),
    (3.14, "ICYaxAWJw87d-lGxvHrde2jN"),
    ("", "ICZt3QfZ4AUtfhlxqVD0in_L"),
    ("hello", "ICYh-BoXuLyZVUCXaTKVZ-o7"),
    ([], "ICbDIzvR5c8T9WoYwoUTB_ND"),
    ([1, 2, 3], "ICaEfC1JEzFpEp_XYczWOxbR"),
    ({}, "ICZGgGfz4viFMdslTJyWsOM1"),
]


@pytest.mark.parametrize("value, expected", CASES)
def test_digest(value, expected):
    assert digest(value) == expected
    assert len(digest(value)) == 24
