# AirBnB clone - The console
### The goal of the project is to deploy on your server a simple copy of the AirBnB website
### The first step towards building this web application involves:
1. Creating a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
2. Creating all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
3. Creating the first abstracted storage engine of the project: File storage.

## Command Interpreter
### The command interpreter will be used to:
1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object

### How to start command interpreter
```
./console
```
### or
```
echo "help" | ./console.py
```

### How to use command interpreter
### 1. To list all commands
```
help
```
### 2. To create an instance
```
create <class name>
```
### 3. To print string representation of instance
```
show <class name> <class id>
```
### 4. To delete an instance
```
destroy <class name> <class id>
```
### 5. To print string representation of all instances
```
all
```
### 6. To print string representation of instances of particular class
```
all <class name>
```
### 7. To update an instance
```
update <class name> <class id> <attribute name> <attribute value>
```
### 8. To quit the command interpreter

```
quit
```
### or
```
ctr + D
```

### Examples
![starting](https://github.com/sakachris/AirBnB_clone/assets/125475525/1d2547bb-99ab-4684-b289-a8576c7bbe06)
![starting2](https://github.com/sakachris/AirBnB_clone/assets/125475525/dd961778-f6a1-45b0-84de-c9d6dc93eff6)
![create](https://github.com/sakachris/AirBnB_clone/assets/125475525/1ca15798-616a-4940-81c1-110db566e381)
![show](https://github.com/sakachris/AirBnB_clone/assets/125475525/53807fe0-8830-4490-91b5-0d4e199122cc)
![all](https://github.com/sakachris/AirBnB_clone/assets/125475525/66154486-d7c8-4812-82d4-7a6533f20160)
![all User](https://github.com/sakachris/AirBnB_clone/assets/125475525/a866ca9c-5012-4d5c-895e-8ed499f56643)
![update](https://github.com/sakachris/AirBnB_clone/assets/125475525/3b58c421-0f03-4de8-b2ad-8d4c1a9032ba)
![destroy](https://github.com/sakachris/AirBnB_clone/assets/125475525/b91ecb2e-19bd-4634-b842-956dbf667cd8)
![quit](https://github.com/sakachris/AirBnB_clone/assets/125475525/cbb51830-5dea-4895-9497-5f93555c8ef7)
