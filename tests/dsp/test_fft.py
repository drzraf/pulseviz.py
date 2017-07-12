import time
import pytest
from pulseviz.dsp.fft import FFT


@pytest.mark.parametrize('window_function', [None, 'hanning'])
@pytest.mark.parametrize('output', ['fft', 'psd'])
def test_analyze(fixture_fake_simple_client, window_function, output):
    analyzer = FFT(sample_size=2048,
                   window_function=window_function,
                   output=output,
                   source_name='foobar',
                   stream_name='pulseviz-tests')

    with analyzer:
        time.sleep(1.0)

    assert analyzer.exit_success


def test_frequencies_and_psd_length():
    analyzer = FFT(sample_size=2048,
                   source_name='foobar',
                   stream_name='pulseviz-tests')

    assert analyzer.frequencies[0] == 0.0
    assert len(analyzer.frequencies) == len(analyzer.values)

