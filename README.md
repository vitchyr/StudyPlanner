# StudyPlanner
This program is used to help you study better. Given a class schedule and your
school's academic calendar, this script creates a schedule for when to review
your lecture notes. Specifically, study a lecture a day, a week, and a month
(4 weeks) after you first listened to a lecture. This ensures that the material
stays in your (relatively) long term memory, reducing the need to cram for
exams.

### Usage
Edit classes.json and calendar.json (see sections below) and then run the
following:
```
python planner.py [savefile]
```
This script requires 2 files to exist in the same directory as `planner.py`:
`classes.json` and `calendar.json`. The `savefile` parameter is optional (see
 Output section).

### classes.json
`classes.json` represents your class schedule. It's a dictionary from a class
name to the day of the week that you have that class. Here is an example:

```
{
  "ECE 4730": ["M", "W"],
  "ECE 3400": ["M", "W", "F"],
  "CS 4670": ["M", "W", "F"],
  "CS 4752": ["M", "W", "F"],
  "ECE 4250": ["T", "R"]
}
```

Days of the week are: M = Monday, T, W, R, F, S, U.

###calendar.json
`calendar.json` represents the school's academic calendar. Namely, the start
date, the end date, and vacation days. The provided calendar.json is the
Cornell Spring 2015 calendar. Here it is with some comments:
```
{
  "start": "1/21/2015",       <- first day of class
  "end": "5/6/2015",          <- last day of class
  "vacations": [
    {
      "start": "2/14/2015",
      "end": "2/17/2015"      <- this should be the last day you're on vacation
    },
    {
      "start": "3/28/2015",
      "end": "4/5/2015"
    },
    {
      "start": "4/27/2015",   <- have the same start and end dates to indicate
      "end": "4/27/2015"         that only one day was off
    }
  ]
}
```

### Output
The output is saved to `study_schedule.txt` or the `savefile` if provided.
If the file already exists, this script fails. Here is a sample output:
```
02/11
  CS 4752 Lec 7, 02/04 (Week)
  ECE 3400 Lec 7, 02/04 (Week)
  ECE 4730 Lec 5, 02/04 (Week)
  CS 4670 Lec 7, 02/04 (Week)
  ECE 4250 Lec 6, 02/10 (Day)
02/12
  ECE 4250 Lec 5, 02/05 (Week)
  CS 4752 Lec 10, 02/11 (Day)
  ECE 3400 Lec 10, 02/11 (Day)
  ...
```
The recommended use of this output is to treat it like a TODO list. Delete
each row after you finish reviewing your lecture notes from that day.
Of course, feel free to do whatever you want with this.
