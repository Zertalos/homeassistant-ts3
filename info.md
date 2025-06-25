[![hacs][hacsbadge]][hacs]

# Teamspeak 3 Server Integration for Home Assistant 🎮🎧🚀

*Seamless integration for your Teamspeak 3 Server into Home Assistant.*
**This updated version works with Homeassistant 2025.06 and later!**

**NOTE:** This project is a fork of the original work by [Larsiiii](https://github.com/Larsiiii/homeassistant-teamspeak), enhanced with new features and improvements. Please see the [original repository](https://github.com/Larsiiii/homeassistant-teamspeak) for additional context.

*DISCLAIMER:* This is a private, open-source project with no official affiliation with TeamSpeak Systems, Inc.

## 🧩 Features and Platforms

This component integrates the following platforms into your Home Assistant setup: 

| Platform | Description                                               |
| -------- | --------------------------------------------------------- |
| `sensor` | Displays general server information.                      |
| `sensor` | Shows number of connected real users.                     |
| `sensor` | Reports total connections, including real users and RCON. |

### 📊 Server Info Attributes

| Attribute           | Description                                          |
| ------------------- | ---------------------------------------------------- |
| `unique_identifier` | Unique identifier of the configured Teamspeak Server |
| `status`            | Server online/offline status                         |
| `name`              | Server name                                          |
| `platform`          | OS platform of the server (e.g. Windows, Linux, Mac) |
| `port`              | Port the server listens on                           |
| `version`           | Installed version of Teamspeak                       |
| `maxclients`        | Maximum allowed simultaneous client connections      |
| `reservedslots`     | Reserved slots                                       |
| `clientsonline`     | Total number of current client connections           |
| `clientconnections` | Number of active client connections                  |
| `channelsonline`    | Number of channels created                           |
| `created`           | Server creation timestamp                            |
| `uptime`            | Server uptime in seconds                             |

## 🛠️ Installation

### 📂 Via HACS

1. Install the integration directly using HACS by adding this repository to your HACS.

### ⚙️ Manual Installation

1. Open your Home Assistant config directory (where `configuration.yaml` is located).
2. Create the `custom_components` directory if it doesn't already exist.
3. Within `custom_components`, create a new directory called `teamspeak`.
4. Download all files from this repository's `custom_components/teamspeak/` directory.
5. Copy those files into your new `teamspeak` directory.
6. Restart Home Assistant.
7. Navigate to **Configuration → Integrations**, click `+`, then search for `Teamspeak 3 Server`.

Your setup directory structure will look like this: 

```
custom_components/teamspeak/
  translations/en.json
  translations/de.json
  __init__.py
  api.py
  config_flow.py
  const.py
  manifest.json
  sensor.py
```

## ⚙️ Configuration

Configure this integration through the UI as follows: 

1. Go to **Configuration → Integrations**, click `+` and search for `Teamspeak 3 Server`.
2. Enter the IP address of your Teamspeak 3 Server.
3. Enter the username and password for a Server Query Account. (Check your Teamspeak server logs after the first startup for credentials.).

## 🤝 Contributions

Your contributions and improvements are always welcome! Be sure to read the [Contribution guidelines](CONTRIBUTING.md).


***

[teamspeak3_server]: https://www.teamspeak.com/en/
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/Larsiiii/homeassistant-teamspeak.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/v/release/Zertalos/homeassistant-ts3.svg?style=for-the-badge
[releases]: https://github.com/Zertalos/homeassistant-ts3/releases
