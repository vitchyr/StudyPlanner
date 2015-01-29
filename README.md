# StudyPlanner
This program is used to help you study better! Given a class schedule and your
school's academic calendar, this creates a schedule for when to review your
notes. Specifically, study a lecture a day, a week, and a month (4 weeks) after
you first listened to a lecture. This ensures that the material stays in your
(relatively) long term memory, reducing the need to cram for exams.

### Usage
```
python planner.py [savefile]
```

This script requires 2 files to exist in the same directory as `planner.py`:
`calendar.json` and `classes.json`.

### Output
This save the output to `study_schedule.txt` or the `savefile` if provided.
If the file already exists, this script fails. 

###calendar.json
`calendar.json` represents the school's academic calendar. Namely, the start
date, the end date, and vacation days. Here is an example:
```
{
  "start": "1/21/2015",       <- first day of class
  "end": "5/6/2015",          <- last day of class
  "vacations": [
    {
      "start": "1/19/2015",   <- have the same start and end dates to indicate
      "end": "1/19/2015"         that only one day was off
    },
    {
      "start": "2/14/2015",
      "end": "2/17/2015"      <- this should be the last day you're on vacation
    },
    {
      "start": "3/28/2015",
      "end": "4/5/2015"
    },
    ...
  ]
}
```

###classes.json
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
