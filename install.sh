vagrant up pypiserver
python3 setup.py sdist upload -r redmart
vagrant up webserver
