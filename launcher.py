import argparse
import os

from ezlib.trailstacker import StarTrailMaster
from ezlib.imgfio import save_img
from ezlib.logging import set_default_logger,get_default_logger

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("dirname", help="dir of images")
    arg_parser.add_argument("--fade-in", type=float, default=0.1)
    arg_parser.add_argument("--fade-out", type=float, default=0.1)
    arg_parser.add_argument("--int-weight", action="store_true")
    arg_parser.add_argument("--jpg-quality", type=int, default=90)
    arg_parser.add_argument("--png-compressing", type=int, default=1)
    arg_parser.add_argument("--output", type=str)
    args = arg_parser.parse_args()

    dir_name = args.dirname
    fin_ratio, fout_ratio = float(args.fade_in), float(args.fade_out)
    output_file = args.output

    set_default_logger(debug_mode=True, work_mode="backend")
    logger = get_default_logger()
    logger.start()

    # get filename list in the directory
    img_files = os.listdir(dir_name)
    img_files.sort()
    img_files = [os.path.join(dir_name, x) for x in img_files]
    
    ## TODO!!! 16bit TIFF => bad result
    res = StarTrailMaster(img_files,
                          fin_ratio=fin_ratio,
                          fout_ratio=fout_ratio,
                          int_weight=args.int_weight)
    save_img(output_file,
             res,
             png_compressing=args.png_compressing,
             jpg_quality=args.jpg_quality)
    
    logger.stop()