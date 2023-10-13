import logging
import logging.handlers
from time import gmtime

from iaas.client import client_factory
from iaas.enums import Providers


def configure_logging():
    handler = logging.handlers.RotatingFileHandler(filename="oci-monitor.log",
                                                   maxBytes=20000,
                                                   backupCount=2,
                                                   encoding="utf-8")

    formatter = logging.Formatter(
        '%(asctime)s %(name)-15s [%(process)s] [%(thread)d] [%(levelname)s] %(message)s')
    formatter.converter = gmtime
    handler.setFormatter(formatter)

    # set the root logger level to info
    logging.basicConfig(handlers=[handler], level=logging.INFO)


def main():
    logger = logging.getLogger("oci-monitor")
    try:
        client = client_factory(Providers.ORACLE)
        all_vms = client.get_all_vms()
        for vm in all_vms:
            if vm.state.upper() == "STOPPED":
                print(f"{vm.display_name} not running. Starting...")
                logger.error(f"{vm.display_name} not running. Starting...")

                client.start_vm(vm)
            else:
                print(f"{vm.display_name} -> {vm.state}")
                logger.debug(f"{vm.display_name} -> {vm.state}")
    except Exception as e:
        print(e)
        logger.error(e)


if __name__ == '__main__':
    configure_logging()
    main()
