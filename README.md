# P2P_Networking
Decentralized/ Peer-to-peer network enabling nodes in a network to establish duplex communication in the form of messages (Chat Application).

## Features
- Establish connections with other nodes using IP and port.
- Send messages to all connected nodes, multiple nodes, or a single node.
- Automatically handle node disconnections.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/P2P_Networking.git
    ```
2. Navigate to the project directory:
    ```sh
    cd P2P_Networking
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the `peer.py` script:
    ```sh
    python peer.py
    ```
2. Follow the prompts to enter your IP, port number, and username.
3. Use the following commands to interact with the network:
    - `stop`: Stops the application.
    - `help`: Prints the help text.
    - `connect`: Establishes connection with a desired node (IP and Port).
    - `message all`: Sends a message to all the nodes you are connected to.
    - `message multiple`: Sends a message to multiple nodes at once.
    - `message one`: Sends a message to one node only.
    - `outbound`: Displays the list of outbound connections.
    - `inbound`: Displays the list of inbound connections.
    - `goddict`: Displays the current state of the god dictionary.

