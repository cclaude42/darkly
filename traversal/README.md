# traversal

The `?page=` section of URLs allows us to select the page we want. But is it protected against folder traversal ?

We try a famous exploit :

```
DARKLY_URL/?page=../../../../../../../../../../../../../../../../../../etc/passwd
```

The idea is to return to the root of the host machine with many `../` ; it doesn't need to be exact, as extra `../` will be ignored and we will remain at `/`.

From there, we can access the `/etc/password` file.

We go to the URL. It works ! We get the flag :

```
b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 
```
