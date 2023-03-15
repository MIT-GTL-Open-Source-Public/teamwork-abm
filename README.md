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

The reference to _da-types.xml_ provides different dialog acts. This file is stored in the _ontologies_ folder.
The file in the first dataset we are working with is reproduced below for reference:

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<da-type nite:id="cmrda" name="da-type" xmlns:nite="http://nite.sourceforge.net/" xmlns:xlink="http://www.w3.org/1999/xlink">
   <da-type nite:id="ami_daclass_0" name="minor" gloss="Minor">
      <da-type nite:id="ami_da_1" name="bck" gloss="Backchannel"/>
      <da-type nite:id="ami_da_2" name="stl" gloss="Stall"/>
      <da-type nite:id="ami_da_3" name="fra" gloss="Fragment"/>
   </da-type>
   <da-type nite:id="ami_daclass_1" name="task" gloss="Task">
      <da-type nite:id="ami_da_4" name="inf" gloss="Inform"/>
      <da-type nite:id="ami_da_6" name="sug" gloss="Suggest"/>
      <da-type nite:id="ami_da_9" name="ass" gloss="Assess"/>
   </da-type>
   <da-type nite:id="ami_daclass_2" name="elicit" gloss="Elicit">
      <da-type nite:id="ami_da_5" name="el.inf" gloss="Elicit-Inform"/>
      <da-type nite:id="ami_da_8" name="el.sug" gloss="Elicit-Offer-Or-Suggestion"/>
      <da-type nite:id="ami_da_11" name="el.ass" gloss="Elicit-Assessment"/>
      <da-type nite:id="ami_da_13" name="el.und" gloss="Elicit-Comment-Understanding"/>
   </da-type>
   <da-type nite:id="ami_daclass_3" name="other" gloss="Other">
      <da-type nite:id="ami_da_7" name="off" gloss="Offer"/>
      <da-type nite:id="ami_da_12" name="und" gloss="Comment-About-Understanding"/>
      <da-type nite:id="ami_da_14" name="be.pos" gloss="Be-Positive"/>
      <da-type nite:id="ami_da_15" name="be.neg" gloss="Be-Negative"/>
      <da-type nite:id="ami_da_16" name="oth" gloss="Other"/>
   </da-type>
   <da-type nite:id="ami_daclass_4" name="unlab" gloss="Unlab"/>
</da-type>
```