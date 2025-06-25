"""Constants for teamspeak."""
# Base component constants
NAME = "Teamspeak 3 Server"
DOMAIN = "teamspeak"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "2025.06.25.2"
MANUFACTURER = "TeamSpeak Systems, Inc"
ATTRIBUTION = f".a.ta from this is provided by a Teamspeak 3 Server by {MANUFACTURER}."
ISSUE_URL = "https://github.com/Larsiiii/teamspeak-homeassistant-integration/issues"

# Icons
ICON_SERVER = "mdi:headset"
ICON_HUMAN_USER = "mdi:account-multiple"
ICON_ALL_CONNECTIONS = "mdi:account-multiple"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_HOST = "host"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
