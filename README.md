### mobileGPT

# This is a python application using the Kivy library.


# After loading requirements.txt, then downloading android sdk, then enabling dev mode on android.


## Installing Buildozer
- pip3 install --upgrade buildozer
- sudo apt update
- sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
- pip3 install --user --upgrade Cython==0.29.33 virtualenv  # the --user should be removed if you do this in a venv
# add the following line at the end of your ~/.bashrc file
- export PATH=$PATH:~/.local/bin/


## Initializing Buildozer
- buildozer init
## Edit the buildozer.spec according to your apps specifications
- buildozer -v android debug
## Then wait a while for the building and compiling