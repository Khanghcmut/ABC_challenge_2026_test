from tsfel.feature_extraction.features_utils import set_domain
import numpy as np
from scipy import stats
# from scipy.fft import rfft, rfftfreq
# from scipy.stats import entropy
from numpy import trapz,trapezoid

# --- Step 1: Define custom features ---



@set_domain("domain", "statistical")
def Mode(signal):
    """
    Calculate the mode (most frequent value) of the input signal.

    Parameters:
        signal (array-like): 1D array, list, or Series containing numerical data.

    Returns:
        float: Mode of the signal. If multiple modes, returns the smallest one.
    """
    mode_result = stats.mode(signal, keepdims=False)
    return mode_result.mode


@set_domain("domain", "statistical")#temperal feat***
def AUC(signal, fs=1.0):
    """
    Compute the Area Under the Curve (AUC) of a 1D signal using trapezoidal integration.

    Parameters:
    - signal: 1D numpy array
    - fs: Sampling frequency in Hz (default: 1.0)

    Returns:
    - auc_value: Area under the curve
    """
    t = np.arange(len(signal)) / fs  # Time axis in seconds
    auc_value = trapz(np.abs(signal), x=t)  # AUC of absolute signal
    return auc_value

@set_domain("domain", "statistical")#temperal feat***
def AUC_abs(signal, fs=1.0):
    """
    Compute the AUC of the absolute value of a 1D signal using trapezoidal integration.

    Parameters:
    - signal: 1D numpy array
    - fs: Sampling frequency in Hz (default: 1.0)

    Returns:
    - auc_abs_value: Area under the curve of |signal|
    """
    t = np.arange(len(signal)) / fs  # Time axis in seconds
    auc_abs_value = trapezoid(np.abs(signal), x=t)
    return auc_abs_value
