
from ssht.Tunnel import Tunnel
import yaml


class Tunneling(object):
    """
    Class to create all kind of tunnel for Novageo
    """

    __tunnels = []

    def __init__(self):
        """
        Constructor
        """

    def _save_tunnels(self, tunnels):
        with open("config.yml", 'w') as ymlfile:
            for tunnel in tunnels:
                t_attr = {}
                t_attr['remote_host'] = tunnel._get_remote_host()
                t_attr['remote_user'] = tunnel._get_remote_user()
                t_attr['remote_port'] = tunnel._get_remote_port()
                t_attr['remote_key'] = tunnel._get_remote_key()
                t_attr['local_port'] = tunnel._get_local_port()
                t_attr['descr'] = tunnel._get_descr()

                data = dict()
                data[tunnel._get_name()] = t_attr

                yaml.dump(data, ymlfile, default_flow_style=False)

    def _get_list(self):

        tunnels = []

        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        if cfg is not None:
            for section in cfg:
                tunnel = {}
                tunnel['name'] = section
                tunnel['remote_host'] = cfg[section]['remote_host']
                tunnel['remote_user'] = cfg[section]['remote_user']
                tunnel['remote_port'] = cfg[section]['remote_port']
                tunnel['remote_key']  = cfg[section]['remote_key']
                tunnel['local_port'] = cfg[section]['local_port']
                tunnel['descr'] = cfg[section]['descr']

                print(section)
                obj_tunnel = Tunnel(tunnel)
                tunnels.append(obj_tunnel)

        return tunnels

    def _load_tunnels(self):
        self.__tunnels = self._get_list()

    def get_new_tunnel(self):
        tunnel = {}
        tunnel['name'] = "Name"
        tunnel['remote_host'] = "remote_host"
        tunnel['remote_user'] = "remote_user"
        tunnel['remote_port'] = 0
        tunnel['remote_key'] = "remote_key"
        tunnel['local_port'] = 0
        tunnel['descr'] = "description"
        return Tunnel(tunnel)

    def _tunnels_list_is_empty(self):
        return len(self.__tunnels) == 0

    def _n_tunnels(self):
        return len(self.__tunnels)

    def _write_tunnels_list(self):
        line = 1
        for tunnel in self.__tunnels:
            print("%d =>  %s %s" % (line, tunnel._get_name(), tunnel._get_status()))
            line += 1

    def _change_status(self, index):
        print("_change_status")
        if self.__tunnels[index]._is_on():
            print(self.__tunnels[index]._get_status())
            self.__tunnels[index]._close()
        else:
            self.__tunnels[index]._open()

    def _get_names_and_index(self):
        t_list = []
        for tunnel in self.__tunnels:
            t = {}
            t['nome'] = tunnel._get_name()
            t['index'] = self.__tunnels.index(tunnel)
            t['status'] = tunnel._get_status()
            t_list.append(t)
        print(len(t_list))
        return t_list
