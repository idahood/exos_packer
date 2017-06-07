# exos_packer
## Requirements
Requires Packer v1.1.0-dev or greater

## Usage
Downloads and builds a Vagrant box based on the ISOs available at Extreme's GitHub repo.
```
packer build -var 'version=22.2.1.5' exos_iso.json
packer build -var 'version=22.2.1.5' exos_vagrant.json
```
