"""Template module for all connections classes."""
import logging
from abc import ABC, abstractmethod
from json import dumps
from os import fspath
from pathlib import Path
from typing import TYPE_CHECKING, Dict, FrozenSet, Optional, Union

# import stale to prevent circullar import
from ssh_utilities import connection

if TYPE_CHECKING:
    from ..typeshed import _SPATH
    from ._builtins import BuiltinsABC
    from ._os import OsABC
    from ._pathlib import PathlibABC
    from ._shutil import ShutilABC
    from ._subprocess import SubprocessABC

__all__ = ["ConnectionABC"]

logging.getLogger(__name__)


# TODO implement deepcopy and pickle protocols
class ConnectionABC(ABC):
    """Class defining API for connection classes."""

    __name__: str
    __abstractmethods__: FrozenSet[str]

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def close(self, *, quiet: bool = True):
        raise NotImplementedError

    @abstractmethod
    def ssh_log(self, log_file: Union[Path, str] = Path("paramiko.log"),
                level: str = "WARN"):
        raise NotImplementedError

    @property  # type: ignore
    @abstractmethod
    def builtins(self) -> "BuiltinsABC":
        raise NotImplementedError

    @builtins.setter  # type: ignore
    @abstractmethod
    def builtins(self, builtins: "BuiltinsABC"):
        raise NotImplementedError

    @property  # type: ignore
    @abstractmethod
    def os(self) -> "OsABC":
        raise NotImplementedError

    @os.setter  # type: ignore
    @abstractmethod
    def os(self, os: "OsABC"):
        raise NotImplementedError

    @property  # type: ignore
    @abstractmethod
    def shutil(self) -> "ShutilABC":
        raise NotImplementedError

    @shutil.setter  # type: ignore
    @abstractmethod
    def shutil(self, shutil: "ShutilABC"):
        raise NotImplementedError

    @property  # type: ignore
    @abstractmethod
    def subprocess(self) -> "SubprocessABC":
        raise NotImplementedError

    @subprocess.setter  # type: ignore
    @abstractmethod
    def subprocess(self, subprocess: "SubprocessABC"):
        raise NotImplementedError

    @property  # type: ignore
    @abstractmethod
    def pathlib(self) -> "PathlibABC":
        raise NotImplementedError

    @pathlib.setter  # type: ignore
    @abstractmethod
    def pathlib(self, pathlib: "PathlibABC"):
        raise NotImplementedError

    # * Normal methods ########################################################
    @staticmethod
    def _path2str(path: Optional["_SPATH"]) -> str:
        """Converts pathlib.Path, SSHPath or plain str to string.

        Also remove any rtailing backslashes.

        Parameters
        ----------
        path: :const:`ssh_utilities.typeshed._SPATH`
            path to convert to string, if string is passed,
            then just returns it

        Raises
        ------
        FileNotFoundError
            if path is not instance of str, Path or SSHPath
        """
        if isinstance(path, Path):  # (Path, SSHPath)):
            p = fspath(path)
        elif isinstance(path, str):
            p = path
        else:
            raise FileNotFoundError(f"{path} is not a valid path")

        if p.endswith("/") and len(p) > 1:
            return p[:-1]
        else:
            return p

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError

    @staticmethod
    def _to_dict(connection_name: str, host_name: str, address: Optional[str],
                 user_name: str, ssh_key: Optional[Union[Path, str]],
                 thread_safe: bool
                 ) -> Dict[str, Optional[Union[str, bool, int]]]:

        if ssh_key is None:
            key_path = ssh_key
        else:
            key_path = str(Path(ssh_key).resolve())

        return {
            "connection_name": connection_name,
            "server_name": host_name.lower(),
            "user_name": user_name,
            "ssh_key": key_path,
            "address": address,
            "thread_safe": thread_safe
        }

    def _to_str(self, connection_name: str, host_name: str,
                address: Optional[str], user_name: str,
                ssh_key: Optional[Union[Path, str]], thread_safe: bool) -> str:
        """Aims to ease persistance, returns string representation of instance.

        With this method all data needed to initialize class are saved to sting
        and connection can be reinitialized with from_str method of
        `conection.Connection` class.

        Parameters
        ----------
        connection_name : str
            SSHConnection or LocalConnection
        host_name : str
            name of remote server
        address : str
            server address in case of remote connection
        user_name : str
            server login name
        ssh_key : Optional[Union[Path, str]]
            file with public key, pass none for LocalConnection
        thread_safe: bool
            make connection object thread safe so it can be safely accessed
            from  any number of threads, it is disabled by default to avoid
            performance  penalty of threading locks

        Returns
        -------
        str
            string representation of the class

        See Also
        --------
        :class:`ssh_utilities.conncection.Connection`
        """
        return dumps(self._to_dict(connection_name, host_name, address,
                                   user_name, ssh_key, thread_safe))

    def __del__(self):
        self.close(quiet=True)

    def __deepcopy__(self, memodict: dict = {}):
        """On deepcopy create new instance as this is simpler and safer."""
        return connection.Connection.from_dict(self.to_dict(), quiet=True)

    def __getstate__(self):
        """Gets the state of object for pickling."""
        return self.to_dict()

    def __setstate__(self, state: dict):
        """Initializes the object after load from pickle."""
        self.__init__(state["address"], state["user_name"],  # type: ignore
                      pkey_file=state["ssh_key"],
                      server_name=state["server_name"],
                      quiet=True, thread_safe=state["thread_safe"])
