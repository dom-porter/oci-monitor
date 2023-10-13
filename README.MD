# Description
This script will monitor all the compute instances in an Oracle Cloud Tenancy and if any are down will attempt to start them.

# Installation
```
git clone https://github.com/dom-porter/oci-monitor.git

cd oci-monitor

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

deactivate

cd ..
```

# Get your API key and PEM file

Login to your Oracle Cloud account. In the top right, click on your account icon. </br>
Choose your tenancy (it should be the first option). </br>
On the left-hand side of the next screen click API Keys.</br>
Click the 'Add API Key' button.</br>
Choose 'Generate API Key Pair' and click the 'Download Private Key' button. Then click the 'Add' button.</br>
Copy the 'Configuration File Preview'.

# Create the Config
Rename the config/oracle.ini.example to config/oracle.ini</br>
Replace the contents with the 'Configuration File Preview' copied earlier.</br>

Place the .pem file in to the /config directory and update the config file entry 'key_file=' with the filename.

```
[DEFAULT]
user=ocid1.user.oc1..aaaaaaaa65abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmn
fingerprint=11:22:33:44:55:66:77:88:99:0a:1b:2c:3d:4e:5f:6g
tenancy=ocid1.tenancy.oc1..aaaaaaaa5nfwo53cezleyy6t73v6rn6knhu3molvptnl3kcq34l5ztenancy
region=us-phoenix-1
key_file=./config/oci_api_key.pem

```

# Running
```
./oci-monitor/venv/bin/python ./oci-monitor/main.py
```

## License
Apache License Version 2.0
