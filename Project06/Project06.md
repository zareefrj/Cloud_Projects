## Project06: Simple Chat App with UDP Sockets on EC2

This project involved building a basic chat application using UDP sockets on separate EC2 instances acting as server and client.

**Objective:**

* Explore the principles of UDP communication and socket programming.
* Implement a functional chat application based on UDP for message exchange.
* Utilize EC2 instances to simulate and test the distributed nature of the application.

**Implementation:**

* This project focused on writing separate code for the server and client sides using programming languages (Java).
* Both sides utilized UDP sockets for communication, handling message sending and receiving.
* Specific commands and code structure are included within this project folder.

**Key Steps:**

* **Server Code:**
    * Created a UDP socket and bound it to a specific port.
    * Implemented logic to listen for incoming messages from the client.
    * Upon receiving a message, processed and displayed it on the server side.
    * Sent response messages back to the client through the socket.

* **Client Code:**
    * Established a UDP socket and connected to the server's IP and port.
    * Composed chat messages and sent them to the server through the socket.
    * Received response messages from the server and displayed them on the client side.

* **Building and Running:**
    * Compiled the server and client code independently on respective EC2 instances.
    * Launched both programs simultaneously, establishing the chat channel.
