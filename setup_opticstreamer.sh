cd ~
sudo apt update
sudo apt install xvfb cmake git -y

curl https://download.libsodium.org/libsodium/releases/libsodium-1.0.18-stable.tar.gz --output libsodium.tar.gz
git clone http://github.com/zeromq/libzmq.git
git clone http://github.com/zeromq/zmqpp.git
git clone http://github.com/mitchellblaser/optic-streamer
git clone http://github.com/mitchellblaser/raspi-utils

sudo apt install python3-rpi.gpio
sudo apt install libopencv-dev -y

tar xzvf libsodium.tar.gz
cd libsodium-stable
./configure
make check -j4
sudo make install
sudo ldconfig
cd ..

cd libzmq
./autogen.sh
./configure --with-libsodium
make -j4
sudo make install
sudo ldconfig
cd ..

cd zmqpp
make -j4
sudo make install
cd ..

cd optic-streamer
mkdir build
cd build
cmake ..
make -j4
cd ..

echo ""
echo ""
echo ""
echo "Installation Complete."
echo "Run ./build/optic optic-conf to start."
echo ""
echo "You might want to modify /etc/dhcpcd.conf to add a static ip request"
echo "or /etc/rc.local to add gpio_shutdown.py and optic to run on startup."
