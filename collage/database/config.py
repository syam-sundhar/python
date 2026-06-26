import configparser
#create object
config=configparser.ConfigParser()
#reading files
config.read('config.ini')
#accessing values
host=config['DATABASE']['host']
user=config['DATABASE']['user']
password=config['DATABASE']['password']
port=config.getint("SETTINGS","port")
debug=config.getboolean("SETTINGS","debug")
# printing
print("host:",host)
print("user:",user)
print("password:",password)
print("---------------------")
print("port:",port)
print("debug:",debug)
print(type(debug))