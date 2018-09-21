import pypiserver
PACKAGES = '/home/{{ansible_ssh_user}}/packages'
HTPASSWD = '/home/{{ansible_ssh_user}}/htpasswd.txt'
application = pypiserver.app(root=PACKAGES, redirect_to_fallback=True, password_file=HTPASSWD)
