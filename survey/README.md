# survey

We go to `/?page=survey`. We see a page with users listed, where we can give them a grade out of 10.

We inspect one of the selectors. We see the following form :

```
<form action="#" method="post">
	<input type="hidden" name="sujet" value="2">
	<select name="valeur" onchange="javascript:this.form.submit();">
		<option value="1">1</option>
		<option value="2">2</option>
            ...
		<option value="2">2</option>
	</select>
</form>
```

On change, the selector immediately submits the form. The values are defined in the HTML.

We can try to exploit this by manually changing one of the values. For example, we can set :

```
<option value="200">2</option>
```

We select option `2`, with the spoofed value.

The form is submitted, the form is exploited, and we get the flag :

```
03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
```