DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ershadul Hoque Sarker', 'ershadulhoque@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
if DEBUG:
    DATABASE_NAME = 'alkawsarsite'
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = ''
else:
    DATABASE_NAME = 'ershadul_kawsar'
    DATABASE_USER = 'ershadul_kawsar'
    DATABASE_PASSWORD = 'ed203b20'
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
