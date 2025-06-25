"""Teamspeak 3 Server entity class"""

from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME, VERSION, MANUFACTURER, ATTRIBUTION, ICON_SERVER


class TeamspeakEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry,unique_id_suffix, icon=ICON_SERVER):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self._unique_id_suffix = unique_id_suffix
        self._icon = icon

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        if self._unique_id_suffix:
            return f"{self.config_entry.entry_id}_{self._unique_id_suffix}"
        else:
            return f"{self.config_entry.entry_id}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.config_entry.entry_id)},
            "name": self.name,
            "model": self.coordinator.data.get("serverinfo").get("version"),
            "manufacturer": MANUFACTURER,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": str(self.coordinator.data.get("id")),
            "integration": DOMAIN,
        }
        
    @property
    def icon(self):
        """
        Return a default icon. Can be overridden per instance.

        :return: str
        """
        return self._icon