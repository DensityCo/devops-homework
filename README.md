# Density DevOps Homework Assignment

## Goal

This repo includes a very simple application which we want to dockerize and secure.  Security standards should be taken from the [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/index.html) and should pertain to Docker image security only.

## Assignment

Your task is to accomplish the following:

- Dockerize the two included applications.
- Apply OWASP image hardening best practices to both containers.
- Set up automated local static image scans of the resulting images using a tool like [Snyk](https://snyk.io/).
- Create a basic Kubernetes deployment for both applications.  The deployment should incorporate any OWASP guidance for running containers.
- Ensure that all steps (build, scan, and local kubernetes deployment) can be easily performed using the included [task](https://github.com/go-task/task) file.

## Don't Let the Dog Eat Your Homework

For delivery of this assignment, we'd like to see:

- Dockerfiles for both included applications with OWASP guidelines applied to the image.
- A Task in the Taskfile that automates local static image scans of the resulting images.
- A Kubernetes deployment file that deploys both apps using OWASP runtime guidelines.
- All work orchestrated through the included Taskfile.yaml, documentation [here](https://taskfile.dev/#/)

## Bonus Points for Any of the Following

- Separate build and deploy stages in your Dockerfiles.
- Automated local Kubernetes environment for testing.
- Discuss how you would integrate regular scans into a CI pipeline, along with any caveats.
- Discuss how you would expose and secure this application publicly on Kubernetes.

Create a new repo using your Github account with a unique name and send us the final product!


## Notes

- Please do not fork or submit a PR to this repo.
- Please document your thought-processes and use well-written git commit messages to show your progress.
- Feel free to change the python application and its requirements in any way you see fit.
- We are purposefully not being overly prescriptive in this assignment, as we want you to think creatively about the solution.
- This assignment should take less than 5 hours to complete.
- If you get stuck or need more information, please reach out for clarity.
- Have fun!

## Getting Started in Local Development

Please create and source your virtualenv before beginning. 

Running the apps locally:

```bash
task run-app
```

Making a request

```bash
curl http://127.0.0.1:5000/hello

curl -X POST -H 'Authorization: mytoken' http://127.0.0.1:5000/jobs
```

Simulating a lot of requests

```bash
ab -m POST -H "Authorization: mytoken" -n 500 -c 4 http://127.0.0.1:5000/jobs
```
