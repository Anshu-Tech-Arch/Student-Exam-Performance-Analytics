import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
np.random.seed(42)
data={
    'student_id':np.arange(1, 301),
    'study_hours':np.random.randint(1, 11, 300),
    'attendance':np.random.randint(50, 101, 300),
    'math_marks':np.random.randint(30, 101, 300),
    'science_marks':np.random.randint(30, 101, 300),
    'english_marks':np.random.randint(30, 101, 300),
    'gender':np.random.choice(['Male', 'Female'], 300)
}
df=pd.DataFrame(data)
df
df['Average Marks']=(df['math_marks']+df['science_marks']+df['english_marks'])/3
plt.figure(figsize=(5,2))
plt.bar(df['gender'], df['Average Marks'])
plt.show()