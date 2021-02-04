import json
import os
import sys
import argparse

from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

KERNEL_NAME = "Hydra"

kernel_json = {
    "argv": [sys.executable, "-m", "hydra_kernel", "-f", "{connection_file}"],
    "display_name": KERNEL_NAME,
    "language": "python",
    # 'metadata': {},
    # 'env': {
    #   'PS1': '$'
    # }
}


def install_kernel_spec(user=True, prefix=None):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)  # Starts off as 700, not user readable
        with open(os.path.join(td, "kernel.json"), "w") as f:
            json.dump(kernel_json, f, sort_keys=True)
        KernelSpecManager().install_kernel_spec(td, "hydra", user=user, prefix=prefix)


def _is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False  # assume not an admin on non-Unix platforms


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=f"Install kernelspec for {KERNEL_NAME} Kernel"
    )

    prefix_locations = parser.add_mutually_exclusive_group()
    prefix_locations.add_argument(
        "--user", help="Install kernelspec in user homedirectory", action="store_true"
    )
    prefix_locations.add_argument(
        "--sys-prefix",
        help="Install kernelspec in sys.prefix. Useful in conda / virtualenv",
        action="store_true",
        dest="sys_prefix",
    )
    prefix_locations.add_argument(
        "--prefix", help="Install kernelspec in this prefix", default=None
    )

    args = parser.parse_args(argv)

    user = False
    prefix = None
    if args.sys_prefix:
        prefix = sys.prefix
    elif args.prefix:
        prefix = args.prefix
    elif args.user or not _is_root():
        user = True

    install_kernel_spec(user=user, prefix=prefix)


if __name__ == "__main__":
    main()
