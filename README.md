# AM-album-art
Finds an analytical form for the Artic Monkeys AM album cover using the leading terms from a fourier transform

Run as:
```
python3 am.py
```

Super quick and dirty little project.
Using the first three terms of the imaginary part of the transform gives you a pretty good approximation of the album art. My goal wasn't a perfect reconstruction, just to get something with a reasonably small number of terms that looks reasonably good. So I'm just gonna leave it as is, more or less.

![Imaginary component of the first three terms of the FT compared to the album art](https://imgur.com/BdNaBFR.png)
