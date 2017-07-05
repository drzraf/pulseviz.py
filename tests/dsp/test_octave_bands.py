import time
import pytest
import numpy.testing
from pulseviz.dsp.octave_bands import OctaveBandsAnalayzer


@pytest.mark.parametrize('fraction', [1, 2, 3])
@pytest.mark.parametrize('weighting', ['A', 'C', 'Z'])
def test_analyze(fixture_null_sink, fixture_audio_playback, fraction, weighting):
    sink_name, source_name = fixture_null_sink

    analyzer = OctaveBandsAnalayzer(sample_size=2048,
                                    fraction=fraction,
                                    weighting=weighting,
                                    source_name=source_name,
                                    stream_name='pulseviz-tests')

    with analyzer:
        time.sleep(1.0)

    assert analyzer.exit_success


def test_octave_bands_center_frequencies():
    analyzer = OctaveBandsAnalayzer(sample_size=44100,
                                    fraction=1,
                                    source_name='whatever')

    # Reference values taken from: http://www.engineeringtoolbox.com/octave-bands-frequency-limits-d_1602.html
    reference_center_frequencies = [16.0, 31.5, 63.0, 125.0, 250.0, 500.0, 1000.0, 2000.0, 4000.0, 8000.0, 16000.0]
    center_frequencies = [center for _, center, _ in analyzer.bands_frequencies]
    numpy.testing.assert_allclose(reference_center_frequencies, center_frequencies, 1)


def test_A_weighting():
    analyzer = OctaveBandsAnalayzer(sample_size=2048,
                                    fraction=1,
                                    weighting='A',
                                    source_name='whatever')

    # Reference values taken from: https://www.vernier.com/til/3500/
    frequencies = [31.5, 63.0, 125.0, 250.0, 500.0, 1000.0, 2000.0, 4000.0, 8000.0]
    reference_A_weightings = [-39.4, -26.2, -16.1, -8.6, -3.2, 0.0, 1.2, 1.0, -1.1]
    A_weightings = [analyzer._calculate_weighting_for_frequency(f, 'A') for f in frequencies]

    numpy.testing.assert_allclose(reference_A_weightings, A_weightings, 1)


@pytest.mark.skip(reason='Not implemented yet.')
def test_C_weighting():
    raise Exception('Not implemented yet.')


def test_Z_weighting():
    analyzer = OctaveBandsAnalayzer(sample_size=2048,
                                    fraction=1,
                                    weighting='Z',
                                    source_name='pulseviz-tests')

    assert analyzer._calculate_weighting_for_frequency(0.0, 'Z') == 1.0
    assert analyzer._calculate_weighting_for_frequency(1337.0, 'Z') == 1.0
    assert analyzer._calculate_weighting_for_frequency(20000.0, 'Z') == 1.0
