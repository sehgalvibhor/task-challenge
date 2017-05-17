##Regression model to predict number of likes on a youtube video:
* As mentioned above, I did two things.
* Extract video data. It consisted of 51 columns. The relevant columns were as following:
  * Channel title
  * Video description
  * Localized description
  * Localized title
  * Tags
  * Title
  * Comment count -- N
  * Dislike count -- N
  * Like count -- N
  * Favorite count -- N
* I then mapped these videos to their respective youtube channels and extracted the following out of the data:
  * Comment count -- N
  * Subscriber count -- N
  * Video count -- N
  * View count  -- N

I divided the feature set into two categories - numerical and text based. 

Numerical based:
A basic correlation of the number of likes with the numerical features were as following:
![Image of Model](task-challenge/predictor/Capture1.PNG)
