# ssi4onnx
**S**imple **S**hape **I**nference tool for **ONNX**.


https://github.com/PINTO0309/simple-onnx-processing-tools

[![Downloads](https://static.pepy.tech/personalized-badge/ssi4onnx?period=total&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/ssi4onnx) ![GitHub](https://img.shields.io/github/license/PINTO0309/ssi4onnx?color=2BAF2B) [![PyPI](https://img.shields.io/pypi/v/ssi4onnx?color=2BAF2B)](https://pypi.org/project/ssi4onnx/) [![CodeQL](https://github.com/PINTO0309/ssi4onnx/workflows/CodeQL/badge.svg)](https://github.com/PINTO0309/ssi4onnx/actions?query=workflow%3ACodeQL)

<p align="center">
  <img src="https://user-images.githubusercontent.com/33194443/170158744-69bfdb6a-e032-4ed9-982c-ee9ac8889022.png" />
</p>

## 1. Setup
### 1-1. HostPC
```bash
### option
$ echo export PATH="~/.local/bin:$PATH" >> ~/.bashrc \
&& source ~/.bashrc

### run
$ pip install -U onnx \
&& python3 -m pip install -U onnx_graphsurgeon --index-url https://pypi.ngc.nvidia.com \
&& pip install -U ssi4onnx
```
### 1-2. Docker
https://github.com/PINTO0309/simple-onnx-processing-tools#docker

## 2. CLI Usage
```
$ ssi4onnx -h

usage:
    ssi4onnx [-h]
    -if INPUT_ONNX_FILE_PATH
    [-of OUTPUT_ONNX_FILE_PATH]
    [-n]

optional arguments:
  -h, --help
        show this help message and exit.

  -if INPUT_ONNX_FILE_PATH, --input_onnx_file_path INPUT_ONNX_FILE_PATH
        Input onnx file path.

  -of OUTPUT_ONNX_FILE_PATH, --output_onnx_file_path OUTPUT_ONNX_FILE_PATH
        Output onnx file path.

  -n, --non_verbose
        Do not show all information logs. Only error logs are displayed.
```

## 3. In-script Usage
```python
>>> from ssi4onnx import shape_inference
>>> help(shape_inference)

Help on function shape_inference in module ssi4onnx.onnx_shape_inference:

shape_inference(
    input_onnx_file_path: Union[str, NoneType] = '',
    onnx_graph: Union[onnx.onnx_ml_pb2.ModelProto, NoneType] = None,
    output_onnx_file_path: Union[str, NoneType] = '',
    non_verbose: Union[bool, NoneType] = False
) -> onnx.onnx_ml_pb2.ModelProto

    Parameters
    ----------
    input_onnx_file_path: Optional[str]
        Input onnx file path.
        Either input_onnx_file_path or onnx_graph must be specified.
        Default: ''

    onnx_graph: Optional[onnx.ModelProto]
        onnx.ModelProto.
        Either input_onnx_file_path or onnx_graph must be specified.
        onnx_graph If specified, ignore input_onnx_file_path and process onnx_graph.

    output_onnx_file_path: Optional[str]
        Output onnx file path. If not specified, no ONNX file is output.
        Default: ''

    non_verbose: Optional[bool]
        Do not show all information logs. Only error logs are displayed.
        Default: False

    Returns
    -------
    estimated_graph: onnx.ModelProto
        Shape estimated onnx ModelProto.
```

## 4. CLI Execution
```bash
$ ssi4onnx --input_onnx_file_path nanodet_320x320.onnx
```

## 5. In-script Execution
```python
from ssi4onnx import shape_inference

estimated_graph = shape_inference(
    input_onnx_file_path="crestereo_init_iter2_120x160.onnx",
)
```

## 6. Sample
### Before
![image](https://user-images.githubusercontent.com/33194443/169821344-f3560cfe-476f-4480-9c76-8c71476ebb57.png)

### After
![image](https://user-images.githubusercontent.com/33194443/169821518-bb58ea27-37d7-42d7-84c6-0e40c522760e.png)

## 7. Reference
1. https://github.com/onnx/onnx/blob/main/docs/Operators.md
2. https://docs.nvidia.com/deeplearning/tensorrt/onnx-graphsurgeon/docs/index.html
3. https://github.com/NVIDIA/TensorRT/tree/main/tools/onnx-graphsurgeon
4. https://github.com/PINTO0309/simple-onnx-processing-tools
5. https://github.com/PINTO0309/PINTO_model_zoo

## 8. Issues
https://github.com/PINTO0309/simple-onnx-processing-tools/issues
