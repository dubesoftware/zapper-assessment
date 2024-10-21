# Check that a feature is enabled
def is_feature_enabled(settings: str, setting_index: int) -> bool:
    index = setting_index - 1
    return settings[index] == '1'
