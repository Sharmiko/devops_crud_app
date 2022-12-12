# Devops Application

## Description
This application contains simple crud operations exposed as REST API. 
This application also supports Docker containerization and github actions.
When new changes are pushed to main branch, github ci workflow is triggered and
application is deployed on GCP instance: 35.216.131.20.


## Running with Docker

1) First build the docker image</br>
`docker build -f docker/Dockerfile -t devops_crud_app .`</br>
2) Finally, run the container using `docker-compose`</br>
`docker-compose -f docker/docker-compose.yml up`</br>
   or to detach and run the container in background</br>
   `docker-compose -f docker/docker-compose.yml up -d` 
   

## Sample API endpoint usage WITH Curl

Insert sample order data:

`curl -X POST http://35.216.131.20:8000/orders/
      -H "Content-Type: application/json"
      --data '{
          "name": "apple",
          "quantity": 2,
          "total_price": 5.75,
          "order_datetime": "2022-12-11T20:04:28.511439"
        }'`   


List all orders and format using json_pp:

`curl http://35.216.131.20:8000/orders/ | json_pp -json_opt pretty`

Get specific order using order id:

`curl http://35.216.131.20:8000/orders/item/1 | json_pp -json_opt pretty`

Delete specific order using order id:

`curl -X DELETE http://35.216.131.20:8000/orders/item/1`
