from FileSharingNode import FileSharingNode
import shortuuid

uid = shortuuid.ShortUUID().random(length=3)

host_ip = str(input("Enter your ip"))
port = int(input('Enter your port number '))
username = input('Please enter your username ')
id = username + '(' + uid + ')'
god_dict = {}
inbound_n = 1
node = FileSharingNode(host_ip, port, id, god_dict, inbound_n)
node.start()
print('node functional')
outbound_n = 1

def connect_to_node(usernames):
    global outbound_n
    host = input('IP of node? ')
    client_port = int(input('port? '))
    node.connect_with_node(host, client_port)
    outbound_lis = node.nodes_outbound
    god_dict[node.outbound_connected_node_id] = outbound_lis[len(node.nodes_outbound) - 1]
    outbound_n+=1

def disconnected_nodes():
    global outbound_n
    global inbound_n
    if node.disconnected_id != None:
        if god_dict[node.disconnected_id] in node.nodes_inbound:
            node.nodes_inbound.remove(god_dict[node.disconnected_id])
            inbound_n-=1
        if god_dict[node.disconnected_id] in node.nodes_outbound: 
            node.nodes_outbound.remove(god_dict[node.disconnected_id])
            outbound_n-=1
        del god_dict[node.disconnected_id]  
        print('god_dict after deletion: ', god_dict)
        node.disconnected_id = None

def print_help():
    print('''Command options: 
             (stop - Stops the application.
              help - Prints this help text.
              connect - Establishes connection with desired node (IP and Port).
              message all - sends a message to all the nodes you are connected to.
              message multiple - sends a message to multiple nodes at once.
              message one - sends a message to one node only.)''')

def flow(commands):
    try:
        while commands != "stop":
            disconnected_nodes()
            if commands == "help":
                print_help()
            if commands == "connect":
                connect_to_node(username)
            if commands == "message all":
                message = input('Enter a message: ')
                node.send_to_nodes(str(message))
            if commands == "message multiple":
                print(god_dict)
                excluded_n = input('Which nodes would you like to send the message to? ')
                message = input('Enter a message: ')
                desired_n_list = excluded_n.split(',')
                for i in desired_n_list:
                    node.send_to_node(god_dict[i], str(message))
            if commands == 'outbound':
                print(node.nodes_outbound)
                for i in node.nodes_outbound:
                    print(type(i))
            if commands == 'inbound':
                print(node.nodes_inbound)
                for i in node.nodes_inbound:
                    print(type(i))
            if commands == 'goddict':
                print(god_dict)
            if commands == 'message one':
                print(god_dict)
                receiver = input('Which node would you like to send a message to ')
                print(type(receiver))
                message = input('Enter a message: ')
                node.send_to_node(god_dict[receiver], str(message))
            print_help()
            commands = input("? ")

    except Exception as ex:
        while commands != "stop":
            print('ex', ex)
            command = input("? ")
            flow(command)
            break
        else:
            node.stop()

print_help()
command = input("? ")
flow(command)
node.stop()