from enum import Enum

class PlayerClass(Enum):
    WARRIOR = "warrior"
    MAGE =    "mage"

BASE_STATS:dict[PlayerClass,dict[str,int]] = {
    PlayerClass.WARRIOR : {
        "base_physical_attack":120,
        "base_special_attack":70,
        "base_physical_defense":120,
        "base_special_defense":70,
        "max_health":100,
        "base_speed":70,
        "max_physical_stamina":100,
        "max_special_stamina":40,
    },
    PlayerClass.MAGE : {
        "base_physical_attack":70,
        "base_special_attack":120,
        "base_physical_defense":70,
        "base_special_defense":120,
        "max_health":70,
        "base_speed":100,
        "max_physical_stamina":40,
        "max_special_stamina":100,
    }

}
