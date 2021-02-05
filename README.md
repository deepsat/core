# DeepSat core
The main deamon running the DeepSat cansat.

## Requirements
- run `source setupvars.sh` always on starting a new terminal
    - it assumes the OpenVino is installed at `/opt/intel/openvino_2021`
    - you can add it to your pyenv's `activate` or somethin'
- Python version: `3.7.9`
    - developer pip requirements are listed in `requirements-dev.txt`
    - deploy pip requirements are listed in `reqirements-deploy.txt`
- OpenVino toolkit installed
    - inference engine
    - model optimizer

## Deployement prerequesites

```bash
pip install wheel
```
```bash
sudo apt-get install python3-numpy python3-cffi python3-aiohttp libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev libopus-dev libvpx-dev pkg-config libsrtp2-dev pulseaudio libgtk-3-dev
```
Additionaly on raspberry pi
```bash
sudo apt install libbz2-dev libssl-dev libreadline-dev
```
