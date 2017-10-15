peer2server_msg_types = ("Register", "Leave", "PQuery", "KeepAlive")


# Peer2Server is used create messages during client and server communication
class Peer2Server:
    count = 0

    def __init__(self, command, ip=None, data=None, version='P2P-DI/1.0'):
        if ip and data:
            if command not in peer2server_msg_types:
                raise "Command %s not in allowed message types" % command
            self.command = command
            self.ip = ip
            if isinstance(data, dict):
                self.data = data
            else:
                self.data = eval(data)
            self.version = version
            Peer2Server.count += 1

        elif not (data and ip):
            fields = command.split("\n")
            try:
                self.command = fields[0]
                self.ip = fields[1]
                self.version = fields[2]
                self.data = eval(fields[3])
            except IndexError:
                raise Exception("Peer2Server could not decode the message %s" % command)
        else:
            raise Exception("Illegal instantiation of Peer2Server. Check parameters.")

    def formatted(self):
        return "%s\n%s\n%s\n%s\n" % (self.command, self.ip, self.version, self.data)



