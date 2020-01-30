**0x01 Permissions, users, and ownership**

0. Script changed UID to betty. Password still required to finalize change
1. Prints current user to terminal
2. Prints all groups current user is part of
3. Changes owner of file "hello" to betty
4. Creates empty file "hello"
5. Grants execute perms for hello file to user
6. Grants execute perms for file hello to owner and group owner, grants read permissions to all other users
7. Adds execution permissions for file hello to all users
8. Grants exact permissions 007 to file hello
9. Grants exact permissions 753 to file hello
10. Copies permissions of file olleh onto hello
11. Grants execute permissions to all subdirectories in the current directory for all users
12. Creates a directory in the working directory with permissions 751
13. Changes group owner for file hello to holberton
14. changes owner to betty and group owner to holberton for all files in the working directory
15. Changes the owner and group owner of symbolic link _hello to betty and holberton, respectively
16. Changes owner of file hello to betty if and only if the file owner is currently guillaume
100. Plays star wars episode IV in terminal
101. Creates a man page exactly identical to an example man page