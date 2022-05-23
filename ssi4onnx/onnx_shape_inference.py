#! /usr/bin/env python

import sys
import onnx
import onnx_graphsurgeon as gs
from typing import Optional
from argparse import ArgumentParser

class Color:
    BLACK          = '\033[30m'
    RED            = '\033[31m'
    GREEN          = '\033[32m'
    YELLOW         = '\033[33m'
    BLUE           = '\033[34m'
    MAGENTA        = '\033[35m'
    CYAN           = '\033[36m'
    WHITE          = '\033[37m'
    COLOR_DEFAULT  = '\033[39m'
    BOLD           = '\033[1m'
    UNDERLINE      = '\033[4m'
    INVISIBLE      = '\033[08m'
    REVERCE        = '\033[07m'
    BG_BLACK       = '\033[40m'
    BG_RED         = '\033[41m'
    BG_GREEN       = '\033[42m'
    BG_YELLOW      = '\033[43m'
    BG_BLUE        = '\033[44m'
    BG_MAGENTA     = '\033[45m'
    BG_CYAN        = '\033[46m'
    BG_WHITE       = '\033[47m'
    BG_DEFAULT     = '\033[49m'
    RESET          = '\033[0m'


def shape_inference(
    input_onnx_file_path: Optional[str] = '',
    onnx_graph: Optional[onnx.ModelProto] = None,
    output_onnx_file_path: Optional[str] = '',
    non_verbose: Optional[bool] = False,
) -> onnx.ModelProto:
    """

    Parameters
    ----------
    input_onnx_file_path: Optional[str]
        Input onnx file path.\n\
        Either input_onnx_file_path or onnx_graph must be specified.\n\
        Default: ''

    onnx_graph: Optional[onnx.ModelProto]
        onnx.ModelProto.\n\
        Either input_onnx_file_path or onnx_graph must be specified.\n\
        onnx_graph If specified, ignore input_onnx_file_path and process onnx_graph.

    output_onnx_file_path: Optional[str]
        Output onnx file path. If not specified, no ONNX file is output.\n\
        Default: ''

    non_verbose: Optional[bool]
        Do not show all information logs. Only error logs are displayed.\n\
        Default: False

    Returns
    -------
    estimated_graph: onnx.ModelProto
        Shape estimated onnx ModelProto.
    """

    # Unspecified check for input_onnx_file_path and onnx_graph
    if not input_onnx_file_path and not onnx_graph:
        print(
            f'{Color.RED}ERROR:{Color.RESET} '+
            f'One of input_onnx_file_path or onnx_graph must be specified.'
        )
        sys.exit(1)

    # Loading Graphs
    # onnx_graph If specified, onnx_graph is processed first
    if not onnx_graph:
        onnx_graph = onnx.load(input_onnx_file_path)
    graph = gs.import_onnx(onnx_graph)
    graph.cleanup().toposort()

    # Shape Estimation
    estimated_graph = None
    try:
        estimated_graph = onnx.shape_inference.infer_shapes(gs.export_onnx(graph))
    except:
        estimated_graph = gs.export_onnx(graph)
        if not non_verbose:
            print(
                f'{Color.YELLOW}WARNING:{Color.RESET} '+
                'The input shape of the next OP does not match the output shape. '+
                'Be sure to open the .onnx file to verify the certainty of the geometry.'
            )

    # Save
    if output_onnx_file_path:
        onnx.save(estimated_graph, output_onnx_file_path)

    if not non_verbose:
        print(f'{Color.GREEN}INFO:{Color.RESET} Finish!')

    # Return
    return estimated_graph


def main():
    parser = ArgumentParser()
    parser.add_argument(
        '--input_onnx_file_path',
        type=str,
        required=True,
        help='Input onnx file path.'
    )
    parser.add_argument(
        '--output_onnx_file_path',
        type=str,
        default='',
        help='Output onnx file path.'
    )
    parser.add_argument(
        '--non_verbose',
        action='store_true',
        help='Do not show all information logs. Only error logs are displayed.'
    )
    args = parser.parse_args()

    input_onnx_file_path = args.input_onnx_file_path
    output_onnx_file_path = args.output_onnx_file_path
    non_verbose = args.non_verbose

    if not output_onnx_file_path:
        output_onnx_file_path = input_onnx_file_path

    # Load
    onnx_graph = onnx.load(input_onnx_file_path)

    # OP add
    estimated_graph = shape_inference(
        input_onnx_file_path=None,
        onnx_graph=onnx_graph,
        output_onnx_file_path=output_onnx_file_path,
        non_verbose=non_verbose,
    )


if __name__ == '__main__':
    main()