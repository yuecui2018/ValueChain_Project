#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:43:08 2018

@author: yuecui
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)

from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
import matplotlib.pyplot as plt

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

from scipy import stats
import statsmodels.api as sm
###Read data
data = pd.read_csv("/Users/yuecui/Desktop/ValueChain/Project/events.csv")




###Proportion of NA for each column
data.isnull().sum()/941009

"""
id_odsp          0.000000
id_event         0.000000
sort_order       0.000000
time             0.000000  yes
text             0.000000   
event_type       0.000000  yes
event_type2      0.772273  
side             0.000000  yes
event_team       0.000000
opponent         0.000000
player           0.064824
player2          0.690428
player_in        0.945043
player_out       0.945019
shot_place       0.758282  
shot_outcome     0.757178
is_goal          0.000000  yes
location         0.503653
bodypart         0.756448
assist_method    0.000000  yes
situation        0.756499
fast_break       0.000000  yes
dtype: float64
"""

data.dtypes

"""
id_odsp           object
id_event          object
sort_order         int64
time               int64
text              object
event_type         int64
event_type2      float64
side              object
event_team        object
opponent          object
player            object
player2           object
player_in         object
player_out        object
shot_place       float64
shot_outcome     float64
is_goal            int64
location         float64
bodypart         float64
assist_method      int64
situation        float64
fast_break         int64
body              object
dtype: object
"""


#####Two potential y variables


### 'shot_outcome'
df['shot_outcome'].unique()

"""
1	On target
2	Off target
3	Blocked
4	Hit the bar
"""

df['shot_outcome'].value_counts()

"""
2.0    92827
1.0    78014
3.0    54082
4.0     3575
Name: shot_outcome, dtype: int64
"""

### 'is_goal'
df['is_goal'].value_counts()

"""
0    204682
1     23816
"""

###Not matched! Use is_goal since no NA




###Y variable 

data['is_goal'].value_counts()/941009
sns.countplot(x="is_goal", data=data)
plt.show()

####0.974022 goal, 0.025978 not goal



"""
side
1	Home
2	Away
"""

data['side'].value_counts()
data['side'] = data.astype(object)

data['side'] = np.where(data['side'] == 1, 'Home', 'Away')
data['side'].head()


"""
bodypart
1	right foot
2	left foot
3	head
"""



#data["bodypart"].isnull().sum()

data.loc[data['bodypart'] == 1, 'body'] = 'right'
data.loc[data['bodypart'] == 2, 'body'] = 'left'
data.loc[data['bodypart'] == 3, 'body'] = 'head'


data["body"].isnull().sum()




"""
time
"""

data["time"].head(10)

sns.distplot(data['time'],bins=50)

"""
text
"""

data["text"].head(10)

"""
event_type
0	Announcement
1	Attempt
2	Corner
3	Foul
4	Yellow card
5	Second yellow card
6	Red card
7	Substitution
8	Free kick won
9	Offside
10	Hand ball
11	Penalty conceded
"""

data["event_type"].value_counts()/941009

bins = np.linspace(0, 12, 20)
plt.hist(data['event_type'],bins,alpha=0.5)



"""
8     0.252848
3     0.247527
1     0.243499
2     0.096921
7     0.054981
9     0.046201
4     0.042413
10    0.011403
11    0.002876
6     0.001224
5     0.000106
"""

m = {"other": [10,11,9,7], "FreeKick": [8], "Foul": [3], "Attempt": [1],"Card":[4,5,6],"Corner":[2]}

m2 = {v: k for k,vv in m.items() for v in vv}
m2

data["event_type"] = data.event_type.map(m2).astype("category", categories=set(m2.values()))

data["event_type"].value_counts()/941009


sns.countplot(x="event_type", data=data)
plt.show()

"""
event_type2
12	Key Pass
13	Failed through ball
14	Sending off
15	Own goal
"""
data["event_type2"].value_counts()


"""
shot_place
1	Bit too high
2	Blocked
3	Bottom left corner
4	Bottom right corner
5	Centre of the goal
6	High and wide
7	Hits the bar
8	Misses to the left
9	Misses to the right
10	Too high
11	Top centre of the goal
12	Top left corner
13	Top right corner
"""
data['shot_place'].value_counts()/data['shot_place'].value_counts().sum()

##Not useful


"""
location
1	Attacking half
2	Defensive half
3	Centre of the box
4	Left wing
5	Right wing
6	Difficult angle and long range
7	Difficult angle on the left
8	Difficult angle on the right
9	Left side of the box
10	Left side of the six yard box
11	Right side of the box
12	Right side of the six yard box
13	Very close range
14	Penalty spot
15	Outside the box
16	Long range
17	More than 35 yards
18	More than 40 yards
19	Not recorded
"""

data['location'].value_counts()/data['location'].value_counts().sum()

sns.countplot(x="location", data=data)
plt.show()
### Need further manipulation

"""
assist_method
0	None
1	Pass
2	Cross
3	Headed pass
4	Through ball
"""

data['assist_method'].value_counts()/data['assist_method'].value_counts().sum()

m = {"None": [0], "Pass": [1,2,3,4]}

m2 = {v: k for k,vv in m.items() for v in vv}
m2

data["assist_method"] = data.assist_method.map(m2).astype("category", categories=set(m2.values()))

data["assist_method"].value_counts()/941009

sns.countplot(x="assist_method", data=data)
plt.show()

data["assist_method"].dtype
"""

situation
1	Open play
2	Set piece
3	Corner
4	Free kick
"""
data['situation'].value_counts()/data['situation'].value_counts().sum()



"""
fast_break
"""
data['fast_break'].value_counts()
plt.hist(data['fast_break'])


######Visualization x's vs y

table=pd.crosstab(data.assist_method,data.is_goal)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Assist vs Is_Goal')
plt.xlabel('Assist')
plt.ylabel('Proportion of scoring')
plt.savefig('assist_vs_goal_stack')

table=pd.crosstab(data.event_type,data.is_goal)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Event_type vs Is_Goal')
plt.xlabel('Event_type')
plt.ylabel('Proportion of scoring')
plt.savefig('event_vs_goal_stack')


table=pd.crosstab(data.body,data.is_goal)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Body_part vs Is_Goal')
plt.xlabel('Body_part')
plt.ylabel('Proportion of scoring')
plt.savefig('Body_part_vs_goal_stack')


table=pd.crosstab(data.side,data.is_goal)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Assist vs Is_Goal')
plt.xlabel('Assist')
plt.ylabel('Proportion of scoring')
plt.savefig('assist_vs_goal_stack')



table=pd.crosstab(data.fast_break,data.is_goal)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of fast_break vs Is_Goal')
plt.xlabel('fast_break')
plt.ylabel('Proportion of scoring')
plt.savefig('fast_break_vs_goal_stack')

