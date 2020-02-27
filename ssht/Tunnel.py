
from sshtunnel import SSHTunnelForwarder


class Tunnel(object):
    """
    @author marcopaulomartins@hotmail.com
    @date 26-02-2020
    """
    __ssh = 22

    __name = None
    __descr = None

    __remote_user = None
    __remote_host = None
    __remote_port = None
    __remote_pass = None
    __remote_key = None

    __local_host = None
    __local_port = None

    __is_on = False

    __tunnel = None

    def __init__(self, params=None):
        """
        Constructor
        """
        if params is not None:
            self._set_tunnel(params)

    def __del__(self):
        if self.__is_on:
            self._close()

    def __params_are_valid(self, params):
        if not isinstance(params, dict):
            print("0")
            return False
        keylist = ('name', 'descr', 'remote_host',
                   'remote_user', 'remote_port',
                   'remote_key', 'local_port')
        if not all(key in params for key in keylist):
            return False
        if sum([1 for x in params if params[x] is None]) > 1:
            return False
        return True

    def __load(self, params):
        self.__name = params['name']
        self.__descr = params['descr']
        self.__remote_host = params['remote_host']
        self.__remote_user = params['remote_user']
        self.__remote_port = params['remote_port']
        self.__remote_key = params['remote_key']
        self.__local_port = params['local_port']
        # by default
        self.__local_host = "localhost"

    # PUBLIC methods    #
    def _set_tunnel(self, params):
        if self.__is_on:
            raise NameError('TunnelIsOn')
        if not self.__params_are_valid(params):
            raise NameError('InvalidParameters')

        self.__load(params)

        self.__tunnel = SSHTunnelForwarder(
            (self.__remote_host, self.__ssh),
            ssh_username=self.__remote_user,
            ssh_private_key=self.__remote_key,
            remote_bind_address=(self.__local_host, self.__remote_port),
            local_bind_address=(self.__local_host, self.__local_port)
        )

    def _open(self):
        print("start tunnel")
        self.__tunnel.start()
        self.__is_on = True

    def _close(self):
        print("stop tunnel")
        self.__tunnel.close()
        self.__is_on = False

    def _is_on(self):
        return self.__is_on

    def _get_name(self):
        return self.__name

    def _get_status(self):
        if self._is_on():
            return "ON"
        return 'OFF'

    def _get_descr(self):
        return self.__descr

    def _get_remote_user(self):
        return self.__remote_user

    def _get_remote_host(self):
        return self.__remote_host

    def _get_remote_port(self):
        return self.__remote_port

    def _get_remote_pass(self):
        return self.__remote_pass

    def _get_remote_key(self):
        return self.__remote_key

    def _get_local_host(self):
        return self.__local_host

    def _get_local_port(self):
        return self.__local_port
