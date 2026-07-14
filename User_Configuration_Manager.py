test_settings = {'Name': 'Jasmeh',
                 'Age': 'Old',
                 'College': 'Thapar'}


def add_setting(setting, pair):
    key, value = pair
    key = key.lower()
    if key in setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    value = value.lower()
    setting[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(setting, pair):
    key, value = pair
    key = key.lower()
    if key not in setting:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    value = value.lower()
    setting[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(setting, pair):
    key = pair.lower()
    if key in setting:
        del setting[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(setting):
    if not setting:
        return 'No settings available.'

    result = ['Current User Settings:']
    for key, value in setting.items():
        result.append(f"{key.capitalize()}: {value}")

    return '\n'.join(result) + '\n'


