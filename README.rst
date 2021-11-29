Quizer Module Repository
========================

This tool allows to use photos database as input for testing yourself
in recognition.

By default it has a base containing photos of animals needed for passing hunter exam in Norway.

0. Prerequisites

- Needed for any other item
- Install Python 3.9+
- Install requirements.txt

1. QUIZER

- Run quiz.py inside quizes directory
- By default test has 20 questions

2. VIEWER

- To view the database run viewer.py
- That functions loads all the photos at once
- startup might be longer
- It shows all prefixes for all entries
- Random button moves the view to random index between first and last
- Goto button will move to the index (if valid) provided in entry box

FAQ

**Tkinter missing**

Might require to be installed separately on Linux machines.
For me that was solved by:

sudo apt-get install python3.9-tk

**ValueError: Namespace Gst not available**

If sounds cannot be played under Linux, try installing:

sudo apt-get install gstreamer-1.0