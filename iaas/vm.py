from dataclasses import dataclass

from oci.core.models import instance


@dataclass
class VirtualMachine:
    display_name: str
    vm_id: str
    state: str


def oracle_vm_factory(vm: instance) -> VirtualMachine:
    """
    Creates an instance of VirtualMachine class.
    Factory does not maintain any of the instances it creates.
    """
    return VirtualMachine(
        display_name=vm.display_name,
        vm_id=vm.id,
        state=vm.lifecycle_state,
    )
