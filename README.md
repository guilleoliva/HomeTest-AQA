<div style="text-align: center;">
  <img src="sporty.png" style="width:70%; height:auto;" alt="Responsive Centered Image">
</div>

# QA Automation

### Description

This framework features are:
- Selenium 
- Behave as Behaviour-Driven Development
- Page Object Pattern Design
- HTML Report
- And Requests to cover APIs tests

### Pre-requisites
- Install Python 3.10: https://www.python.org/downloads/release/python-3100/
- Install Poetry: https://python-poetry.org/docs/
- On Windows if you need Microsoft Visual C++ 14.0 https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170 


### Installing dependencies
 ```poetry install```

### To execute tests locally:
Execute the following command, by replacing \<TAG\> by any scenario tags you would like to execute, the environment by default is dev but if you want to specify it, you can use the env parameter inside the command line:
```
behavex -t SPORTY-TEST -D browser=chrome -D env=<qa or dev>
```

### To execute tests inside a CI env:
Execute the following command, by replacing \<TAG\> by any scenario tags you would like to execute:

```
behavex -t API -D browser=chrome -D headless_browser -D env=<qa or dev>
```

### Requested Snapshot in test statement
* The Snapshot requested in the test is available after the automation finalize, inside the /output folder as "screenshot.png"


### Gif with the Automation running the proposed test scenario
<div style="text-align: center;">
  <img src="sporty-test-result.gif" alt="Automation Result" style="max-width: 100%; height: auto;">
</div>


### Testing solution documentation
As the testing solution consists of a wrapper (called BehaveX) on top of Python Behave, please take a look at the Behave documentation:
https://behave.readthedocs.io/en/stable/

