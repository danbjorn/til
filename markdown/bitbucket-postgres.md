---
created: 2021-04-23
tag: bitbucket
title: Creating multiple Postgres databases in a Bitbucket Pipeline
---
Had an odd one today where some unit tests needed accesses to two separate Postgres
databases. Setting aside the wisdom of these tests, I wanted a way of having access to
two databases in a Bitbucket Pipeline (think Github Actions) without spinning up two
copies of Postgres.

Unfortunately the Postgres Docker image doesn't have an option to specify two databases,
so I needed an alternate solution.

This wasn't particularly tricky to figure out but I couldn't find the exact incantation
online, so consider this my contribution:

```yaml
image: python:3.7

definitions:
  services:
    postgres:
      image: postgres
      variables:
        POSTGRES_USER: "postgres"
        POSTGRES_PASSWORD: "postgres"
        POSTGRES_DB: "database_one"

pipelines:
  default:
    - step:
        name: Run Tests
        services:
          - postgres
        script:
          - apt update -y
          - apt install -y postgresql-client
          - createdb -h 127.0.0.1 -U postgres database_two
          - pip install -r test-requirements.txt
          - pytest --junitxml=./test-reports/coverage.xml
```
