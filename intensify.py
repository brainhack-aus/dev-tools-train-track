from dipy.io.image import load_nifti, save_nifti
import click


@click.command()
@click.argument('in_file')
@click.argument('out_file')
@click.option('--scalar', default=10.0, help="The amount to scale the image by")
@click.option('--offset', default=10.0, help="The amount to offset the image by")
def intensify_image(in_file, out_file, scalar, offset):
    # load image from nifti
    data, affine, img = load_nifti(in_file, return_img=True)
    # scale image
    scaled_data = modulate_image(data, scalar, offset)
    # save image back to file
    save_nifti(out_file, scaled_data, affine)
    print(f'scaled image written to {out_file}')


def modulate_image(image_data, x, y):
    return image_data * x + y + 'bad-value'


if __name__ == '__main__':
    intensify_image()
    # intensify_image('/Users/tclose/.dipy/sherbrooke_3shell/HARDI193.nii.gz',
    #                 '/Users/tclose/Desktop/scaled-image.nii.gz',
    #                 1.0)
    