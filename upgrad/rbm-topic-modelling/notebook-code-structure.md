In this assignment, we shall create a function to perform Gibbs sampling k times within contrastive divergence often referred to as CD-k. Let's understand the structure of the notebook and the CD-k training process:

* Importing the dataset.
* Create a bag of words model.
Note that the shape of a bag of words model will be (data_size, vocablury_size)
Please note that the above shape might vary with the way you perform bag of words model but the index data_size will be the same.
* Training using CD-k. This involves performing Gibbs sampling k-times which can be better understood using the following image.

![](Contrastive-Divergence.png)


1. You start with the input batch of data, v<sub>0</sub>. 
2. You then calculate <br>
&nbsp;&nbsp;&nbsp;&nbsp;<img src="CD-phv0-calc.png" width="247" height="36"><br> Vectorized implementation: <br> 
> p(h|v<sub>0</sub>)=σ(C + V.W)
3. Using this p(h|v<sub>0</sub>), you sample h<sub>0</sub>.
4. Now that you have got h<sub>0</sub>, you calculate
&nbsp;&nbsp;&nbsp;&nbsp;<img src="CD-phv0-calc-2.png" width="247" height="36"><br> Vectorized implementation: <br>  Vectorized implementation: <br>
> p(v|h<sub>0</sub>)=σ(B+H.WT)
5. Using this p(v|h<sub>0</sub>), you sample v<sub>1</sub>.