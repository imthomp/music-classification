# Music Classification Proposal

## Description

I want to be able to classify a song into a genre based on its song features. I like listening to music and I think it would be interesting to be able to take data based on a song and be able to say which category it falls into. This seems like something a company like spotify would do, because of the sheer amount of songs that they have, it would be nice to be able to automatically classify them into different genres.

## Data

| Feature            | Value |
|--------------------|-------|
| Tempo              | 103   |
| Beats              | 50    |
| Chorma_stft        | .38   |
| Spectal_centroid   | 2116  |
| Spectral_bandwidth | 1956  |
| Rolloff            | 4196  |
| Genre              | Blues |

All of these values are continuous, except for the genre which is categorical. In total there are 29 features and 1 target column. We should be able to look at all of these features (or a combination of them) to determine genre. One thing we need to make sure we do when working with this data is that at least one of each genre is included in the training set, because if the genre “classical” is not in the training set, it will not be used as a value for the predictions.

## Gathering the data

The data comes from a [Kaggle dataset](https://www.kaggle.com/datasets/insiyeah/musicfeatures). It is already labeled and gathered for us, which will save some time and help us focus on feature selection and fine tuning. The Kaggle site has two different datasets and we would need to combine them together first.
