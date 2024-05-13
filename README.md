
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

# Bundling score
Small utility to extract the bundling score from actomyosin network images.

## Installation

### With conda: if on windows or if you are not used to pip
1. If you don’t already have Anaconda, install it from https://www.anaconda.com/download
2. Open a terminal (Linux/Mac), or anaconda-prompt (Windows). Make sure you are in a conda environment: (base) should appear at the left of the input line.
3. (Optional) Create a specific virtual environment. This is useful to avoid version conflicts.

```conda create --name bundling_score_env```

```conda activate bundling_score_env```

At the left of the input line, you should now have (bundling_score_env). You should run the activate command each time you open a new terminal, in order for the module to be available.

4. Make sure pip is available.

```conda install -c anaconda git```
```conda install pip ```

5. Install the module

```pip install bundling_score``` 

### With pip
In the terminal, run

```pip install bundling_score```

## Usage:
### Folder processing
1.	In the terminal, run

```bundling_score```

First run might take a bit of time before printing instructions because of security analysis by the OS.

2.	The program will ask for the location of files that should be analyzed. Write the folder path and press Enter.
Tip: You can copy the path to a folder from the file explorer. On Windows, click at the right of the folder name, at the very top of the explorer. On Mac, right click on the name of the folder, at the very bottom of Finder.
3.	If you want to change the window size (see 3.3), write yes or the desired value (in px) and press Enter.
4.	Files are processed, and results are stored in a csv file (bundling_scores_window_20px.csv)  in the same folder as the images. You can open it in your favorite spreadsheet (Excel, LibreOffice Calc).
5.	Multiply values by the square of the resolution to get the bundling score in μm2.

### Advanced usage
Tutorial notebooks are available on the github repository.
1.	Use the plugin in python scripts. Have a look at the 1. Get started notebook.
2.	Tweak correlation window. The default window size has been chosen for images of size 300 by 300px, with a certain level of noise. If your images are different, you might consider tweaking it. Have a look at the 2. Tweak correlation window size notebook.

