# borntosec

At the very bottom of the page, a `BornToSec` copyright text takes us to a page with a strange URL : `/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`

We inspect to see comments and hidden elements. Two of them stand out :

```
<!--You must come from : "https://www.nsa.gov/".-->
```
```
<!--Let's use this browser : "ft_bornToSec". It will help you a lot.-->
```

These give pretty clear instructions :

- We must come from the NSA website (meaning we must set it as the `Referer` in the `GET` request)
- And we must use the - fictional - `ft_bornToSec` browser (meaning we have to set it as `User-Agent`)

We can do this with a simple `curl` request on the desired URL :

```
curl --user-agent "ft_bornToSec" --referer "https://www.nsa.gov/" http://DARKLY_URL/index.php\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

We inspect the page `curl` returns and we find the flag :

```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```
