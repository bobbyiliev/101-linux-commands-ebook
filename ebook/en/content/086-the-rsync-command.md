# The `rsync` command

The `rsync` command is probably one of the most used commands out there. It is used to securely copy files from one server to another over SSH.

Compared to the `scp` command, which does a similar thing, `rsync` makes the transfer a lot faster, and in case of an interruption, you could restore/resume the transfer process.

In this tutorial, I will show you how to use the `rsync` command and copy files from one server to another and also share a few useful tips!

Before you get started, you would need to have 2 Linux servers. I will be using DigitalOcean for the demo and deploy 2 Ubuntu servers.

You can use my referral link to get a free $100 credit that you could use to deploy your virtual machines and test the guide yourself on a few DigitalOcean servers:

**[DigitalOcean $100 Free Credit](https://m.do.co/c/2a9bba940f39)**

## Transfer Files from local server to remote

This is one of the most common causes. Essentially this is how you would copy the files from the server that you are currently on (the source server) to remote/destination server.

What you need to do is SSH to the server that is holding your files, cd to the directory that you would like to transfer over:

```
cd /var/www/html
```

And then run:

```
rsync -avz user@your-remote-server.com:/home/user/dir/
```

The above command would copy all the files and directories from the current folder on your server to your remote server.

Rundown of the command:

* `-a`: is used to specify that you want recursion and want to preserve the file permissions and etc.
* `-v`: is verbose mode, it increases the amount of information you are given during the transfer.
* `-z`:  this option, rsync compresses the file data as it is sent to the destination machine, which reduces the amount of data being transmitted -- something that is useful over a slow connection.

I recommend having a look at the following website which explains the commands and the arguments very nicely:

[https://explainshell.com/explain?cmd=rsync+-avz](https://explainshell.com/explain?cmd=rsync+-avz)

In case that the SSH service on the remote server is not running on the standard `22` port, you could use `rsync` with a special SSH port:

```
rsync -avz -e 'ssh -p 1234' user@your-remote-server.com:/home/user/dir/
```

## Transfer Files remote server to local

In some cases you might want to transfer files from your remote server to your local server, in this case, you would need to use the following syntax:

```
rsync -avz your-user@your-remote-server.com:/home/user/dir/ /home/user/local-dir/
```

Again, in case that you have a non-standard SSH port, you can use the following command:

```
rsync -avz -e 'ssh -p 2510' your-user@your-remote-server.com:/home/user/dir/ /home/user/local-dir/
```

## Transfer only missing files

If you would like to transfer only the missing files you could use the `--ignore-existing` flag. 

This is very useful for final sync in order to ensure that there are no missing files after a website or a server migration.

Basically the commands would be the same apart from the appended --ignore-existing flag:

```
 rsync -avz --ignore-existing  user@your-remote-server.com:/home/user/dir/
```

## Conclusion

Using `rsync` is a great way to quickly transfer some files from one machine over to another in a secure way over SSH.

For more cool Linux networking tools, I would recommend checking out this tutorial here:

[Top 15 Linux Networking tools that you should know!](https://devdojo.com/serverenthusiast/top-15-linux-networking-tools-that-you-should-know)

Hope that this helps!

Initially posted here: [How to Transfer Files from One Linux Server to Another Using rsync](https://devdojo.com/bobbyiliev/how-to-transfer-files-from-one-linux-server-to-another-using-rsync)
