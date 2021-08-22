import re
def find_age(x):
    if re.match('\d{1,2}',x) != None and x != np.nan:
        a = re.match('\d{1,2}',x).group(0)
        return a
    else:
        x = np.nan