import datetime

"""
Month choices from here, goes into SearchForm and the user can select
from these months and can also search from the same.
"""
MONTH_CHOICES = ((datetime.date.today().month,datetime.datetime.now().\
    strftime("%B")), ('1', 'January'), ('2', 'February'), 
    ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), 
    ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), 
    ('11', 'November'), ('12', 'December'),
)
