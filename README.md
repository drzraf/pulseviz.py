**pulseviz** is a small OpenGL-accelerated audio visualizer for PulseAudio written in Python.
Right now it's more or less a proof of concept with little to no features.

[![Build Status](https://travis-ci.org/pckbls/pulseviz.svg?branch=master)](https://travis-ci.org/pckbls/pulseviz)

![Draft](images/draft_animated.gif)

# Installation

pulseviz can be installed via `pip3`:

```sh
# System wide...
sudo pip3 install git+https://github.com/pckbls/pulseviz.git

# ...or only for the current user
pip3 install --user git+https://github.com/pckbls/pulseviz.git
```

# Usage

pulseviz requires you to choose an audio source and a visualizer type:

```
$ pulseviz
Usage: pulseviz <source> <visualizer>

Available sources:
    alsa_output.pci-0000_00_1b.0.analog-stereo.monitor
    alsa_input.pci-0000_00_1b.0.analog-stereo
    alsa_output.usb-VIA_Technologies_Inc._USB_Audio_Device-00.iec958-stereo.monitor

Available visualizers:
    waveform
    spectrum
    bands
```

By default PulseAudio automatically creates a monitor source for each sink which can be used to visualize the audio that you are hearing.
Those sources have a `.monitor` suffix.

# Future goals

* Make visualizers configurable
  * Either via command line switches...
  * ...or via configuration file
* Stereo support
* Create more visually appealing visualiziations such as
  * [Spectrogram](https://en.wikipedia.org/wiki/Spectrogram#/media/File:Spectrogram-19thC.png)
  * Vectroscope/Stereometer for visualizing the correlation between multiple audio channels
  * [Kodi's rotating 3D Spectrum visualizer](http://kodi.wiki/view/File:Fullscreen_music_controls.png).
  * [Shadertoy](https://www.shadertoy.com/) visualization
  * [projectM](http://projectm.sourceforge.net/) visualization
* Optimize for speed. Smooth 60 frames per seconds with minimal CPU usage are the target.
* Experiment with different digital signal processing algorithms.
* Implement a GUI
  * Most likely based on GTK3
  * Ship two applications `pulseviz` (the original CLI version) and `pulseviz-gtk`
* Something for the far distant future: Support more audio sub systems and platforms.
