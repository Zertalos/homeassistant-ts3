"""Sensor platform for Teamspeak 3 Server."""

from .const import (
    DEFAULT_NAME,
    DOMAIN,
    ICON_SERVER,
    ICON_HUMAN_USER,
    ICON_ALL_CONNECTIONS,
    SENSOR,
)
from .entity import TeamspeakEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """
    Set up the Teamspeak sensor platform.

    Retrieves the data coordinator from hass.data and adds all defined sensor entities
    to Home Assistant.
    """
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        [
            TeamspeakSensor(
                coordinator=coordinator,
                config_entry=entry,
                icon=ICON_SERVER),
            TeamspeakClientsOnlineSensor(
                coordinator=coordinator,
                config_entry=entry,
                name="Active Users",
                filter_func=lambda client: client.get("client_type") == "0",
                icon=ICON_HUMAN_USER,
            ),
            TeamspeakClientsOnlineSensor(
                coordinator=coordinator,
                config_entry=entry,
                name="Active Connections",
                filter_func=lambda client: True,
                icon=ICON_ALL_CONNECTIONS,
            ),
        ]
    )


class TeamspeakSensor(TeamspeakEntity):
    """
    Sensor representing the overall status of the Teamspeak 3 server.

    Displays the server's name and status (online/offline), as well as
    any extra state attributes returned by the coordinator.
    """

    @property
    def name(self):
        """
        Get the name of the sensor.

        Uses the 'serverinfo' data from the coordinator to return the
        server's configured name. Falls back to "No Connection to Server"
        if data is unavailable.

        :return: str
        """
        serverinfo = self.coordinator.data.get("serverinfo")
        if serverinfo is not None:
            return serverinfo.get("name")
        return "No Connection to Server"

    @property
    def state(self):
        """
        Get the current status of the Teamspeak server.

        Reads the 'status' value from the 'serverinfo' data block
        in the coordinator.

        :return: str status, or None if unavailable.
        """
        serverinfo = self.coordinator.data.get("serverinfo")
        if serverinfo is not None:
            return serverinfo.get("status")
        return None

    @property
    def icon(self):
        """
        Get the icon for this sensor.

        :return: str icon path
        """
        return ICON_SERVER

    @property
    def extra_state_attributes(self):
        """
        Get additional state attributes for the sensor.

        :return: dict of all coordinator data.
        """
        return self.coordinator.data


class TeamspeakClientsOnlineSensor(TeamspeakEntity):
    """
    Sensor representing the number of clients online based on a custom filter.

    :param coordinator: The DataUpdateCoordinator instance.
    :param entry: The config entry.
    :param name: Name of the sensor shown in Home Assistant.
    :param filter_func: A callable that accepts a client dict and returns True if it should be counted.
    """

    def __init__(self, coordinator, entry, name, filter_func, icon=ICON_SERVER):
        super().__init__(coordinator, entry)
        self._name = name
        self._filter_func = filter_func
        self._icon = icon

    @property
    def name(self):
        """
        Return the custom name for this sensor.

        :return: str
        """
        serverinfo = self.coordinator.data.get("serverinfo")
        if serverinfo is not None:
            servername = serverinfo.get("name")
            return f"{servername} {self._name}"
        return f"{self._name}"

    @property
    def state(self):
        """
        Count the number of clients that pass the filter function.

        :return: int or None if no serverinfo
        """
        serverinfo = self.coordinator.data.get("serverinfo")
        if not serverinfo:
            return None
        return len(
            [
                client
                for client in self.coordinator.data.get("clients", [])
                if self._filter_func(client)
            ]
        )

    @property
    def icon(self):
        """
        Return a default icon. Can be overridden per instance.

        :return: str
        """
        return self._icon
