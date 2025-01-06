import os

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = (
    "1"  # Transformers uses .isin for a simple op, which is not supported on MPS
)
os.environ["OMP_NUM_THREADS"] = "1"

# import logging
# import warnings

# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger('PIL').setLevel(logging.DEBUG)

from pathlib import Path

from marker.config.parser import ConfigParser
from marker.config.printer import CustomClickPrinter
from marker.converters.pdf import PdfConverter
from marker.logger import configure_logging
from marker.models import create_model_dict
from marker.output import save_output

configure_logging()

root = r"D:\.notes2\tasks\stitching\papaer2"


def converter_demo():
    models = create_model_dict()

    converter = PdfConverter(artifact_dict=models)
    files = [f.name for f in Path(root).iterdir() if f.is_file()]
    for file in files:
        print(f"Converting {file}")
        rendered = converter(os.path.join(root, file))

        name = Path(file).stem
        dirname = os.path.join(root, name)

        os.makedirs(dirname, exist_ok=True)
        save_output(rendered, dirname, name)


if __name__ == "__main__":
    converter_demo()
