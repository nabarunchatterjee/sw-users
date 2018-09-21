# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.define "pypiserver" do |pypi|
    pypi.vm.network "private_network", ip: "192.168.33.10"
    pypi.vm.provision :ansible do |ansible|
      ansible.playbook = "ansible/pypi.yml"
    end
  end

  config.vm.define "webserver" do |web|
    web.vm.network "private_network", ip: "192.168.33.20"
    web.vm.provision :ansible do |ansible|
      ansible.playbook = "ansible/web.yml"
      ansible.extra_vars = {
        pypi_server: "192.168.33.10",
        app_name: "swagger_server",
        app_version: "1.0.4",
        app_port: "8000"
      }
    end
  end

end

