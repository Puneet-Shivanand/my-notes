## Install salt
        'sudo apt-get --yes -q install python-software-properties',
        'wget https://bootstrap.saltstack.com -O install_salt.sh',
        'sudo sh install_salt.sh -P',
        'sudo apt-get --yes -q install salt-master',
        'sudo apt-get --yes -q install salt-minion',



## Configure Salt
    'sudo cp salt/start/minion /etc/salt/',
    'sudo cp salt/start/master /etc/salt/',
    'sudo service salt-master restart',
    'sudo service salt-minion restart',


## Accept keys
    sudo salt-key -A
    sudo salt '*' state.highstate saltenv=base
    
## Run salt cmds
  ### Find available minions
     salt '*' test.ping
  ### Install on specific minion
    salt '03767c255555' cmd.run 'yum install -y python-pip'



