# Honours-Project-Archive

#Installation Instructions

##Installing SimpleDL
Install SimpleDL - can be found at https://github.com/slumou/simpledl.git
Follow SimpleDL installation instructions

#Setup the New Honours Archive
##Installing HonoursProjectArchive
Download HonoursProjectArchive from GitHub, found at https://github.com/richy1623/Honours-Project-Archive
Replace the SimpleDL/data directory from with the Honours-Project-Archive/data directory
##Setup Gmail Functionality 
###Install the required dependancies
```
sudo apt install cpanminus
cpan App::cpanminus
sudo cpanm Email::Send::SMTP::Gmail
```
###Copy the common.pl script
Copy the common.pl script from the data/website/cgi-bin to the public_html/cgi-bin directory

##Run the following commands command to initilise the digtal library
```
simpledl/bin/import.pl
simpledl/bin/index.pl
simpledl/bin/generate.pl --all
```
##Set up new password
Change the email adress for Admin found in file '''data/users/1.email.xml'''
Reset your password to your own password for the account


#Usage
##Create New Users and Projects
Login as the Admin account
Press the dropdown menu with your Username on it
Select (Admin) Add/Manage Projects
Add a new project with a CSV or manual entry
##Approve or deny projects
Login as the Admin account
Press the dropdown menu with your Username on it
Select (Admin) Moderate Projects
If there are projects pending review they will show up on the webpage and you can approve or deny them
##Upload a Project as a User
Login as the user account
Select Upload/Manage Project in the navigation bar
Follow the on screen help tool
