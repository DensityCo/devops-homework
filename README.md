# Density DevOps Homework Assignment

## Goal
Your goal is to illustrate how you would deploy and scale two applications (App A and App B) to incoming requests. 

## Assignment
Your task is to accomplish the following:

- Deploy the sample python applications to a cluster of nodes using a container orchestration framework
- Application A should be publicly accessible over HTTPS
- Application B should not be accessible via the public internet
- Please show how you would auto-scale the number of nodes and containers as the number of requests increases

## Don't Let the Dog Eat Your Homework

For delivery of this assignment, we'd like to see:

- A Dockerfile for each application
- Framework for deploying containers to a group of nodes
- Document how you will use continuous delivery to ship to a production environment
- Scripts involved with automatically scaling the application and nodes horizontally based on requests

Create a new repo using your Github account with a unique name and send us the final product!


## Notes

- Please do not fork or submit a PR to this repo
- Please document your thought-processes and use well-written git commit messages to show your progress
- Feel free to change the python application and its requirements in any way you see fit
- We are purposefully not being overly prescriptive in this assignment, as we want you to think creatively about the solution
- This assignment should take less than 3 hours to complete
- If you get stuck or need more information, please reach out for clarity
- Have fun!

## Getting Started in Local Development

Please create and source your virtualenv before beginning. 

Running the apps locally:
```
pip install -r requirements.txt
sqlite3 database.db < schema.sql
python app_a.py
python app_b.py
```

Making a request
```
curl -X POST -H 'Authorization: mytoken' http://127.0.0.1:5000/jobs
```

Simulating a lot of requests
```
ab -m POST -H "Authorization: mytoken" -n 500 -c 4 http://127.0.0.1:5000/jobs
```