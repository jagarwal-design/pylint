# pylint: disable=missing-module-docstring,import-error,unused-import,wrong-import-order
# pylint: disable=import-outside-toplevel

import json
import re
import re as re1  # [reimported]

from . import json as my_json


def import_local_json():
    """A function-local relative import also differs from the absolute import."""
    from . import json as local_json

    return local_json
