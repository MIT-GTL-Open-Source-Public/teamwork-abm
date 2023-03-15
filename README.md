# teamwork-abm
An agent based model of teamwork

# Utilities

## Dialog Intent Timeline Plot

The dialog intent timeline plot creates a plot of actors and intents and actions along a timeline,
with the following parameters:

1. Intent Data Location
2. Intent Data Format
3. Output Data Location
4. Output Picture Format
5. Time increments

### Approach

The AMI Corpus is the first data format that we are planning to tackle in this codebase. In the AMI
Corpus, the data is arranged by Experiement/Meeting Number and Agent. For example, _ES2002a_ 
is an experiment code, and _A_ is an agent. The dialog acts for this experiment are store in the folder
_dialogActs_ and hav ethe following files for the 4 agents in the experiment:

1. ES2002a.A.dialog-act.xml
2. ES2002a.B.dialog-act.xml
3. ES2002a.C.dialog-act.xml
4. ES2002a.D.dialog-act.xml