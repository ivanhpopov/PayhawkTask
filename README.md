# PayhawkTask
Repo for the task I received

The programming task was built in four stages:

- First, I created the GUI for the simple App. (gui.py - this is the main file)

- Second, I created the API call to VirusTotal and JS response parser. (API.py)

- Third, I created the logic for the filtering of IPs from a file (this was not perfectly implemented - RegexMatch.py)

- Fourth, I connected the files by importing the needed functions.

NOTE: I have purposefully removed my API key after pushing the project to github.

Screenshots of the application can be found in the "App Screenshots" folder.

Button functions:

Open file - Browses for files, extracts the IPs with Regex and fills the larger text field.

Single - checks VirusTotal Api with the provided IP in single IP field

Bulk - check VirusTotal API with the list of IPs from the larger text field.

all of the tests against the API pars JSON and provide the reputation of the IP.
