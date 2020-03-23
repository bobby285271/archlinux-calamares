#/bin/bash
cd /root/
git clone https://e.coding.net/bobby285271/calamares.git --depth=1 --branch=master --single-branch
cp -rpf ./archlinux-calamares/* ./calamares/
mkdir ./calamares/build/
cd ./calamares/build/
cmake ..
make
make install
mkdir /etc/calamares/
cp -p /root/archlinux-calamares/settings.conf /etc/calamares/
rm -rf /root/archlinux-calamares/ /root/calamares/ /root/build_calamares.sh
pacman -Rscun qt5-doc qt5-examples --noconfirm
