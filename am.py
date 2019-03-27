import imageio
import numpy as np
import matplotlib.pyplot as plt

def FFT(x, y):
    ''' 
        Perform the Fast Fourier Transform
    '''

    ft    = np.fft.fft(y)                                              # Perform the FFT
    freqs = np.linspace(0, 1/abs((x[1]-x[0])), len(x))                 # Generate the frequency data (transformed x-values)

    ## This is a rather subtle point related to fourier transforms
    ## Since the input is real-valued, only half of the output is actual info.
    ft    = ft[   :len(freqs)//2]
    freqs = freqs[:len(freqs)//2]

    return freqs, ft

def main():

    img           = np.asarray(imageio.imread('AM.png'))
    img_y, img_x  = np.where(img==255)                  # Onle where the pic is white
    
    img_x = img_x - len(img)//2                         # Center pixel axis at 0,0
    img_y = img_y - len(img)//2                         # Center pixel axis at 0,0
    img_y = -1*img_y                                    # For some reason Y's are loaded in a mirror image???

    ### Plot the waveform before being cleaned up
    print("Plotting >> raw extracted waveform")
    plt.plot(img_x, img_y, 'o')
    plt.show()

    ### The image is also not a single pixel waveform, so if one X-value has several Y-pixels at 255, use the middle one.
    clean_x = []
    clean_y = []
    for xi in img_x:
        if not xi in clean_x:                           # Only append x', or y' to clean_<> once
            xi_idx = np.where(img_x==xi)
            repeated_ys = []
            for yi in xi_idx:                           # Both arrays' indices are the same. (IE zip(x,y) does what you would want)
                repeated_ys.append(img_y[yi])
            mean_yi = np.mean(repeated_ys)              # Take the avg of all the y's in a column(x-value) where the pixels are at 255
            clean_x.append(xi)
            clean_y.append(mean_yi)

    clean_x, clean_y = zip(*sorted(zip(clean_x, clean_y), key=lambda x: x[0]))  # Sneaky, sort both clean_x and _y based on the _x's

    ### Plot the waveform after being cleaned up
    print("Plotting >> cleaned up waveform")
    plt.plot(clean_x, clean_y)
    plt.show()

    ### Perform the FFT
    freqs, img_ft = FFT(clean_x, clean_y)

    ### Plot the frequency spectrum
    print("Plotting >> frequency spectrum")
    plt.plot(freqs, np.abs(img_ft))
    plt.show()

    ### Sort the freqs and fourier data by the maximum amplitudes of each point.
    sorted_fft = sorted(zip(freqs, img_ft), key=lambda x: np.abs(x[1]) )
    sorted_x, sorted_y = zip(*sorted_fft)

    ### How many terms to use in the approximation
    nterms = 3
    Fs = sorted_x[-1*nterms:]                           # Top <nterms> frequency components
    As = sorted_y[-1*nterms:]                           # Top <nterms> complex valued coefficients (contains amp. and phase info)
                                                        # Use np.abs(As[i]) for the amplitude, and np.angle(As[i]) for... you get it.

    ### Define the function so add sine terms from the FFT
    def f(t):
        i = pow(-1,0.5)
        sum = 0
        for f, a in zip(Fs, As):
            sum += a*np.exp(i*2*np.pi*f*t)              # X = Sum{ A_i * exp(i*w*t) }, A_i is the complex coeff, w is the angular frequency 2*pi*F_i 
        return sum
    
    xs = np.arange(-150,150,0.1)                        # Initialize some X values in our original domain
    y_r = np.real(f(xs))
    y_i = np.imag(f(xs))

    ### Plot the final generated waveform
    print("Plotting >> final waveform generated")
    plt.plot(xs, y_r, 'r')                        # Plot our fourier generated waveform. np.real(...) to prevent a complex->real warning being printed
    plt.plot(xs, y_i, 'b')                        # Plot our fourier generated waveform. np.real(...) to prevent a complex->real warning being printed
    plt.show()

    ### Plot the final over the original for comparison
    print("Plotting >> target and output waveforms overlayed")
    plt.plot(clean_x, clean_y/max(clean_y), 'g')
    plt.plot(xs, y_r/max(y_r), 'r')                        # Plot our fourier generated waveform. np.real(...) to prevent a complex->real warning being printed
    plt.plot(xs, y_i/max(y_i), 'b')                        # Plot our fourier generated waveform. np.real(...) to prevent a complex->real warning being printed
    plt.show()

    ### Plot just the imaginary part of the output over the original for comparison
    print("Plotting >> just the imaginary part")
    plt.plot(xs, y_i/max(y_i), 'b')                        # Plot our fourier generated waveform. np.real(...) to prevent a complex->real warning being printed
    plt.show()


    return

if __name__=="__main__":
    main()
