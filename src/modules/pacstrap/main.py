#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import libcalamares
from pathlib import Path

root_mount_point = libcalamares.globalstorage.value("rootMountPoint")
    
def run():
    """
    Installing base filesystem. Please wait! It may take some time!
    """

    PACSTRAP = "/usr/bin/pacstrap_calamares"
    PACKAGES = "base grub efibootmgr linux linux-firmware vi nano networkmanager"

    subprocess.call(PACSTRAP.split(' ') + [root_mount_point] + PACKAGES.split(' '))
