"""Base entity for RewIRe devices."""
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import RewireCoordinator


class RewireEntity(CoordinatorEntity[RewireCoordinator]):
    """Defines a base Rewire entity."""

    def __init__(self, coordinator: RewireCoordinator, entry_id: str) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self._entry_id = entry_id
        self._attr_unique_id = f"{DOMAIN}_{entry_id}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry_id)},
            name=self.coordinator.config_entry.data.get("name", "IR Device"),
            manufacturer="IR Remote Control",
            model=self.coordinator.config_entry.data.get("device_type", "Generic"),
        )
