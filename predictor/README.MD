## Regression model to predict number of likes on a youtube video:
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

## Numerical based:
* A basic correlation of the number of likes with the numerical features were as following:
![capture1](https://cloud.githubusercontent.com/assets/10993808/26173422/637f0080-3b69-11e7-8fc6-e9474e383323.PNG)
* As expected, the video comment count and view count have a high correlation with the number of likes. The surprising part is that the statistics of channels don’t determine the number of likes on the video. 
* I ran a simple linear regression on the above mentioned features. Divided 1089 videos into 70% training and 30% testing and randomly sampled this set of 10 iterations. 
* The average results were the following:
 * If the output labels are not normalized:
  * average correlation: 0.81
	 * average mean absolute error :3362.41

## Regressor weights: 

![capture2](https://cloud.githubusercontent.com/assets/10993808/26173483/a366f07c-3b69-11e7-8137-a5234c5260b5.PNG)</br>
* If the output labels are normalized: (didn’t make sense doing this because we need the actual number of likes, instead of a relative number).
 * average correlation: 0.86
 * average mean absolute error :0.016

## Weights

![capture3](https://cloud.githubusercontent.com/assets/10993808/26173489/a6d52a80-3b69-11e7-80d0-9ca11b319638.PNG)


## Text Based features:
* Didn’t get time to actually take these out, but jotting down the ideas I had. 
* The following columns are text based:
* Channel title
* Video description
* Localized description
* Localized title
* Tags
* Title
* Comments per video

