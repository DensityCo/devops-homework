# Density DevOps Homework Assignment

## Goal

Your goal is to show how you would build, and deploy the included applications
using Kubernetes and cloud-native tooling.

## Assignment

Your task is to accomplish the following:

- Build a small Kubernetes test cluster either locally or in the cloud. A single
  node is fine. Feel free to use Terraform with a cloud provider or an
  all-in-one tool for a local cluster
- Build Docker files for both sample applications (applications must return
  correct results)
- Build a deployment mechanism for these apps
- Describe a plan for continuous delivery with the specific tools/vendors you'd
  look at and your evaluation criteria for them

## Deliverables

We'd like to see a repo with the following:

- A Dockerfile for each application
- Repeatable deployment mechanism for each application
- A README with the set-up process so we can run it ourselves
- A text file with a brief write-up about brief the following:
  - Continuous Delivery plan for the app ecosystem
  - Discussion of tools chosen, and how you would 
- Well-written git commit messages to show your progress. (Hint: we can't tell
  if  you rebase! :wink: )
  
## Bonus Points for Any of the Following

- Separate build and deploy stages in your Dockerfiles
- Automated local or cloud-based Kubernetes environment for testing

Create a new repo using your Github account with a unique name and send us the
final product! If you'd prefer to make the repo private, that's fine too! When
you're ready, you can add us as collaborators.


## Notes

- Please do not fork or submit a PR to this repo
- Feel free to change the python application code and/or their requirements to
  make them more "cloud native"
- If you get stuck or need more information, please reach out for clarity
- Have fun!

## Getting Started in Local Development

Running the apps outside of a container:

```
pip install -r requirements.txt
sqlite3 database.db < schema.sql
python app_a.py
python app_b.py
```

Making a request

```bash
# Test a non-auth'd route
curl http://127.0.0.1:5000/hello

curl -X POST -H 'Authorization: mytoken' http://127.0.0.1:5000/jobs
```
