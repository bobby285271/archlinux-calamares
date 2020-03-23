#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import libcalamares
from pathlib import Path

root_mount_point = libcalamares.globalstorage.value("rootMountPoint")
    
def run():
    """
    Installing: base grub efibootmgr os-prober linux linux-firmware vi nano networkmanager.
    """

    PACSTRAP = "sudo /usr/bin/pacstrap_calamares"
    PACKAGES = "base grub efibootmgr os-prober linux linux-firmware vi nano networkmanager"

    subprocess.call(PACSTRAP.split(' ') + [root_mount_point] + PACKAGES.split(' '))
