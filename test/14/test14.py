from shutit_module import ShutItModule


class test14(ShutItModule):


	def build(self, shutit):
		a = '''a
b
c
d
e'''
		shutit.send_file('/tmp/a',a)
		md5sum1 = shutit.send_and_get_output('md5sum /tmp/a')
		shutit.add_line_to_file('e','/tmp/a')
		md5sum2 = shutit.send_and_get_output('md5sum /tmp/a')
		if md5sum1 != md5sum2:
			shutit.fail('file was changed 1')

		md5sum1 = shutit.send_and_get_output('md5sum /tmp/a')
		shutit.add_line_to_file("abc'def",'/tmp/a')
		md5sum2 = shutit.send_and_get_output('md5sum /tmp/a')
		if md5sum1 == md5sum2:
			shutit.fail('file was not changed 2')

		md5sum1 = shutit.send_and_get_output('md5sum /tmp/a')
		shutit.add_line_to_file("abc'def",'/tmp/a')
		md5sum2 = shutit.send_and_get_output('md5sum /tmp/a')
		if md5sum1 != md5sum2:
			shutit.fail('file was changed 3')

		md5sum1 = shutit.send_and_get_output('md5sum /tmp/a')
		shutit.delete_text("a",'/tmp/a')
		shutit.pause_point('cat /tmp/a')
		md5sum2 = shutit.send_and_get_output('md5sum /tmp/a')
		if md5sum1 == md5sum2:
			shutit.fail('file was not changed 4')

		md5sum1 = shutit.send_and_get_output('md5sum /tmp/a')
		shutit.delete_text("""d
e""",'/tmp/a')
		shutit.pause_point('cat /tmp/a')
		md5sum2 = shutit.send_and_get_output('md5sum /tmp/a')
		if md5sum2 != '3a7a52a60d0413b5614fb9b889b6a3d4  /tmp/a':
			shutit.fail('md5sum wrong 5')
		if md5sum1 == md5sum2:
			shutit.fail('file was not changed 5')

		return True

	def get_config(self, shutit):
		return True

	def test(self, shutit):
		# For test cycle part of the ShutIt build.
		return True

	def finalize(self, shutit):
		# Any cleanup required at the end.
		return True
	
	def is_installed(self, shutit):
		return False


def module():
	return test14(
		'test.test14.test14.test14', 1627321857.00,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)

