import sys
import numpy as np
import matplotlib.pyplot as plt
import os.path as op
sys.path = ['../lib'] + sys.path
import hw_utils as utils
path = './data/'

def create_pano(
        image_list, ratio_thres,
        canvas_height, canvas_width,
        num_iter, tol, figsize=(20, 20)):
    """
    This function creates a panorama using a list of images.
    Inputs:
        image_list: a list of str, the path to each image (without file extensions).
        ratio_thres: the ratio test threshold in `FindBestMatches`
        canvas_height, canvas_width: The dimension of the canvas
        num_iter: num of iterations of performing RANSAC to find the homography matrix.
        tol: tolerance for keypoint projection
    """
    # Get the matches from `FindBestMatches`
    # xy_src_list: np.array, (matches, 2) in xy format
    # xy_ref_list: np.array, (matches, 2) in xy format
    # im_list: a list of images in np.array
    xy_src_list, xy_ref_list, im_list = utils.PrepareData(
        image_list, ratio_thres)

    # Use the matches to estimate a homography matrix to the ref image frame
    # for each source image. Then project each source image to the reference
    # frame using the homography matrix.
    wrap_list = utils.ProjectImages(
        xy_src_list, xy_ref_list, im_list,
        canvas_height, canvas_width, num_iter, tol)

    # Merge the projected images above
    # Note: the first element is the reference image in warp_list
    result = utils.MergeWarppedImages(
        canvas_height, canvas_width, wrap_list)

    # show the final panorama
    plt.figure(figsize=figsize)
    plt.imshow(result)
    plt.show()


def main():
    canvas_height = 1200     
    canvas_width = 1600

    image_list = ['garden4', 'garden0', 'garden3']
    #image_list = ['fountain4', 'fountain0']
    # image_list = ['irving_out3', 'irving_out6', 'irving_out5']
    # image_list = ['garden_up4', 'garden_up5', 'garden_up6']
    # image_list = ['Rainier1', 'Rainier2', 'Rainier3','Rainier4','Rainier5','Rainier6']

    num_iter = 50
    tol = 3
    ratio_thres = 0.7
    image_list = [op.join(path, im) for im in image_list]
    create_pano(image_list, ratio_thres, canvas_height, canvas_width,
                num_iter, tol, figsize=(20, 20))

def main1():
    canvas_height = 1200     
    canvas_width = 1600

    # image_list = ['garden4', 'garden0', 'garden3']
    image_list = ['fountain4', 'fountain0']
    # image_list = ['irving_out3', 'irving_out6', 'irving_out5']
    # image_list = ['garden_up4', 'garden_up5', 'garden_up6']
    # image_list = ['Rainier1', 'Rainier2', 'Rainier3','Rainier4','Rainier5','Rainier6']

    num_iter = 50
    tol = 5
    ratio_thres = 0.6
    image_list = [op.join(path, im) for im in image_list]
    create_pano(image_list, ratio_thres, canvas_height, canvas_width,
                num_iter, tol, figsize=(20, 20))

def main2():
    canvas_height = 1200     
    canvas_width = 1600

    #image_list = ['garden4', 'garden0', 'garden3']
    #image_list = ['fountain4', 'fountain0']
    image_list = ['irving_out3', 'irving_out6', 'irving_out5']
    # image_list = ['garden_up4', 'garden_up5', 'garden_up6']
    # image_list = ['Rainier1', 'Rainier2', 'Rainier3','Rainier4','Rainier5','Rainier6']

    num_iter = 50
    tol = 3
    ratio_thres = 0.7
    image_list = [op.join(path, im) for im in image_list]
    create_pano(image_list, ratio_thres, canvas_height, canvas_width,
                num_iter, tol, figsize=(20, 20))
    
def main3():
    canvas_height = 1200     
    canvas_width = 1600

    #image_list = ['garden4', 'garden0', 'garden3']
    #image_list = ['fountain4', 'fountain0']
    # image_list = ['irving_out3', 'irving_out6', 'irving_out5']
    image_list = ['garden_up4', 'garden_up5', 'garden_up6']
    # image_list = ['Rainier1', 'Rainier2', 'Rainier3','Rainier4','Rainier5','Rainier6']

    num_iter = 50
    tol = 3
    ratio_thres = 0.7
    image_list = [op.join(path, im) for im in image_list]
    create_pano(image_list, ratio_thres, canvas_height, canvas_width,
                num_iter, tol, figsize=(20, 20))

def main4():
    canvas_height = 1200     
    canvas_width = 1600

    #image_list = ['garden4', 'garden0', 'garden3']
    #image_list = ['fountain4', 'fountain0']
    # image_list = ['irving_out3', 'irving_out6', 'irving_out5']
    # image_list = ['garden_up4', 'garden_up5', 'garden_up6']
    image_list = ['Rainier1', 'Rainier2', 'Rainier3','Rainier4','Rainier5','Rainier6']

    num_iter = 50
    tol = 3
    ratio_thres = 0.7
    image_list = [op.join(path, im) for im in image_list]
    create_pano(image_list, ratio_thres, canvas_height, canvas_width,
                num_iter, tol, figsize=(20, 20))
if __name__ == '__main__':
    #main()
    #main1()
    main2()
    #main3()
    #main4()

