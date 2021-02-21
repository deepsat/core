# DeepSat core
The main deamon running the DeepSat cansat.

## Requirements
- run `source setupvars.sh` always on starting a new terminal
    - it assumes the OpenVino is installed at `/opt/intel/openvino_2021`
    - you can add it to your pyenv's `activate` etc.
- Python version: `3.7.9`
    - developer pip requirements are listed in `requirements-dev.txt`
    - deploy pip requirements are listed in `reqirements-deploy.txt`
- OpenVino toolkit installed
    - inference engine
    - model optimizer

## Deployement prerequesites

### RPI setup
1. Copy `dhcpcd.conf` to `/etc/`
2. Follow the steps from [here](https://www.arducam.com/docs/arducam-obisp-mipi-camera-module/3-use-on-raspberry-pi/3-0-emergent-temporary-driver-for-the-lastest-rpi-2020-12-02-update/).
    - `wget https://github.com/ArduCAM/Arducam_OBISP_MIPI_Camera_Module/releases/download/v2.0/arducam_obisp_camera_driver.tar.gz`
    - `tar zxvf arducam_obisp_camera_driver.tar.gz`
    - `cd arducam_obisp_camera_driver`
    - `./install.sh`
3. Copy `config.txt` to `/boot/`

### pyenv 
1. Install prerequesites:
`libbz2-dev libssl-dev libreadline-dev build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git`
2. `curl https://pyenv.run | bash`
3. `pyenv install 3.7.9`
4. `pyenv global 3.7.9`
5. `pip install wheel`

### rtcbot 
Prerequesites:
`python3-numpy python3-cffi python3-aiohttp libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev libopus-dev libvpx-dev pkg-config libsrtp2-dev python3-opencv pulseaudio`

