# Dyson IR Control for Home Assistant

This custom component allows you to control Dyson AM09 (and potentially AM07/AM11) fans and heaters using any IR blaster configured as a `remote` entity in Home Assistant (e.g., Broadlink, ESPHome).

## Features
- **Power Control**: Turn the device on/off.
- **Speed Control**: Set fan speed (Low/Medium/High or percentage).
- **Oscillation**: Toggle oscillation.
- **State Management**: Estimates device state (speed, power, oscillation) since IR is one-way.

## Installation

### Via HACS
1.  Add this repository to `HACS > Integrations > 3 dots > Custom repositories`. Copy/paste the repository link and select the repository type as "Integration".
    ```
    https://github.com/sahilanguralla/hacs.git
    ```
2.  Search for "Dyson IR" and install.
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

## Development

### Setup
1. Install development dependencies:
   ```bash
   pip install -r requirements_tests.txt
   ```

2. Setup git hooks:
   ```bash
   ./scripts/setup-hooks.sh
   ```

### Committing Changes
- **Interactive Mode**: Run `git commit` (without `-m`) to launch the interactive commit wizard
- **Manual Mode**: Run `git commit -m "feat(scope): description"` to write your own message
- All commits are validated against [Conventional Commits](https://www.conventionalcommits.org/) format

### Versioning
- Version bumps happen automatically in Pull Requests based on commit types:
  - `feat:` → Minor version bump (e.g., 1.0.0 → 1.1.0)
  - `fix:` → Patch version bump (e.g., 1.0.0 → 1.0.1)
  - `feat!:` or `BREAKING CHANGE:` → Major version bump (e.g., 1.0.0 → 2.0.0)
- When you merge a PR with "Squash and Merge", the version bump is included in the single commit
# Debug test
# Test
