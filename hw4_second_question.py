# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
cv1 = [{'user': 'john', 'jobs': ['analyst', 'engineer']},
      {'user': 'jane', 'jobs': ['finance', 'software']}]

cv2 = [{'user': 'jess', 'jobs': ['analyst', 'finance']},
      {'user': 'jeremy', 'jobs': ['data science', 'software']}]
list_of_cv = [cv1, cv2]
#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.
def has_experience_as(list_of_cv, job_title):
    candidate = [i['user'] for i in list_of_cv if job_title in i['jobs']]
    return candidate


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.
def job_counts(list_of_cv):
    jobcount = dict()
    for cv in cvs:
        for job in cv['jobs']:
            if jobcount.get(job)!=None:
                jobcount[job] += 1
            else:
                jobcount[job] = 1
    return jobcount

#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
def most_popular_job(list_of_cv):
    popular = ()
    rank = job_counts(list_of_cv)
    popular = sorted(rank, reverse = True)
    return popular