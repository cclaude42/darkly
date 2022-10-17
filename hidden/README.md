# hidden

We go to `/robots.txt` to see if anything is referenced. We get the following :

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

We go to `/.hidden` to see if we can exploit anything. We see the following page :

```
Index of /.hidden/

../
amcbevgondgcrloowluziypjdh/                        29-Jun-2021 18:15                   -
bnqupesbgvhbcwqhcuynjolwkm/                        29-Jun-2021 18:15                   -
ceicqljdddshxvnvdqzzjgddht/                        29-Jun-2021 18:15                   -
doxelitrqvhegnhlhrkdgfizgj/                        29-Jun-2021 18:15                   -
eipmnwhetmpbhiuesykfhxmyhr/                        29-Jun-2021 18:15                   -
ffpbexkomzbigheuwhbhbfzzrg/                        29-Jun-2021 18:15                   -
ghouhyooppsmaizbmjhtncsvfz/                        29-Jun-2021 18:15                   -
hwlayeghtcotqdigxuigvjufqn/                        29-Jun-2021 18:15                   -
isufpcgmngmrotmrjfjonpmkxu/                        29-Jun-2021 18:15                   -
jfiombdhvlwxrkmawgoruhbarp/                        29-Jun-2021 18:15                   -
kpibbgxjqnvrrcpczovjbvijmz/                        29-Jun-2021 18:15                   -
ldtafmsxvvydthtgflzhadiozs/                        29-Jun-2021 18:15                   -
mrucagbgcenowkjrlmmugvztuh/                        29-Jun-2021 18:15                   -
ntyrhxjbtndcpjevzurlekwsxt/                        29-Jun-2021 18:15                   -
oasstobmotwnezhscjjopenjxy/                        29-Jun-2021 18:15                   -
ppjxigqiakcrmqfhotnncfqnqg/                        29-Jun-2021 18:15                   -
qcwtnvtdfslnkvqvzhjsmsghfw/                        29-Jun-2021 18:15                   -
rlnoyduccpqxkvcfiqpdikfpvx/                        29-Jun-2021 18:15                   -
sdnfntbyirzllbpctnnoruyjjc/                        29-Jun-2021 18:15                   -
trwjgrgmfnzarxiiwvwalyvanm/                        29-Jun-2021 18:15                   -
urhkbrmupxbgdnntopklxskvom/                        29-Jun-2021 18:15                   -
viphietzoechsxwqacvpsodhaq/                        29-Jun-2021 18:15                   -
whtccjokayshttvxycsvykxcfm/                        29-Jun-2021 18:15                   -
xuwrcwjjrmndczfcrmwmhvkjnh/                        29-Jun-2021 18:15                   -
yjxemfsgdlkbvvtjiylhdoaqkn/                        29-Jun-2021 18:15                   -
zzfzjvjsupgzinctxeqtzzdzll/                        29-Jun-2021 18:15                   -
README                                             29-Jun-2021 18:15                  34
```

We find a proper directory hell, with hundreds of scattered READMEs. A quick inspection reveals :

- There are 26 top-level directories
- They each contain 26 second-level directories
- Which each contain 26 lowest-level directories
- In those lowest-level directories, there's only a README
- We have 26³ (17576) READMEs to check
- There's only a few unique READMEs ; most are copies of each other

The task can't be done by hand ; we decide to write a simple crawler / scrapper in Python.

The script (`crawler.py`) follows these simple steps :

- Start at the root (`DARKLY_URL/.hidden/`)
- Get all linked URLs and read them
- For each URL, repeat the process to go deeper
- When you're at depth 3, (example : `DARKLY_URL/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/ayuprpftypqspruffmkuucjccv/`), read the README
- If you find a README you've never seen before, display its contents and save it to an "already seen" list

We run the script. Quickly, the "garbage" is displayed, and the script isn't finding any unique READMEs...

```
Demande Ã  ton voisin de gauche  

Non ce n'est toujours pas bon ...

Demande Ã  ton voisin du dessous 

Demande Ã  ton voisin du dessus  

Toujours pas tu vas craquer non ?

Demande Ã  ton voisin de droite  

Tu veux de l'aide ? Moi aussi !  

1/26...
2/26...
3/26...
...
```

Until the 22nd directory, where it finds a README with the flag :

```
d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
```