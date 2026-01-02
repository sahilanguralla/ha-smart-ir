# Dyson IR Control for Home Assistant

This custom component allows you to control Dyson AM09 (and potentially AM07/AM11) fans and heaters using any IR blaster configured as a `remote` entity in Home Assistant (e.g., Broadlink, ESPHome).

## Features
- **Power Control**: Turn the device on/off.
- **Speed Control**: Set fan speed (Low/Medium/High or percentage).
- **Oscillation**: Toggle oscillation.
- **State Management**: Estimates device state (speed, power, oscillation) since IR is one-way.

## Installation

### Via HACS
1.  Add the repository to HACS custom repositories.
2.  Install "Dyson IR".
3.  Restart Home Assistant.

## Configuration

1.  Go to **Settings > Devices & Services**.
2.  Click **Add Integration** and search for "Dyson IR".
3.  **Step 1**: Select your device type (AM09, AM07, AM11) and choose your IR blaster entity (e.g., `remote.broadlink_living_room`).
4.  **Step 2**: Enter the Base64 IR codes for each command.
    *   You can learn these codes using your IR blaster's learning mode via the `remote.learn_command` service.
    *   The setup wizard requires codes for: Power On, Power Off, Speed Up, Speed Down, Oscillate Toggle.
    *   (AM09 Only) Heat On/Off codes are optional but recommended.

## Usage

Once added, a new fan entity (e.g., `fan.dyson_am09`) will be created. You can control it via the standard Fan card in Lovelace.

### Notes
- **Syncing**: Since IR is send-only, the state in Home Assistant may get out of sync if you use the physical remote. Use the UI to "reset" the state (e.g., turn it off and on again in HA).
- **Speed**: The integration simulates absolute speed setting by sending "Speed Up" / "Speed Down" commands multiple times from a known state.
