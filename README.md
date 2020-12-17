# Data Engineering Project 2

## Build and run the container

Building the docker file:
```
docker build -t data-eng-proj2 .	
```

To run the service, run the following command:  
```
docker run -p 5000:5000 data-eng-proj2
```

This will run website on port 5000

Go to [http://localhost:5000](http://localhost:5000) and start playing with the application!

## Tests
Run the unit tests:
```
python unit.py
```

Run the integration tests:
```
python test.py
```

Run the stress tests:
```
python stress_test.py
```
## Link to Trello
[https://trello.com/b/GBY14s2p/engineeringproject](https://trello.com/b/GBY14s2p/engineeringproject)

