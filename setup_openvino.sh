wget https://storage.openvinotoolkit.org/repositories/openvino/packages/2021.1/l_openvino_toolkit_runtime_raspbian_p_2021.1.110.tgz
sudo mkdir -p /opt/intel/openvino2021
sudo tar -xf  l_openvino_toolkit_runtime_raspbian_p_2021.1.110.tgz --strip 1 -C /opt/intel/openvino2021
sudo apt install cmake -y
sudo ln -s /opt/intel/openvino2021 /opt/intel/openvino
source /opt/intel/openvino/bin/setupvars.sh
sudo usermod -a -G users "$(whoami)"
exec $SHELL
sh /opt/intel/openvino/install_dependencies/install_NCS_udev_rules.sh

