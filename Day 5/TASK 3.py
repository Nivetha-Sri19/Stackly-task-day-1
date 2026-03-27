def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0")