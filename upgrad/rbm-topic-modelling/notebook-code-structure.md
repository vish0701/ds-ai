In this assignment, we shall create a function to perform Gibbs sampling k times within contrastive divergence often referred to as CD-k. Let's understand the structure of the notebook and the CD-k training process:

* Importing the dataset.
* Create a bag of words model.
Note that the shape of a bag of words model will be (data_size, vocablury_size)
Please note that the above shape might vary with the way you perform bag of words model but the index data_size will be the same.
* Training using CD-k. This involves performing Gibbs sampling k-times which can be better understood using the following image.<br>
<img src="Contrastive-Divergence.png" width="450" height="150">

1. You start with the input batch of data, v<sub>0</sub>. 
2. You then calculate <img src="CD-phv0-calc.png" width="247" height="36"><br> Vectorized implementation: p(h|v<sub>0</sub>)=σ(C + V.W)
3. Using this p(h|v<sub>0</sub>), you sample h<sub>0</sub>.
4. Now that you have got h<sub>0</sub>, you calculate
<img src="CD-phv0-calc-2.png" width="247" height="36"><br> Vectorized implementation: p(v|h<sub>0</sub>)=σ(B+H.WT)
5. Using this p(v|h<sub>0</sub>), you sample v<sub>1</sub>.

You repeat this k times till you get h<sub>k</sub> and v<sub>k</sub>.

Step 2 and 3 are performed in the function *sampleHiddenLayer()* while Step 4 and 5 are performed in *sampleVisibleLayer()*. 

*sampleHiddenLayer()* and *sampleVisibleLayer()* are combined to create a function *gibbs()* which does one iteration of Gibbs sampling.

gibbs is repeated k-times in the function *cd_k()* to perform Contrastive Divergence k-times.


To maximize the joint probability distribution, using the energy function as defined in the above sampling process, the update matrices and vectors simplify as follows:

1. ΔW = v<sub>0</sub> ⊗ p(h<sub>0</sub>|v<sub>0</sub>) − v<sub>k</sub>⊗p(h<sub>k</sub>|v<sub>k</sub>)
2. Δb = avg_across_batch(v<sub>o</sub>−v<sub>k</sub>)
3. Δc = avg_across_batch(p(h<sub>0</sub>|v<sub>o</sub>)−p(h<sub>k</sub>|v<sub>k</sub>))

You do average across batch because you need a vector update for the bias vectors and v<sub>o</sub>,<sub>k</sub> and p(h<sub>0</sub>|v<sub>o</sub>),p(h<sub>k</sub>|v<sub>k</sub>) are matrices.

Since we have to maximize the joint probability distribution, we use gradient ascent here with momentum.

The momentum equations are as follows:

1. mW<sub>t</sub>=γ mW<sub>t−1</sub> − ΔW
2. mb<sub>t</sub>=γ mb<sub>t−1</sub> − Δb
3. mc<sub>t</sub>=γ mc<sub>t−1</sub> − Δc

γ is the momentum coefficient here.

Using these momentum terms, you update the weights and biases as follows:

1. W<sub>t</sub> = W<sub>t−1</sub> + α mW<sub>t</sub>
2. b<sub>t</sub> = b<sub>t−1</sub> + α mb<sub>t</sub>
3. c<sub>t</sub> = c<sub>t−1</sub> + α mc<sub>t</sub>

α is the learning rate.

The above equations are implemented in the function *train()*.

