import librosa
import pandas as pd
import numpy as np

# Function to extract features from a single file
def extract_features(file_path):
    # Load the audio file
    y, sr = librosa.load(file_path)
    length = librosa.get_duration(y=y, sr=sr)
    
    # Extract features
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    harmony, perceptr = librosa.effects.hpss(y)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    
    # Aggregate features
    features = {
        'filename': file_path,
        'length': length,
        'chroma_stft_mean': np.mean(chroma_stft),
        'chroma_stft_var': np.var(chroma_stft),
        'rms_mean': np.mean(rms),
        'rms_var': np.var(rms),
        'spectral_centroid_mean': np.mean(spectral_centroid),
        'spectral_centroid_var': np.var(spectral_centroid),
        'spectral_bandwidth_mean': np.mean(spectral_bandwidth),
        'spectral_bandwidth_var': np.var(spectral_bandwidth),
        'rolloff_mean': np.mean(rolloff),
        'rolloff_var': np.var(rolloff),
        'zero_crossing_rate_mean': np.mean(zcr),
        'zero_crossing_rate_var': np.var(zcr),
        'harmony_mean': np.mean(harmony),
        'harmony_var': np.var(harmony),
        'perceptr_mean': np.mean(perceptr),
        'perceptr_var': np.var(perceptr),
        'tempo': tempo,
    }
    
    # Adding MFCCs
    for i in range(20):
        features[f'mfcc{i+1}_mean'] = np.mean(mfcc[i])
        features[f'mfcc{i+1}_var'] = np.var(mfcc[i])
    
    return features

# Example usage
file_path = 'path/to/your/audio.mp3'  # Replace with the path to your MP3 file
features = extract_features(file_path)

# Convert to DataFrame
df_features = pd.DataFrame([features])

print(df_features)
