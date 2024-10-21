# Check that a feature is enabled
def is_feature_enabled(settings: str, setting_index: int) -> bool:
    index = setting_index - 1
    return settings[index] == '1'

# Test cases for `is_feature_enabled` function
print(is_feature_enabled('00000000', 7))  # Output: False
print(is_feature_enabled('00000010', 7))  # Output: True
print(is_feature_enabled('11111111', 4))  # Output: True

# Write and read user settings using bitwise shifting to conserve space
def write_settings(settings_list: list) -> int:
    settings_value = 0    
    for i, setting in enumerate(settings_list):
        if setting:
            settings_value |= (1 << i)
    return settings_value

def read_settings(settings_value: int) -> list:
    return [(settings_value & (1 << i)) != 0 for i in range(8)]
