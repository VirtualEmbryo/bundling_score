#import bundling_score.bundling_score as bs
import sys
import os
import pandas as pd
from skimage import io
import platform
import bundling_score.bundling_score as bs


def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def main():
    print("Currently in " + os.getcwd())
    test = False
    while not test:
        print("Enter source folder")
        source_dir = input()
        if not os.path.isdir(source_dir):
            print("Folder does not exist, retry")
        else:
            test = True

    test = False
    while not test:
        print("\nWindow size is 20px, do you want to change it?")
        print("See notebook for more details. (y/n/value)")
        answer = input()
        if answer in ['y', 'yes', 'Yes', 'YES', 'Y']:
            print("Enter window size (px)")
            try:
                smax = int(input())
                test = True
                print(f'Window size set to {smax}px.')
            except ValueError:
                print("Window size has to be an integer.")
        elif answer in ['n', 'N', 'no', 'No', 'NO']:
            smax = 20
            test = True
            print('Keeping 20px')
        else:
            try:
                smax = int(answer)
                test = True
                print(f'Window size set to {smax}px.')
            except ValueError:
                test = False

    ic = io.MultiImage(os.path.join(source_dir, '*.tif'), dtype=float)

    print(f"\n{len(ic)} files detected. Processing (this can be long...)")

    # Bundling scores will be stored in a DataFrame
    df = pd.DataFrame()

    for i, timelapse in enumerate(ic):
        # Get only the name of the file
        name = ic.files[i][len(source_dir):-4]
        print(f"Processing {name}.")

        # Load ROI and crop
        timelapse = timelapse.astype(float)

        # Single image
        if len(timelapse.shape) == 2:
            scores = [bs.compute_score(timelapse, smax=smax)]

        # Timelapse
        elif len(timelapse.shape) == 3:
            scores = []
            for j in range(timelapse.shape[0]):
                scores.append(bs.compute_score(timelapse[j, ...], smax=smax))
        else:
            print(f"File {name} is neither timelapse nor image, skipping")

        # Header is the name of the tif file
        series = pd.Series(scores, name=name)
        # Add to the main dataframe
        df = pd.concat((df, series), axis=1)

    save_path = os.path.join(source_dir,
                             f'bundling_scores_window_{smax}px.csv')
    df.to_csv(save_path)

    print('\nSuccess! Data are stored in ' + save_path)
    print('Remember to multiply by the square of the resolution!')


if __name__ == "__main__":
    main()
