"""Module for IQ option API ssid websocket chanel."""
from pyiqoptionapi.ws.chanels.base import Base


class Ssid(Base):
    """Class for IQ option API ssid websocket chanel."""

    name = "ssid"

    def __call__(self, ssid):
        """Method to send message to ssid websocket chanel.
        :param ssid: The session identifier.
        """
        self.send_websocket_request(self.name, ssid)