import json
import datetime
import os.path
import sys

"""
Author: Vitchyr Pong
"""

def get_json(fname):
  json_data = open(fname).read()
  return json.loads(json_data)

def date_of(s):
  """Converts a string of format 2015-01-28 to date."""
  return datetime.datetime.strptime(s, '%m/%d/%Y').date()

def iso_day(d):
   return {
     'M': 1,
     'T': 2,
     'W': 3,
     'R': 4,
     'F': 5,
     'S': 6,
     'U': 7,
   }[d]

def create_schedule(cal_fname, classes_fname, save_fname):
  """
  Note: I know I'm not being very efficient, but considering a semester usually
  lasts ~120 days, this isn't important.
  """
  classes = get_json(classes_fname)
  cal = get_json(cal_fname) 

  # get the vacation days
  vacations = \
    [(date_of(v["start"]), date_of(v["end"])) for v in cal["vacations"]]
  vacation_dates = []
  for v in vacations:
    start, end = v
    assert (end - start).days >= 0, \
      "Invalid vacation date ranges: {0} - {1}".format(start, end)
    date = start
    vacation_dates.append(date)
    while (date != end):
      date += datetime.timedelta(days=1)
      vacation_dates.append(date)

  fdoc = date_of(cal["start"]) # first day of class
  ldoc = date_of(cal["end"]) # first day of class
  n_days = (ldoc - fdoc).days

  lectures = [[] for i in range(n_days)]
  lec_nums = {}
  for k in classes.keys():
    lec_nums[k] = 1

  # populate the list of all lectures
  date = fdoc
  for i in range(n_days):
    for class_name, days in classes.items():
      iso_days = [iso_day(d) for d in days] 
      if date.isoweekday() in iso_days and date not in vacation_dates:
        lectures[i].append(
          "{0} Lec {1}, {2}".format(class_name, lec_nums[class_name],
            date.strftime("%m/%d"))
        )
        lec_nums[class_name] += 1
    date += datetime.timedelta(days=1)
 
  # make the study schedule based on the study rule
  study_schedule = [[] for i in range(n_days + 28)]
  for i, ls in enumerate(lectures):
    study_schedule[i + 1] += [l + " (Day)" for l in ls]
    study_schedule[i + 7] += [l + " (Week)" for l in ls]
    study_schedule[i + 28] += [l + " (Month)" for l in ls]
  
  # Save the schedule
  with open(save_fname, 'w') as outfile:
    to_save = [{} for i in range(len(study_schedule))]
    date = fdoc
    for lectures in study_schedule:
      if len(lectures) != 0:
        outfile.write("{0}\n".format(date.strftime("%m/%d")))
        for l in lectures:
          outfile.write("  {0}\n".format(l))
      date += datetime.timedelta(days=1)

if __name__ == '__main__':
  cal_fname = "calendar.json"
  classes_fname = "classes.json"

  save_fname = "study_schedule.txt"
  if len(sys.argv) > 1:
    save_fname = sys.argv[1]

  if os.path.isfile(save_fname):
    print("File {0} already exists.".format(save_fname))
  else:
    create_schedule(cal_fname, classes_fname, save_fname)
