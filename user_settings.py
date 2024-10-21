# Check that a feature is enabled
def is_feature_enabled(settings: str, setting_index: int) -> bool:
    index = setting_index - 1
    return settings[index] == '1'

# Test cases for `is_feature_enabled` function
print(is_feature_enabled('00000000', 7))  # Output: False
print(is_feature_enabled('00000010', 7))  # Output: True
print(is_feature_enabled('11111111', 4))  # Output: True
