# recover

We go to `?page=recover`. We see a submit button, but no input field.

Clicking `Submit` does something. We inspect the page to see what. We see a POST form, with this hidden input field :

```
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

We manually change the value to `admin@borntosec.com` and click Submit.

It works ! We get the flag :

```
1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
```
