#!/usr/bin/env python

import subprocess
from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("--version", action="store", type="string", dest="version",
                        help="Build verson of EXOS VM")
    (options, args) = parser.parse_args()

    subprocess.call('rm -rf exos_{}'.format(options.version).split())

    subprocess.call('packer build -var version={} exos_iso.json'.format(options.version).split())
    subprocess.call('packer build -var version={} exos_vagrant.json'.format(options.version).split())
    subprocess.call('vagrant box remove exos_{}'.format(options.version).split())
    subprocess.call('vagrant box add exos_{}/exos_{}.box --name exos_{}'.format(options.version, options.version, options.version).split())

if __name__ == "__main__":
    main()
