# cookie

In the `Storage` section of the Browser Developer Tools, we can check cache and other things.

We inspect the storage. We find a cookie with the following specs :

```
Name: I_am_admin
Value: 68934a3e9455fa72420237eb05902327
```

This is an MD5 hash. We decrypt it over at [MD5decrypt](https://md5decrypt.net/) and get :

```
false
```

We encode the word `true` into an MD5 hash, which yields us `b326b5062b2f0e69046810717534cb09`

We can now replace the value of the cookie, with a double click (directly from Developer Tools).

We reload the page, and we get an `alert()` with the flag :

```
df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```
