import argparse
import neo
import numpy as np
import quantities as pq
import matplotlib.pyplot as plt

from neo.core import (AnalogSignal, Block, Segment)
from utils.parse import parse_string2dict, none_or_float, none_or_int, none_or_str
from utils.neo_utils import analogsignal_to_imagesequence, imagesequence_to_analogsignal, flip_image, rotate_image, time_slice, add_empty_sites_to_analogsignal
from utils.io_utils import write_neo

CLI = argparse.ArgumentParser()
CLI.add_argument("--data", nargs='?', type=str, required=True,
                 help="path to input data directory")
CLI.add_argument("--output", nargs='?', type=str, required=True,
                 help="path of output file")
CLI.add_argument("--sampling_rate", nargs='?', type=none_or_float,
                 default=None, help="sampling rate in KHz")
CLI.add_argument("--spatial_scale", nargs='?', type=float, required=True,
                 help="distance between electrodes or pixels in mm")
CLI.add_argument("--data_name", nargs='?', type=str, default='None',
                 help="chosen name of the dataset")
CLI.add_argument("--annotations", nargs='+', type=none_or_str, default=None,
                 help="metadata of the dataset")
CLI.add_argument("--array_annotations", nargs='+', type=none_or_str,
                 default=None, help="channel-wise metadata")
CLI.add_argument("--array_annotation_file", nargs='?', type=none_or_str,
                 default=None, help="path to channel-wise metadata file")
CLI.add_argument("--kwargs", nargs='+', type=none_or_str, default=None,
                 help="additional optional arguments")
CLI.add_argument("--t_start", nargs='?', type=none_or_float, default=None,
                 help="start time in seconds")
CLI.add_argument("--t_stop", nargs='?', type=none_or_float, default=None,
                 help="stop time in seconds")
CLI.add_argument("--projection", nargs='?', type=str, required=True,
                 help="2D plane on which 3D data has been projected")

if __name__ == '__main__':

    args, unknown = CLI.parse_known_args()

    # Load data - Data shape is (t,z,y)
    
    projected_activity = np.load(args.data)
    
    if len(projected_activity.shape)==2:
        dim_t, dim_channels = projected_activity.shape
        if args.array_annotation_file is not None:
            # For each channel, ordered couple (y,z) of coordinates is provided
            # Here we are using the convention (y,z) <--> (x,y)
            active_channels_coords = np.load(args.array_annotation_file)
            x_coords = active_channels_coords[:,0]
            y_coords = active_channels_coords[:,1]
        print(dim_t, dim_channels, f'Y={np.max(x_coords)}', f'Z={np.max(y_coords)}')
    elif len(projected_activity.shape)==3:
        # For each channel, 2nd coordinate is z, 3rd is y
        # Here we are using the convention (y,z) <--> (x,y)
        dim_t, dim_y, dim_z = projected_activity.shape
        projected_activity = np.reshape(projected_activity, (dim_t, dim_y*dim_z))
        coords = [(y,z) for y in range(dim_y) for z in range(dim_z)]
        x_coords = [y for (y,z) in coords]
        y_coords = [z for (y,z) in coords]
        print(dim_t, dim_z, dim_y, f'Y={np.max(x_coords)}', f'Z={np.max(y_coords)}')

    # Transform data into Analogsignal
    a = AnalogSignal(projected_activity, units='V', \
                     sampling_rate=args.sampling_rate*pq.kHz, \
                     spatial_scale=args.spatial_scale*pq.mm)

    a = time_slice(a, args.t_start, args.t_stop)

    # Annotations
    # kwargs = parse_string2dict(args.kwargs)
    a.annotations.update(parse_string2dict(args.annotations))
    a.annotations.update(spatial_scale=args.spatial_scale*pq.mm)
    a.annotations.update(projection=args.projection)
    a.array_annotations.update(x_coords=x_coords)
    a.array_annotations.update(y_coords=y_coords)

    a = add_empty_sites_to_analogsignal(a)
    
    if a.description is None:
        a.description = ''
    a.description += 'Spike count activity in macro-pixel.'

    # CHECK
    imgseq = analogsignal_to_imagesequence(a)
    #imgseq = flip_image(imgseq, axis=-2) # vertical flip
    #a = imagesequence_to_analogsignal(imgseq)

    # Create the necessary neo structure
    blk = neo.Block(name = args.data_name)
    seg = neo.Segment(name = 'Segment 0', index = 0)
    blk.segments.append(seg)
    blk.segments[0].analogsignals = [a]

    # Write the neo file
    if False:
        # Using NixIO
        writer = neo.io.NixIO("./projected_activity_NIXIO.nix", mode="rw")
        writer.write(blk)
        writer.close()
    if False:
        # Using get_io
        nio = neo.io.get_io(str("./projected_activity_IO.nix"))
        writer.write(blk)
        writer.close()
    if True:
        # Using default Cobrawap function
        write_neo(args.output, blk)
