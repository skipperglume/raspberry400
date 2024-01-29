# DHT sensor with Raspberry Pi 400
## Beginning with Pi's GPIO

Setting Up required packages:

    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    cd Adafruit_Python_DHT
    sudo python3 setup.py install

Check that GPIO is enabled:

    sudo raspi-config

After window opens got to `Interface` and `Enable` I2C and SPI 

Or: 

    sudo raspi-config nonint do_rgpio <0/1>

Check that python's GPIO package (rpi.gpio) is installed:

    sudo apt install python3-rpi.gpio




### SSH-key from github:
[Link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent):

    ssh-keygen -t ed25519 -C "your_email@example.com"




##