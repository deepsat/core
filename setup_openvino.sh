FILE=l_openvino_toolkit_runtime_raspbian_p_2021.1.110.tgz

if [ -f "$FILE" ]; then
    echo "Using downloaded $FILE"
else
    wget https://storage.openvinotoolkit.org/repositories/openvino/packages/2021.1/$FILE
fi

sudo mkdir -p /opt/intel/openvino_2021
sudo tar -xf $FILE --strip 1 -C /opt/intel/openvino_2021
sudo apt install cmake -y
sudo ln -sfn /opt/intel/openvino_2021 /opt/intel/openvino
source /opt/intel/openvino/bin/setupvars.sh
sudo usermod -a -G users "$(whoami)"
exec $SHELL
source /opt/intel/openvino/bin/setupvars.sh
sh /opt/intel/openvino/install_dependencies/install_NCS_udev_rules.sh

