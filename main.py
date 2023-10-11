from iaas.client import client_factory
from iaas.enums import Providers


def main():
    client = client_factory(Providers.ORACLE)
    all_vms = client.get_all_vms()
    for vm in all_vms:
        if vm.state.upper() == "STOPPED":
            print(f"{vm.display_name} not running. Starting....")
            client.start_vm(vm)
        else:
            print(f"{vm.display_name} -> {vm.state}")


if __name__ == '__main__':
    main()
