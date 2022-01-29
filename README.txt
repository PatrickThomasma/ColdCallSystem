This system is used for helping an instructor to cold call on their students. It allows an instructor to import a text file that includes the students' information. The system will take the data from the file and display four different names to be "on deck" and the instructor can check off if they have paritipated or flag them to follow up with them. If a student participates or is flagged, that student is removed from the list and another student is added to the list. It saves the list of students when the application is closed and creates a summary list that inclused how many times a student is flagged or has participated. 

Authors: David Han, Kassandra Morando, Patrick Thomasma, Brianna Vago, Geli Zhang

This project was created on Januaray 12th, 2022.

This was created for an assignment at the University of Oregon for Anothony Hornof’s Software Methodologies class.

To run this program, the user needs to go to their terminal by pressing the command key and then the space key then type in terminal and press enter. They need to download tkinter by typing in without the quotation marks  “pip3 --version” then press enter  “pip3 install --upgrade pip” then press enter “pip3 install tk” and then press enter. Navigate to where they download the source code, most likely in the downloads section of their computer. Type in “cd Downloads” and press enter. Type “python3 GUI.py” in the terminal window and press enter. The user should follow the instructions from the prompts to use the system.

Should be run on Macintosh OSX 10.13 (High Sierra) or 10.14 (Mojave)

There is the GUI directory and its subdirectories are backend, config, and records. The GUI directory holds the GUI.py which will run the graphical user interface. 
The subdirectory backend contains object.py and roster.py.The object file will initialize the student and Queue from an input file that has a list of Students and their ID numbers. The roster file uses the information from the object file and gets data from the imported file, randomizes the list of students, and creates the summary file for the end of term.
Another subdirectory of GUI is config, which contains a log of the participants that have been flagged or called on and a config text file that contains the original student information. The last subdirectory, record, contains the summary file that was created in the roster file.

