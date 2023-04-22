# NBA-Basketball-Analysis-Platform
### Abstract
Sports have always played an important role in our daily lives for a long time, among which ball games have become the most popular competitive sports. Combining our interests with our expertise in data science, we use machine learning methods to investigate basketball match prediction and player capacity evaluation in detail in this article. In match prediction part, we separate into two parts. The first part is making the input features. We use Elo mechanism, PCA analysis and factor analysis to evaluate the capacity of each team to make the input features. And the second part is implemented machine learning models. We implement decision tree, random forest, logistic regression, SVM, neural network, LSTM to make the prediction. In players’ capacity evaluation part, we implement the 2D and 3D K-Means Clustering and PCA to illustrate the capacity of different types of players. Besides the complete analysis with charts and table for predictions and capacity evaluations, the final demo would be integrated into a webpage which allow NBA basketball fans to find the interesting combination of players and examine different predictions based on different models.

### User Interface
![](https://github.com/JaczzzZ/NBA-Basketball-Analysis-Platform/blob/main/NBA.png)

### Technical
* Web Page Frame: Django
* Database: Mysql
* Language: Python

### Data
Capture the data from https://www.basketball-reference.com/

### How to run
Run the code in the file directory that owns manage.py
```
python manage.py runserver
```
