def load_configuration(**kwargs):
    
    return dict(total_settings_count = len(kwargs),
                 setting_names = list(kwargs.keys()),
                 original_configuration = set(kwargs.values()))

print(load_configuration(
    host="10.0.0.1",
    port=8080,
    protocol="https"
))