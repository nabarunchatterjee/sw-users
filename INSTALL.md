Installation
============

Steps:

1. Copy `config/pypirc` and `config/pip.conf`

```
cp config/pypirc ~/.pypirc

mkdir -p ~/.pip && cp config/pip.conf ~/.pip
```

```
Note: Do not copy if these files already exist. Append appropriately
```

2. make `instal.sh` executable and run

```
chmod +x install.sh && ./install.sh
```

Description:

install.sh first creates a pypi server. Then it creates pip package and uploads to the created server.
Then it creates a web server and installs pip package from pypi server previously created

Further Improvements:
===

The db could have been separated to a different server.
Monitoring could be setup easily using Prometheus/Sensu/Shinken
Test cases should be run before deploying


Tools:
===

Ansible for config management
Vagrant for infra provisioning
