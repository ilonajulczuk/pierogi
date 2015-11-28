# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.hostname = "pierogi"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
	vb.memory = 512
	vb.cpus = 2
  end

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network :private_network, ip: "192.168.11.30", port: 2200

  # config.vm.synced_folder "../", "/home/vagrant/src/"

  config.vm.provision :ansible do |ansible|
     ansible.groups = {
       "default" => ["default"]
     }
     ansible.playbook = "devel.yml"
  end


  # postgresql-9.3 python-dev python-virtualenv
end

