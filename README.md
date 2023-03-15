# teamwork-abm
An agent based model of teamwork

# Utilities

## Dialog Act Timeline Plot

The dialog act timeline plot creates a plot of actors and actions along a timeline,
with the following parameters:

1. Intent Data Location
2. Intent Data Format
3. Output Data Location
4. Output Picture Format
5. Time increments

### Data Map

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
<da-type nite:id="cmrda" name="da-type" 
        xmlns:nite="http://nite.sourceforge.net/" 
        xmlns:xlink="http://www.w3.org/1999/xlink">
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

To get to a timeline from a given dialog act, the words spoken in a meeting can be back-tracked
to files in the _words_ folder. For example, the file _ES2002a.A.words.xml_ starts out as follows:

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<nite:root nite:id="ES2002a.A.words" xmlns:nite="http://nite.sourceforge.net/">
   <w nite:id="ES2002a.A.words0" starttime="77.44" endtime="77.74">Hi</w>
   <w nite:id="ES2002a.A.words1" starttime="77.74" endtime="77.74" punc="true">,</w>
   <w nite:id="ES2002a.A.words2" starttime="77.74" endtime="78.16">I&#39;m</w>
   <w nite:id="ES2002a.A.words3" starttime="78.16" endtime="78.6">David</w>
   <w nite:id="ES2002a.A.words4" starttime="78.6" endtime="78.85">and</w>
...   
```

In addition, the folder _topics_ contains segmentation of the meeting into topics. For example,
the file _ES2002a.topic.xml_ starts out as:

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<nite:root nite:id="ES2002a.topic" xmlns:nite="http://nite.sourceforge.net/">
   <topic nite:id="ES2002a.topic.vkaraisk.1" other_description="introduction of participants and their roles">
      <nite:pointer role="scenario_topic_type"  href="default-topics.xml#id(top.4)"/>
      <nite:child href="ES2002a.B.words.xml#id(ES2002a.B.words0)..id(ES2002a.B.words71)"/>
      <nite:child href="ES2002a.D.words.xml#id(ES2002a.D.words0)..id(ES2002a.D.words3)"/>
      <nite:child href="ES2002a.A.words.xml#id(ES2002a.A.words0)..id(ES2002a.A.words12)"/>
      <nite:child href="ES2002a.B.words.xml#id(ES2002a.B.words72)..id(ES2002a.B.words73)"/>
      <nite:child href="ES2002a.D.words.xml#id(ES2002a.D.words4)..id(ES2002a.D.words11)"/>
      <nite:child href="ES2002a.C.words.xml#id(ES2002a.C.words0)..id(ES2002a.C.words7)"/>
      <nite:child href="ES2002a.D.words.xml#id(ES2002a.D.words12)..id(ES2002a.D.words13)"/>
   </topic>
   <topic nite:id="ES2002a.topic.vkaraisk.2" other_description="project goals and design process">
      <nite:pointer role="scenario_topic_type"  href="default-topics.xml#id(top.4)"/>
      <nite:child href="ES2002a.B.words.xml#id(ES2002a.B.words74)..id(ES2002a.B.words192)"/>
      <nite:child href="ES2002a.A.words.xml#id(ES2002a.A.words13)..id(ES2002a.A.words48)"/>
      <nite:child href="ES2002a.B.words.xml#id(ES2002a.B.words193)..id(ES2002a.B.words194)"/>
      <nite:child href="ES2002a.D.words.xml#id(ES2002a.D.words14)..id(ES2002a.D.words23)"/>
      <nite:child href="ES2002a.C.words.xml#id(ES2002a.C.words8)..id(ES2002a.C.words9)"/>
      <nite:child href="ES2002a.D.words.xml#id(ES2002a.D.words24)..id(ES2002a.D.words25)"/>
      <nite:child href="ES2002a.B.words.xml#id(ES2002a.B.words195)..id(ES2002a.B.words225)"/>
   </topic>
...
```

### Approach

Once the data folder and meeting id is provided, the code will scan the dia