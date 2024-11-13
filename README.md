Quickshare
Quickshare is a Python-based application for transferring files over a local network. It uses Tkinter for the GUI, SQLite for tracking transferred files, and sockets for network communication, enabling users to send and receive files with ease.

Features
•	File Transfer Over Local Network: Transfer files to other devices on the same network.
•	GUI with Tkinter: User-friendly interface for selecting, sending, and receiving files.
•	SQLite Database Integration: Records file names of sent and received files.
•	TCP Socket Communication: Ensures reliable file transfer between devices.


Requirements
•	Python 3.x
•	Required libraries: Tkinter, SQLite3, and socket (included with Python)
•	Images for GUI icons and backgrounds (located in the specified paths)
Project Structure
•	Main Application: Provides a GUI with buttons to either "Send" or "Receive" files.
•	Send Module: Allows users to select a file and send it to another device.
•	Receive Module: Accepts files sent from another device.


Installation
1.	Clone this repository:
bash
Copy code
git clone https://github.com/grishma7733/Quickshare.git
2.	Ensure all images for icons and backgrounds are in the correct file paths as referenced in the code.
3.	Run the program:
bash
Copy code
python quickshare.py

Usage
1.	Open the Application: Run the quickshare.py script to open the Quickshare GUI.
2.	Sending a File:
o	Click the Send button.
o	In the new window, select the file you want to send.
o	Click Send to initiate the file transfer.
o	The selected file name will be stored in the database.
3.	Receiving a File:
o	Click the Receive button.
o	Enter the sender’s ID (hostname).
o	Enter a filename for the received file.
o	Click Receive to connect and save the incoming file.
o	The received file name will also be recorded in the database.

Explanation of Socket Communication
Quickshare uses TCP sockets for reliable, ordered, and error-checked data transfer.
•	Server (Sender): Binds to a specific IP and port, waits for connections, and sends the file data in chunks.
•	Client (Receiver): Connects to the sender's IP and port, receives the file data, and writes it to a local file.

Database
The application uses SQLite to store file names in a users2 table within filename.db. This helps maintain a record of all transferred files.
Troubleshooting
•	Connection Issues: Ensure that both devices are on the same local network.
•	File Paths for Images: Update the file paths for icons and background images if they are stored in different locations.
•	Firewall: Make sure the firewall settings allow the application to use the specified port (default: 8080).

