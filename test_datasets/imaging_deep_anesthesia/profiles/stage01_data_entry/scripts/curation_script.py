import numpy as np
import argparse
import neo
import quantities as pq
from utils.parse import parse_string2dict, none_or_float, none_or_str
from utils.neo_utils import imagesequence_to_analogsignal, time_slice
from utils.neo_utils import rotate_image, flip_image
from utils.io_utils import write_neo
import matplotlib.pyplot as plt

CLI = argparse.ArgumentParser()
CLI.add_argument("--data", nargs="?", type=str, required=True,
                 help="path to input data directory")
CLI.add_argument("--output", nargs="?", type=str, required=True,
                 help="path of output file")
CLI.add_argument("--sampling_rate", nargs="?", type=none_or_float,
                 default=None, help="sampling rate in Hz")
CLI.add_argument("--spatial_scale", nargs="?", type=float, required=True,
                 help="distance between electrodes or pixels in mm")
CLI.add_argument("--data_name", nargs="?", type=str, default="None",
                 help="chosen name of the dataset")
CLI.add_argument("--annotations", nargs="+", type=none_or_str, default=None,
                 help="metadata of the dataset")
CLI.add_argument("--array_annotations", nargs="+", type=none_or_str,
                 default=None, help="channel-wise metadata")
CLI.add_argument("--kwargs", nargs="+", type=none_or_str, default=None,
                 help="additional optional arguments")
CLI.add_argument("--t_start", nargs="?", type=none_or_float, default=None,
                 help="start time in seconds")
CLI.add_argument("--t_stop",  nargs="?", type=none_or_float, default=None,
                 help="stop time in seconds")
CLI.add_argument("--orientation_top", nargs="?", type=str, required=True,
                 help="upward orientation of the recorded cortical region")
CLI.add_argument("--orientation_right", nargs="?", type=str, required=True,
                 help="right-facing orientation of the recorded cortical region")

if __name__ == "__main__":
    args, unknown = CLI.parse_known_args()

    # Load optical data
    nio = neo.io.tiffio.TiffIO(directory_path=args.data,
                              sampling_rate=args.sampling_rate*pq.Hz,
                              spatial_scale=args.spatial_scale*pq.mm,
                              units="dimensionless")
    # loading the data flips the images vertically!

    block = nio.read_block()

    # change data orientation to be top=ventral, right=lateral
    imgseq = block.segments[0].imagesequences[0]
    imgseq = flip_image(imgseq, axis=-2) # vertical
    imgseq = rotate_image(imgseq, rotation=-90)
    block.segments[0].imagesequences[0] = imgseq

    # Transform into analogsignals
    asig = imagesequence_to_analogsignal(imgseq)

    asig = time_slice(asig, args.t_start, args.t_stop)

    if args.annotations is not None:
        asig.annotations.update(parse_string2dict(args.annotations))

    asig.annotations.update(orientation_top=args.orientation_top)
    asig.annotations.update(orientation_right=args.orientation_right)

    # # for debugging
    # fig, ax = plt.subplots()
    # ax.imshow(imgseq.as_array()[0], origin="lower")
    # breakpoint()

    # ToDo: add metadata
    block.name = args.data_name
    block.segments[0].name = "Segment 1"
    block.segments[0].description = "Loaded with neo.TiffIO (neo version {}). "\
                                    .format(neo.__version__)
    if asig.description is None:
        asig.description = ""
    asig.description += "Ca+ imaging signal. "
    block.segments[0].analogsignals = [asig]

    # Save data
    write_neo(args.output, block)
