# AM-album-art

![AM cover art](https://imgur.com/woLecWp.png)


Finds an analytical form for the Artic Monkeys AM album cover using the leading terms from a fourier transform

Solution: f(x) = Im( (918.4 + 370.7i) * exp(2 * pi * i * 0.0769 * x) + (1700.5 + 497.0i) * exp(2 * pi * i * 0.0635 * x) + (-3958.5 - 755.5j) * exp(2 * pi * i * 0.0702 * x) )

## Description
Super quick and dirty little project to find an equation for the Artic Monkeys AM album art. My goal wasn't a perfect reconstruction, just to get something with a reasonably small number of terms that looks reasonably good.


The waveform is extracted from am.png by converting it to a pixel array and finding where pixels are white (==255.). This gives a rather messy waveform, which I then clean up and apply a fourier transform to. There are three main peaks, so I use three terms of the form;

>A_{i} * e^{2 * \pi * i * f_{i} * t }

Where A_{i} is the complex coefficient from the FT and f_{i} is the corresponding frequency


Using the first three terms of the imaginary part of the transform gives you a pretty good approximation of the album art. So I'm just gonna leave it as is, more or less.


## Run as:
```
python3 am.py
```


## The analysis in images:

### The raw waveform extracted from am.png
![The raw waveform extracted from am.png](https://imgur.com/rUcnhSF.png)

### The waveform extracted from am.png after being cleaned up
![The waveform extracted from am.png after being cleaned up](https://imgur.com/VDqfYmS.png)

### Frequency spectrum from the fourier transform
![Frequency spectrum from the fourtier transform](https://imgur.com/mOAqD7o.png)

### Real (red) and imaginary (blue) parts of the waveform from the three leading terms in the FT
![Real (red) and imaginary (blue) parts of the waveform from the three leading terms in the FT](https://imgur.com/knvZGhk.png)

### Imaginary component of the first three terms of the FT compared to the album art
![Imaginary component of the first three terms of the FT compared to the album art](https://imgur.com/BdNaBFR.png)
