# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Top-level module for digestible."""


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
