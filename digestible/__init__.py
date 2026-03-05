# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Top-level module for digestible."""

import base64
import hashlib
import json


# A recursive type describing any value representable in JSON.
#
# The six JSON kinds map to Python as follows:
#   JSON object  -> dict[str, JSONType]
#   JSON array   -> list[JSONType]
#   JSON string  -> str
#   JSON number  -> int | float
#   JSON true    -> True   (bool is a subtype of int)
#   JSON false   -> False
#   JSON null    -> None
#
type JSONType = (
    dict[str, JSONType]
    | list[JSONType]
    | str
    | int
    | float
    | bool
    | None
)


def digest(o: JSONType) -> str:
    """Return a length-24 Base64URL digest of the JSON encoding of *o*."""
    h = hashlib.shake_128()
    h.update(b"digestible")
    encoder = json.JSONEncoder(
        skipkeys=False,
        ensure_ascii=True,
        check_circular=True,
        allow_nan=True,
        sort_keys=True,          # non-default
        indent=None,
        separators=(",", ":"),   # non-default
        default=None,
    )
    for chunk in encoder.iterencode(o):
        h.update(chunk.encode())
    return base64.urlsafe_b64encode(b"\xf7\xb7" + h.digest(16)).decode()
