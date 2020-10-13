This assignment calls for trainin a Restricted Boltzmann Machine to perform Topic Modelling on a set of Amazon reviews.

Topic Modelling is the art and science of identifying the 'latent topics' in a text. It is an unsupervised problem. You input a set of documents/ corpus into the model and the model finds the topics that describe the corpus. Each topic is a distribution over the words that best describe the topic. 

Let's understand this with the help of an example:

Suppose you are given reviews about a product, for example, iPhone. You can perform topic modelling to see what topics are the people in the reviews talking about. Consider that we have input to the model that we want 3 top topics from the reviews.

The top 5 words that describe the topics are shown below:
|Topic 1 |	Topic 2	 | Topic 3 |
|--------|-----------|---------|
| pixel	| smooth	| slow |
| selfie |	apps	| memory |
| good	| hangs	| storage |
| blur	| interface	| full |
| filter |	intelligent	| apps |

Looking at the above words, we can say that Topic 1 mostly talks about the camera of iPhone while Topic 2 talks about the iOS operating system and Topic 3 talks about the storage memory available. It might often happen that you might not be able to figure out the topics from the distribution of the words.

 

After getting the topics, you can do a lot of things like:

    Find the distribution of each review over the topics
    Couple the topics and sentiments of each review and see which topics more often in negative reviews
    Use the topic representation of each document as a feature representation for developing further machine learning models

You can use different models to perform topic modelling, one of which is LDA  which you have studied earlier in the Natural Language Processing course.

In this assignment, we will use a Restricted Boltzmann Machine (RBM) to perform topic modelling. The input to an RBM is a bag of words model and the output is the distribution of words in the topics.

[Dataset](amazon.csv) used for this assignment.