# File name
names = []
ps_codes = []
loaded_data = {}
file_name_end = "_settings.json"
webhook = "https://discord.com/api/webhooks/1069012888028721283/" \
          "2aNLdjWTxv5GgkhUMshEYhpiz173W4_7QM7Y8IGqXKjy0XKDK1U0Hp1nQVDA1Kh6v36b"


def get_codes():
    with open("../PrivateServers.txt") as f:
        lines = f.readlines()
        for line in lines:
            ps_codes.append(line.strip())
    print(ps_codes)


def get_names():
    with open("../AccountNames.txt") as f:
        lines = f.readlines()
        for line in lines:
            names.append(line.strip())
    print(names)


def load_data():
    get_names()
    get_codes()
    for name in names:
        for code in ps_codes:
            print("Loaded Account: {} With the Private Server Code: {}".format(name, code))
            loaded_data[name] = code
            ps_codes.remove(code)
            break
    print("\n", loaded_data)


load_data()


# config management
def config(code, _webhook):
    config_template = '''
    {
      "648454481": {
        "TimeKick": "15",
        "SecureMode": true,
        "itemNotifier": true,
        "PSCode": "%s",
        "autoJoinPS": true,
        "showFruits": true,
        "AutoAcceptParty": false,
        "LevelFarm": true,
        "WebHook": "%s",
        "MobFarmType": "Default",
        "statSwordMastery": true,
        "teleportSpeed": 20,
        "autoKick": true,
        "LevelFarmMode": "Katana",
        "AutoReconnect": true
      }
    }
    ''' % (code, _webhook)
    return config_template


def make_files():
    for name in names:
        file_name = name + file_name_end
        config(loaded_data[name], webhook)
        with open(file_name, "w") as f:
            f.write(str(config(loaded_data[name], webhook)))


make_files()