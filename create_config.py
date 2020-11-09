import configparser

config = configparser.ConfigParser()
config["SOUNDNAMES"] = {

}

config['SOUNDCOLOR'] = {
    'C': 0,
    'C#': 30,
    'D': 60,
    'D#': 90,
    'E': 120,
    'F': 150,
    'F#': 180,
    'G': 210,
    'G#': 240,
    'A': 270,
    'A#': 300,
    'B': 330,
}

config['SOUNDBOARD'] = {
    'marked_steps': '3, 5, 7, 9, 12, 15, 17',
    'guitar_tuning': 'e/4,b/3,g/3,d/3,a/2,e/2',
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)