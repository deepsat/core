# DeepSat core
The main deamon running the DeepSat cansat.

## Requirements
- run `source setupvars.sh` always on starting a new terminal
    - it assumes the OpenVino is installed at `/opt/intel/openvino_2021`
    - you can add it to your pyenv's `activate` or somethin'
- Python version: `3.7.9`
- OpenVino toolkit installed
    - inference engine
    - model optimizer