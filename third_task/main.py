import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fig, axes = plt.subplots(4, 1)

first_func = pd.Series(np.random.rand(12))
second_func = pd.Series(np.random.rand(12))

third_func = pd.DataFrame(
    np.random.rand(5, 3),
    index=range(5),
    columns=pd.Index(['C', 'B', 'A'], name='Third Function'),
)

first_func.plot.barh(ax=axes[0], color='orange', alpha=1)
second_func.plot.bar(ax=axes[1], color='red', alpha=0.6)
third_func.plot.bar(ax=axes[2], alpha=0.8)

third_func.plot(ax=axes[3], kind='barh', stacked=True)
plt.show()
