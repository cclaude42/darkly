# hidden

We go to `/?page=signin`. We're prompted to enter a username and a password.

We decide to bruteforce our way in. We write a simple script in Python.

The script (`brute.py`) follows these simple steps :

- Initialize with the provided `URL` and `username`
- Send a POST request with an incorrect password and save the `WrongAnswer` page
- Read the `wordlist.txt` file
- For each password, send a POST request and compare results
- When something's different, display and quit

We fill the `wordlist.txt` file with the 100 most common passwords ([found online](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt)), set username as `admin` and run the script.

After a while the script and prints :

```
Done ! Password is [shadow]
```

We go to `?page=signin` manually and log in with `admin:shadow`. It works and we get the flag :

```
b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2 
```