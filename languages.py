languages = (('bengali', 'Bengali'), ('english', 'English'))
default_language = 'bengali'

def is_valid_language(language):
	for lang in languages:
		if lang[0] == language:
			return True
	return False