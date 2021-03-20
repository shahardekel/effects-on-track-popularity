# effects-on-track-popularity

- Song recommendation apps are popular with listeners who want a convenient track selection interface.
- It is easy to find the right music or podcast for every moment. The various applications often provide details about the artist's name, the name of track, the duration of the track and the popularity rating of the app users who listen to the tracks.
- High-rated tracks may attract more listeners. Therefore, it is in the interest of the artist’s tracks that the overall rating of their track will be higher relative to competing tracks.
- The causal effects we want to assess are:
1) How does the track’s danceability affect its popularity?
2) How does the track’s liveness affect its popularity?
3) How does a change in the track time-signature affect its popularity?

- Motivated to raise the track’s popularity and thereby increase the number of listeners.


- In our study, we used various functionalities on Python, including the Pandas, sklearn, numPy, Seaborn and matplotlib.pyplot libraries. Also, for the causal forests CATE estimations we used R functionalities.

- Our report includes the code:
1. data_analysis.py- for the Data Analysis chapter.
2. data_preparation.py- for the Data Preparation chapter.
3.	X_learner.py and methods.py- for the Experiment and Results chapter- X-Learner method.
4.	causal_forest.R- for the Experiment and Results chapter- Causal Forests method.

- To get familiar with our results, first run data_analysis.py and then data_preparation.py.
- To get the results for the X-Learner method- run X_learner.py.
- To get the results for the Causal Forests method- run causal_forest.R.


- The CSV can be found here: https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db
