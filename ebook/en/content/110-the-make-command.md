# The `make` command

The `make` command is used to automate the reuse of multiple commands in certain directory structure.

An example for that would be the use of `terraform init`, `terraform plan`, and `terraform validate` while having to change different subscriptions in Azure. This is usually done in the following steps:

```
az account set --subscription "Subscription - Name"
terraform init
```

How the `make` command can help us is it can automate all of that in just one go:
```make tf-init```

### Syntax:

```
make [ -f makefile ] [ options ] ... [ targets ] ...
```

### Example use (guide):

#### 1. Create `Makefile` in your guide directory
#### 2. Include the following in your `Makefile` :
```
hello-world:
        echo "Hello, World!"

hello-bobby:
        echo "Hello, Bobby!"

touch-letter:
        echo "This is a text that is being inputted into our letter!" > letter.txt

clean-letter:
        rm letter.txt
```
#### 3. Execute ```make hello-world``` - this echoes "Hello, World" in our terminal.
#### 4. Execute ```make hello-bobby``` - this echoes "Hello, Bobby!" in our terminal.
#### 5. Execute ```make touch-letter``` - This creates a text file named `letter.txt` and populates a line in it.
#### 6. Execute ```make clean-letter```



### References to lenghtier and more contentful tutorials:

(linoxide - linux make command examples)[https://linoxide.com/linux-make-command-examples/]
(makefiletutorial.com - the name itself gives it out)[https://makefiletutorial.com/]