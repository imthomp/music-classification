# Music Classification Project

## Description

Our project aims to leverage machine learning techniques to develop a robust classification model that categorizes songs into genres based on their unique features. We are drawing inspiration from platforms like Spotify, where vast libraries of music demand efficient organization, our endeavor seeks to automate the genre classification process, facilitating seamless music discovery and enhancing user experience.

## Data

### Features

- **Filename**: The filename as provided in the dataset.
- **Tempo**: Represents the speed at which a passage of music is played.
- **Beats**: Denotes the rhythmic units in the music.
- **Chroma_stft**: Refers to the Short Time Fourier Transform, which breaks down the music into segments to analyze frequency content over time.
- **RMSE**: Stands for Root Mean Square Error, a measure of the average magnitude of differences between predicted and actual values.
- **Spectral_centroid**: Indicates the "center of mass" of the spectrum, providing insight into the distribution of frequencies in the music.
- **Spectral_bandwidth**: Describes the wavelength interval where a radiated spectral quantity is at least half its maximum value.
- **Rolloff**: Represents the steepness of a transmission function concerning frequency.
- **Zero_crossing_rate**: Reflects the rate at which the signal changes from positive to negative or vice versa.
- **MFCC1**: Mel-frequency cepstral coefficients (MFCCs) represent the short-term power spectrum of a sound, capturing characteristics such as timbre and pitch.
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

All of these values are continuous, except for the genre. In total, there are 29 features and 1 target column. Ensuring the presence of at least one instance of each genre in the training set is vital to encompass the diversity of music styles for accurate predictions.

## Gathering the Data

The dataset is sourced from a comprehensive collection on [Kaggle](https://www.kaggle.com/datasets/insiyeah/musicfeatures), offering labeled data that streamlines our efforts in feature selection and model refinement. Integration of multiple datasets from Kaggle may be required for comprehensive coverage across music genres.
