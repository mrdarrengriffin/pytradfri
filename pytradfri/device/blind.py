"""Represent a blind."""
from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from ..const import ATTR_BLIND_CURRENT_POSITION

if sys.version_info < (3, 9, 2):
    from typing_extensions import TypedDict
else:
    from typing import TypedDict

BlindResponse = TypedDict(
    # The TypedDict:s below uses an alternative syntax due to the need of using strings
    # as keys: https://www.python.org/dev/peps/pep-0589/#alternative-syntax
    "BlindResponse",
    {
        "5536": int,  # Current blind position
        "9003": int,  # ID
    },
)

if TYPE_CHECKING:
    # avoid cyclic import at runtime.
    from . import Device


class Blind:
    """Represent a blind."""

    def __init__(self, device: Device, index: int) -> None:
        """Create object of class."""
        self.device = device
        self.index = index

    @property
    def raw(self) -> BlindResponse:
        """Return raw data that it represents."""
        blind_control_response = self.device.raw.blind_control
        assert blind_control_response is not None
        return blind_control_response[self.index]

    @property
    def current_cover_position(self) -> int:
        """Get the current position of the blind."""
        return self.raw[ATTR_BLIND_CURRENT_POSITION]
