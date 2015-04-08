# This Fabfile will do the followin:
#    - update the remote system(s)
#    - download and install an application

# Import Fabric's API module
from fabric.api import *
import time


# host_names = open('/home/clgreen/fab/systems', 'rb')
# access_list = host_names.read()

# print access_list # print has been moved after the assignment

# host_names.close()

#  env.hosts = access_list
#[
#    'systems_file',
  # 'ip.add.rr.ess
  # 'server2.domain.tld',
#]
# Set the username

env.user   = "greenc"
env.hosts = "localhost"

# Set the password [NOT RECOMMENDED]
# env.password = "passwd"


# import time
def mem():
    run('free')
# def remote_status():
def remote_status():
    with open("systems", "r") as hosts:
        for line in hosts:
            print line,
#            env.hosts = "line"
#            line2 = env.hosts
#           print line2,
            mem()
            time.sleep(10)
#            lines.remove(lines[0])
#        time.sleep(60)

#        file.truncate(0) #this truncates the file to 0 bytes
#    except IOError:
#        print 'No such file in directory'

# def service_status():
#    """
#        Update the default OS installation's
#        basic default tools.
#                                            """
#    sudo("service dhcpd status")

# def used_memory():
#    """ Download and install memcached. """
#    run("free")


#    access_list = host_names.read()
#    for host in  host_names.readlines():
#        print(host)
#       env.hosts = host
#        test = env.hosts
#        used_memory()
#        print(test)
# Update
# execute(service_status, hosts=systems_file)
#    service_status()
# Install
# execute(used_memory, hosts=systems_file)
#    used_memory()

