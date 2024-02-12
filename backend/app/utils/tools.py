def deepupdate(original_dict, new_dict):
    """Merge recursively two dictionaries"""
    for key, value in new_dict.items():
        if isinstance(value, dict) and key in original_dict and isinstance(original_dict[key], dict):
            deepupdate(original_dict[key], value)
        else:
            original_dict[key] = value
