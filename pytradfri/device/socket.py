"""Represent a socket."""
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from ..const import ATTR_DEVICE_STATE, ATTR_ID


class SocketResponse(BaseModel):
    """Represent API response for a blind."""

    id: int = Field(alias=ATTR_ID)
    state: int = Field(alias=ATTR_DEVICE_STATE)


if TYPE_CHECKING:
    # avoid cyclic import at runtime.
    from . import Device


class Socket:
    """Represent a socket."""

    def __init__(self, device: Device, index: int) -> None:
        """Create object of class."""
        self.device = device
        self.index = index

    @property
    def state(self) -> bool:
        """State."""
        return self.raw.state == 1

    @property
    def raw(self) -> SocketResponse:
        """Return raw data that it represents."""
        socket_control_response = self.device.raw.socket_control
        assert socket_control_response is not None
        return socket_control_response[self.index]

    def __repr__(self) -> str:
        """Return representation of class object."""
        state = "on" if self.state else "off"
        return f"<Socket #{self.index} - name: {self.device.name}, state: {state}>"
