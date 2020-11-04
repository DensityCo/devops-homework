# Density DevOps Homework Assignment

## Goal

Your goal is to show how you would build, test, scale, and deploy the included application on [Hashicorp Nomad](https://www.nomadproject.io/).


## Assignment

Your task is to accomplish the following:

- Build a small Nomad test cluster either locally or or in the cloud, single node is fine.
- Build Docker files for both sample applications (applications must return correct results).
- Build a deployment mechanism for Nomad's [docker driver](https://www.nomadproject.io/docs/drivers/docker), this should include basic .hcl files for both applications.
- Create a plan for continuous delivery for Nomad, discuss the specific tools you'd look at and your evaluation criteria for them.
- Discuss options for Nomad auto-scaling using the [Nomad Autoscaler](https://www.nomadproject.io/docs/autoscaling), [Levant](https://github.com/hashicorp/levant), or tooling of your choice.


## Don't Let the Dog Eat Your Homework

For delivery of this assignment, we'd like to see:

- A Dockerfile for each application
- Simple implementation of Nomad (locally or in a public cloud)
- Repeatable deployment mechanism for each application
- Continuous Delivery plan for the Nomad ecosystem
- Auto-scaling plan for the Nomad ecosystem
- Brief discussion of Nomad as a container platform - note strengths and weaknesses vs more common options (e.g. Kubernetes)

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
