# Quiz project
Simple quiz project that contains fronted SPA application written on React and 
RestAPI written on Python (Django/DRF)

## Installation
Before you start, make sure that you have [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/) installed on your machine  
`make dev`  
It will run two development servers frontend at [http://127.0.0.1:3000](http://127.0.0.1:3000) and backend at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Tests
If you want to run backend tests use `make tests`  
It will run unit tests and also check PEP8 and tests coverage

## Clean up
if you want to clean up after yourself use
`make clean`