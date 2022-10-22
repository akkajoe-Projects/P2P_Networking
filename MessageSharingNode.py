from p2pnetwork.node import Node
print('Started!')

class FileSharingNode(Node):

    def __init__(self, host, port, id, god_dict = {}, inbound_n = 0, callback=None, max_connections=0, outbound_connected_node_id = None, inbound_connected_node_id = None, 
    disconnected_id= None):
        super(FileSharingNode, self).__init__(host, port, id, callback, max_connections)
        self.outbound_connected_node_id = outbound_connected_node_id
        self.inbound_connected_node_id = inbound_connected_node_id
        self.disconnected_id = disconnected_id
        self.god_dict = god_dict
        self.inbound_n = inbound_n

    def outbound_node_connected(self, connected_node):
        print("outbound_node_connected: " + connected_node.id)
        self.outbound_connected_node_id = connected_node.id

    def inbound_node_connected(self, connected_node):
        print('INBOUND_N', self.inbound_n)
        print('INBOUND_LIST', self.nodes_inbound)
        print("inbound_node_connected: " + connected_node.id)
        self.inbound_connected_node_id = connected_node.id
        self.god_dict[connected_node.id] = self.nodes_inbound[len(self.nodes_inbound) - 1]
        print(self.god_dict)
        self.inbound_n+=1
        print('INBOUND_N', self.inbound_n)

    def node_disconnected(self, connected_node):
        """While the same nodeconnection class is used, the class itself is not able to
           determine if it is a inbound or outbound connection. This function is making
           sure the correct method is used."""
        self.debug_print("node_disconnected: " + connected_node.id)

        if connected_node in self.nodes_inbound:
            del self.nodes_inbound[self.nodes_inbound.index(connected_node)]
            self.inbound_node_disconnected(connected_node)

        if connected_node in self.nodes_outbound:
            del self.nodes_outbound[self.nodes_outbound.index(connected_node)]
            self.outbound_node_disconnected(connected_node)

    def inbound_node_disconnected(self, connected_node):
        """This method is invoked when a node, that was previously connected with us, is in a disconnected
           state."""
        print("inbound_node_disconnected: " + connected_node.id)
        self.debug_print("inbound_node_disconnected: " + connected_node.id)
        self.disconnected_id = connected_node.id
        print('SELF.DISCONNECTED_ID', self.disconnected_id)
        if self.callback is not None:
            self.callback("inbound_node_disconnected", self, connected_node, {})

    def outbound_node_disconnected(self, connected_node):
        """This method is invoked when a node, that we have connected to, is in a disconnected state."""
        self.debug_print("outbound_node_disconnected: " + connected_node.id)
        print("outbound_node_disconnected: " + connected_node.id)
        self.disconnected_id = connected_node.id
        print('SELF.DISCONNECTED_ID', self.disconnected_id)
        if self.callback is not None:
            self.callback("outbound_node_disconnected", self, connected_node, {})

    def node_message(self, connected_node, data):
        print("node_message from " + connected_node.id + ": " + str(data))
        if str(data) == 'DISCONNECTING...':
            self.disconnected_id = connected_node.id

    def node_disconnect_with_outbound_node(self, connected_node):
        """This method is invoked just before the connection is closed with the outbound node. From the node
           this request is created."""
        print("node wants to disconnect with other outbound node: " + connected_node.id)
        self.debug_print("node wants to disconnect with oher outbound node: " + connected_node.id)
        if self.callback is not None:
            self.callback("node_disconnect_with_outbound_node", self, connected_node, {})

    def node_request_to_stop(self):
        """This method is invoked just before we will stop. A request has been given to stop the node and close
           all the node connections. It could be used to say goodbey to everyone."""
        print("node is requested to stop!")
        self.send_to_nodes('DISCONNECTING...')
        self.debug_print("node is requested to stop!")
        if self.callback is not None:
            self.callback("node_request_to_stop", self, {}, {})

    def inbound_nodes(self):
        return self.nodes_inbound

    def outbound_nodes(self):
        return self.nodes_outbound




