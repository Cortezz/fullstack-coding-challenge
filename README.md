# Unbabel Fullstack Challenge

Hey :smile:

Welcome to our Fullstack Challenge repository. This README will guide you on how to participate in this challenge.

In case you are doing this to apply for our open positions for a Fullstack Developer make sure you first check the available jobs at [https://unbabel.com/jobs](https://unbabel.com/jobs)

Please fork this repo before you start working on the challenge. We will evaluate the code on the fork.

**FYI:** Please understand that this challenge is not decisive if you are applying to work at [Unbabel](https://unbabel.com/jobs). There are no right and wrong answers. This is just an opportunity for us both to work together and get to know each other in a more technical way.

## Challenge


#### Build a multilingual Hackernews.

Create a multilingual clone of the Hackernews website, showing just the top 10 most voted news and their comments.
This website must be kept updated with the original hackernews website (every 10 minutes).

Translations must be done using the Unbabel API in sandbox mode. (Ask whoever has been in contact with you about the credentials)

Build a dashboard to check the status of all translations.


#### Requirements
* Use Flask web framework
* Use Bootstrap
* For MongoDB
* Create a scalable application.
* Only use Unbabel's Translation API on sandbox mode
* Have the news titles translated to 2 languages
* Have unit tests


#### Notes
* We dont really care much about css but please dont make our eyes suffer.
* Page load time shouldnt exceed 2 secs


#### Resources
* Unbabel's API: http://developers.unbabel.com/
* Hackernews API: https://github.com/HackerNews/API


### Cortezz's fork

Heyo! Here's my take on your challenge! :bowtie:

#### Notes

Here's a few notes about my solution:
* There's two jobs: one which fetches HN posts and another which performs polling on the unfinished translations. The scheduler system that I used was [APS](http://apscheduler.readthedocs.io/).
  1. The HN job checks the current data and only fetches information regarding new posts and comments. It is run every 9 minutes. The initial translation attempt (machine translation) is done in this job.
  2. The polling job checks all unfinished translations every 20 seconds and tries to complete them once.

And here's a list of things I didn't manage to complete:
* Start the polling job only after fetching new HN stories and pause it afterwards.
* Have mocked mongo tests or at least a test database for the tests which involved database operations.
* Have the jobs run on a separate script so they can be called before the server is up and running. Right now the jobs are added.

#### Usage Instructions

Create a virtualenv named env.
```
virtualenv env
```

Install the following packages installed:
```
pip install flask
pip install pymongo
pip install mock
pip install apscheduler
```

Make sure you have Mongo running. Then run the `db_update` to create and populate the database with the first top ten HN stories and their comments.
```
mongod
./db_update
```

And you're good to go!
```
./run.py
```

###### Tests

In order to run the test suite, just run the following script:
```
./run_tests
```
