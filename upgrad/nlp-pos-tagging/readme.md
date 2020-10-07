**HMMs and Viterbi algorithm for POS tagging**
This assignment involves build your own HMM-based POS tagger and implementing the Viterbi algorithm using the Penn Treebank training corpus. The vanilla Viterbi algorithm given had resulted in ~87% accuracy. The approx. 13% loss of accuracy was majorly due to the fact that when the algorithm encountered an unknown word (i.e. not present in the training set, such as 'Twitter'), it assigned an incorrect tag arbitrarily. This is because, for unknown words, the emission probabilities for all candidate tags are 0, so the algorithm arbitrarily chooses (the first) tag.

In this assignment, the Viterbi algorithm has been modified to solve the problem of unknown words using **at least two techniques**. Though there could be multiple ways to solve this problem, the following approach was taken:
*	Which tag class do unknown words belong to. Identify rules (e.g. based on morphological cues) that can be used to tag unknown words. separate python functions defined to exploit these rules so that they work in tandem with the original Viterbi algorithm.
*	Viterbi algorithm modified so that it considers only one of the transition or emission probabilities for unknown words.

A 'test' file has been given containing some sample sentences with unknown words. 

[Sample test sentences file](https://github.com/vish0701/datasci/blob/master/upgrad/nlp-pos-tagging/Test_sentences.txt)

**Data**
For this assignment, I used the Treebank dataset of NLTK with the 'universal' tagset. [The Universal tagset of NLTK](https://www.nltk.org/_modules/nltk/tag/mapping.html) comprises only 12 coarse tag classes as follows: Verb, Noun, Pronouns, Adjectives, Adverbs, Adpositions, Conjunctions, Determiners, Cardinal Numbers, Particles, Other/ Foreign words, Punctuations.
 Note that using only 12 coarse classes (compared to the 46 fine classes such as NNP, VBD etc.) will make the Viterbi algorithm faster as well.
 
**Goals**
The Treebank dataset into train and validation sets with **a sample size of 95:5** for training: validation sets, to keep the algorithm runtime low.

The following needed to be accomplished in this assignment:
* Write the vanilla Viterbi algorithm for assigning POS tags (i.e. without dealing with unknown words) 
* Solve the problem of unknown words using at least two techniques. These techniques can use any of the approaches discussed in the class - lexicon, rule-based, probabilistic etc. Note that to implement these techniques, you can either write separate functions and call them from the main Viterbi algorithm, or modify the Viterbi algorithm, or both.
* Compare the tagging accuracy after making these modifications with the vanilla Viterbi algorithm.
* List down at least three cases from the sample test file (i.e. unknown word-tag pairs) which were incorrectly tagged by the original Viterbi POS tagger and got corrected after your modifications.



