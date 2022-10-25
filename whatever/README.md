# whatever

We go to `/robots.txt` to see if anything is referenced. We get the following :

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

We go to `/whatever` to see if we can exploit anything. We see the following page :

```
Index of /whatever/

../
htpasswd                                           29-Jun-2021 18:09                  38
```

`htpsswd` is used to password-protect folders - typically, an admin page.

We go to `DARKLY_URL/admin`. We find a page ! It prompts us for a username and password.

We download the `htpasswd` file. It contains credentials :

```
root:437394baff5aa33daa618be47b75cb49
```

The password's hashed, it's an MD5. We decrypt it over at [MD5decrypt](https://md5decrypt.net/). We get the password in clear :

```
qwerty123@
```

Finally, we log in with `root` and `qwerty123@` on the `/admin` page and we find the flag :

```
d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
```