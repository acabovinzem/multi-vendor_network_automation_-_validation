from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def get_version(task):
    result = task.run(task = netmiko_send_command, command_string= "show version")
    return result

result = nr.run(task=get_version)
print_result(result)
