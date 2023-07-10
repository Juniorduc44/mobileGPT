### mobileGPT

# This is a python application using the Kivy library.


# After loading requirements.txt, then downloading android sdk, then enabling dev mode on android.

- buildozer init
- .\adb start-server
- .\adb devices
- buildozer -v android debug

on ubuntu zlib had to be installed before buildozer stuff
- sudo apt-get install zlib1g-dev
- buildozer -v android debug