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

An example of data in each file is as follows:

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<nite:root nite:id="ES2002a.A.dialog-act" xmlns:nite="http://nite.sourceforge.net/">
   <dact nite:id="ES2002a.A.dialog-act.dharshi.1">
      <nite:pointer role="da-aspect"  href="da-types.xml#id(ami_da_4)"/>
      <nite:child href="ES2002a.A.words.xml#id(ES2002a.A.words0)..id(ES2002a.A.words12)"/>
   </dact>
   <dact nite:id="ES2002a.A.dialog-act.dharshi.2">
      <nite:pointer role="da-aspect"  href="da-types.xml#id(ami_da_4)"/>
      <nite:child href="ES2002a.A.words.xml#id(ES2002a.A.words13)..id(ES2002a.A.words27)"/>
   </dact>
...
```
