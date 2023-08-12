# AirBnB clone - The console
### The goal of the project is to deploy on your server a simple copy of the AirBnB website
### The first step towards building this web application involves:
1. Creating a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
2. Creating all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
3. Creating the first abstracted storage engine of the project: File storage.

## Command Interpreter
### The command interpreter wull be used to:
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

