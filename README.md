# Music Classification Proposal

## Description

Our project aims to leverage machine learning techniques to develop a robust classification model capable of accurately categorizing songs into genres based on their unique features. Drawing inspiration from platforms like Spotify, where vast libraries of music demand efficient organization, our endeavor seeks to automate the genre classification process, facilitating seamless music discovery and enhancing user experience.

## Data

### Features

- **Filename**: Filename as given in the Marsyas dataset.
- **Tempo**: The speed at which a passage of music is played.
- **Beats**: Rhythmic unit in music.
- **Chroma_stft**: Short Time Fourier Transform.
- **RMSE**: Root Mean Square Error.
- **Spectral_centroid**: Indicates where the "center of mass" of the spectrum is located.
- **Spectral_bandwidth**: The wavelength interval in which a radiated spectral quantity is not less than half its maximum value.
- **Rolloff**: Roll-off is the steepness of a transmission function with frequency.
- **Zero_crossing_rate**: The rate at which the signal changes from positive to negative or back.
- **MFCC1**: Mel-frequency cepstral coefficients (MFCCs) are coefficients that collectively make up an MFC.
- **Label**: Contains a string depicting the genre.

### Sample Data

| Feature            | Value |
|--------------------|-------|
| Tempo              | 103   |
| Beats              | 50    |
| Chroma_stft        | 0.38  |
| Spectral_centroid  | 2116  |
| Spectral_bandwidth | 1956  |
| Rolloff            | 4196  |
| Genre              | Blues |

All of these values are continuous, except for the categorical genre. In total, there are 29 features and 1 target column. Ensuring the presence of at least one instance of each genre in the training set is vital to encompass the diversity of music styles for accurate predictions.

## Gathering the Data

The dataset is sourced from a comprehensive collection on [Kaggle](https://www.kaggle.com/datasets/insiyeah/musicfeatures), offering labeled data that streamlines our efforts in feature selection and model refinement. Integration of multiple datasets from Kaggle may be required for comprehensive coverage across music genres.
