"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule

class template(ShutItModule):

	def is_installed(self, shutit):
		return False

	def build(self, shutit):

		return True

	#def get_config(self, shutit):
	#    return True

	#def check_ready(self, shutit):
	#    return True
	
	#def start(self, shutit):
	#    return True

	#def stop(self, shutit):
	#    return True
	#def finalize(self, shutit):
	#    return True

	#def remove(self, shutit):
	#    return True

	#def test(self, shutit):
	#    return True

def module():
	return template(
		GLOBALLY_UNIQUE_STRING, FLOAT,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)

