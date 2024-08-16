import PIL
from io import BytesIO

import PIL.Image
from boto_handler import read_file, write_file


def reduce_size(input_bucket: str, input_file_path: str, output_bucket: str) -> None:
    image = read_file(input_bucket=input_bucket, input_file_path=input_file_path)
    pil_img = PIL.Image.open(image)

    pil_img = pil_img.resize(160, 300)

    pil_img_resized = BytesIO()
    pil_img.save(pil_img_resized, format=pil_img.format)
    pil_img_resized.seek(0)

    write_file(
        output_bucket=output_bucket, file_path=input_file_path, file_obj=pil_img_resized
    )
