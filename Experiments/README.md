# Experiments

| Architecture  | Hyperparams                                                                                          | Cairo: validation accuracy | Cairo: Test accuracy | Milan: validation accuracy | Milan: Test accuracy | kyoto7: validation accuracy | kyoto7: Test accuracy |
| ------------- | ---------------------------------------------------------------------------------------------------- | -------------------------- | -------------------- | -------------------------- | -------------------- | --------------------------- | --------------------- |
| LSTM          | EPOCHS: 50 \| EMBEDDING SIZE: 1000 (high dim) \| ADAM lr = 0.001                                     | 83.24                      | 77.88                |                            |                      |                             |                       |
| biLSTM        | EPOCHS: 50 \| EMBEDDING SIZE: 1000 (high dim) \| ADAM lr = 0.001                                     | 91.34                      | 89.43                |                            |                      | 79.65                       | 73.44                 |
| biLSTM        | EPOCHS: 30 \| EMBEDDING SIZE: 1000 (high dim) \| ADAM lr = 0.001                                     |                            |                      | 94.12                      | 94.84                | 73.45                       | 68.75                 |
| biLSTM        | EPOCHS: 30 \| EMBEDDING SIZE: 104 (total number of unique sensor activations + 1) \| ADAM lr = 0.001 | 90.27                      | 82.27                |                            |                      |                             |                       |
| biLSTM        | EPOCHS: 30 \| EMBEDDING SIZE: 104 (total number of unique sensor activations + 1) \| ADAM lr = 0.005 |                            |                      |                            |                      |                             |                       |
| cascadedSLSTM | EPOCHS: 30 \| EMBEDDING SIZE: 104 (total number of unique sensor activations + 1) \| ADAM lr = 0.005 | 82.28                      | 77.88                |                            |                      |                             |                       |

  

--- 
---

### How the experiments were structured:

First all different types of model architectures were tried out on the cairo dataset with different hyperparameters in different experiments to gain an understanding how the changes influence the result.

After gaining an understanding of this, we tried out different datasets of different sizes with the best architecture to reach a conclusion about the generalization capabilities of our model.

### Size:

- **cairo**: 1031 samples (10% test and 18% validation)
- **milan**: 4252 samples (10% test and 18% validation)
- **kyoto7**: 631 samples (10% test and 18% validation)

### Observations:

- Bidirectional LSTM perform better on the task than unidirectional LSTM's.
- More complex model architecture like a cascaded LSTM model fail to perform better than a bidirectional LSTM.
- Embedding size: as expected a high dimension embedding matrix did not provide any advantages than to limit at the size of the number of unique sensor activations.
- Adam optimizer with default learning rate of 0.001 gave optimal results.
- The model failed to perform well when there wasn't much data. This trend can be observed in the variation in performance in the three different datasets of different sizes.
- In the case of kyoto7, the model failed to perform well even when the task was simpler because of not enough data.
- In the case of Milan, the model performed well, even with the task being the toughest because there were sufficient data for the model to learn the general sequences for the activities.

**_NOTE:_**

We need more data to achieved better performance in each case and also we require the dataset to be balanced, so the model predicting common activies do not dominate the overall accuracy.
