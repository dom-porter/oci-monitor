from typing import Protocol, List
from iaas.enums import Providers
from iaas.vm import VirtualMachine, oracle_vm_factory
from oci import config
from oci.core import ComputeClient, VirtualNetworkClient
from oci.exceptions import ServiceError


class Client(Protocol):
    """ Used as an interface for all IaaS API clients """

    def get_all_vms(self) -> List:
        return []

    def stop_vm(self, vm: VirtualMachine) -> str:
        return ""

    def start_vm(self, vm: VirtualMachine) -> str:
        return ""

    def restart_vm(self, vm: VirtualMachine) -> str:
        return ""

    def get_public_ips(self, vm: VirtualMachine) -> List:
        return []


class OracleClient:
    """ Oracle Cloud client """

    def __init__(self):
        self._config = config.from_file(file_location="./config/oracle.ini")
        config.validate_config(self._config)  # Raises InvalidConfig exception if config not correct
        self._compute_client = ComputeClient(self._config)

    def get_all_vms(self) -> List:
        """ Returns a list of VirtualMachine class instances """

        try:
            vm_instances = self._compute_client.list_instances(compartment_id=self._config["tenancy"]).data
            return_list = [oracle_vm_factory(vm) for vm in vm_instances]
            return return_list
        except ServiceError as s:
            print(f"ERROR: failed to obtain a list of compute VM instances due to '{s.message}'")
            return []

    def stop_vm(self, vm: VirtualMachine) -> str:
        """ Stops the supplied VM instance """

        instance = self._compute_client.instance_action(vm.vm_id, action="STOP")
        return instance.data.lifecycle_state

    def start_vm(self, vm: VirtualMachine) -> str:
        """ Starts the supplied VM instance """

        instance = self._compute_client.instance_action(vm.vm_id, action="START")
        return instance.data.lifecycle_state

    def restart_vm(self, vm: VirtualMachine) -> str:
        """ Restarts the supplied VM instance """

        instance = self._compute_client.instance_action(vm.vm_id, action="SOFTRESET")
        return instance.data.lifecycle_state

    def get_public_ips(self, vm: VirtualMachine) -> List:
        """ Returns a list of all public IP addresses assigned to the VM instance """

        return_list = []

        virtual_network_client = VirtualNetworkClient(self._config)

        vnic_attachments = self._compute_client.list_vnic_attachments(
            compartment_id=self._config["tenancy"],
            instance_id=vm.vm_id
        ).data

        # get a list of vNICs from the vNIC attachement. Most often you
        # find a single vNIC, but it's possible to have multiple.
        vnics = [virtual_network_client.get_vnic(va.vnic_id).data for va in vnic_attachments]
        for vnic in vnics:
            if vnic.public_ip:
                return_list.append(vnic.public_ip)
        return return_list


class AWSClient:
    """ TO DO """

    def get_all_vms(self) -> List:
        return []

    def stop_vm(self, vm: VirtualMachine) -> str:
        return ""

    def start_vm(self, vm: VirtualMachine) -> str:
        return ""

    def restart_vm(self, vm: VirtualMachine) -> str:
        return ""

    def get_public_ips(self, vm: VirtualMachine) -> List:
        return []


FACTORIES = {
    Providers.ORACLE: OracleClient(),
    Providers.AWS: AWSClient()
}


def client_factory(provider: Providers) -> Client:
    """
    Creates an instance of an IaaS provider client.
    Factory does not maintain any of the instances it creates.
    """

    return FACTORIES[provider]
