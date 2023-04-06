import platform
import os

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("latter")._site_view_()
elif 'aarch' in arc:
	__import__("ll").cek_login()
else:
	exit(f' Unknow device machine {arc}')
