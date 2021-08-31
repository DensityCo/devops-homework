# Density DevOps Homework Assignment

## Goal

This repo includes a very simple sample application which we want to gain some data insights from. We want to understand user behavior patterns and look for common failed requests using a combination of data analysis tools.

## Assignment

Your task is to accomplish the following:

- Use the included Kafka and TimescaleDB docker containers to build a basic data pipeline
- The pipeline should have two paths, one to the timescaledb and one to a **public S3 bucket** you'll use as a data lake.
- Push the request / response headers and payload for each request made to app_a and app_b to both systems.

## Data Formats

Your jobs should use the following schemas:

### TimescaleDB

Create a database record for each request with:

* IP Address of the request
* Parameters
* Method
* Response Code

### S3

Push the raw request / response to a bucket with the following path:

`<s3_bucket>/<datestamp-daily>/<timestamp-hourly>/<ip-address>`

## Don't Let the Dog Eat Your Homework

For delivery of this assignment, we'd like to see:

- Working data paths for both pipeline destinations
- Reproducible local workflow (e.g., add your stages to docker compose)

## Bonus Points for Any of the Following

- An architecture diagram of your pipeline setup
- discussion of data lake query tools and patterns you'd use to consume the data
- TimescaleDB continuous aggregations along 5 minute intervals
- Any reflections on how you'd improve this exercise

Create a new repo using your Github account with a unique name and send us the final product!


## Notes

- Please do not fork or submit a PR to this repo
- Please document your thought-processes and use well-written git commit messages to show your progress
- Feel free to change the python application and its requirements in any way you see fit
- We are purposefully not being overly prescriptive in this assignment, as we want you to think creatively about the solution
- This assignment should take less than 5 hours to complete
- If you get stuck or need more information, please reach out for clarity
- Have fun!

## Getting Started in Local Development

Please create and source your virtualenv before beginning. 

Running the apps locally:

```bash
task build
task up
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
