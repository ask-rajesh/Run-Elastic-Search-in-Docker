# Run-Elastic-Search-and-Kibana-in-Docker
Run elastic search and kibana in Docker and also access it through Python. Read and write data from elastic search using Python.

* ### Download ```yml``` file from this repositories
  download ```docker-compose.yml``` 

* ### Run below command
  ```docker-compose up```, this command will start the container for Elastic Search and Kibana using ```docker-compose.yml```.

Great, Elastic Search and Kibana is now running.

* ### Check Elastic Search and Kibana is running ot not.
  ```docker ps```, this command will list down the current running containers.

* ### Access Kibana
  Kibana can be access from ```http://localhost:5601/```

* ### Access Elastic Search

  Elastic Search can be access through ```curl``` command using ```http://localhost:9200/```

* ### Access Elastic Search using Python
  Install ```elasticsearch```

  ```pip install elasticsearch```

  Python script is present in this repository.


## If you liked this repository

* Dont't forget to give this repository a 🌟
