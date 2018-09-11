#encoding=utf-8
#Author: Tom Qian  
#Email: TomQianMaple@outlook.com


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from classify_image import NodeLookup

import argparse
import os.path
import re
import sys
import tarfile

import numpy as np
from six.moves import urllib
import tensorflow as tf



class ImageRecognizer:
    # method from classify_image.py
    def __create_graph(self):
        """Creates a graph from saved GraphDef file and returns a saver."""
        # Creates graph from saved graph_def.pb.
        with tf.gfile.FastGFile('classify_image_graph_def.pb', 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

    # method from classify_image.py
    def run_inference_on_image(self,imageList,num_top_predictions=5):
        """Runs inference on an image.

        Args:
          image: Image file name.

        Returns:
          Nothing
        """

        for image in imageList:
            if not tf.gfile.Exists(image):
                tf.logging.fatal('File does not exist %s', image)
            image_data = tf.gfile.FastGFile(image, 'rb').read()

            # Creates graph from saved GraphDef.
            self.__create_graph()

            with tf.Session() as sess:
                # Some useful tensors:
                # 'softmax:0': A tensor containing the normalized prediction across
                #   1000 labels.
                # 'pool_3:0': A tensor containing the next-to-last layer containing 2048
                #   float description of the image.
                # 'DecodeJpeg/contents:0': A tensor containing a string providing JPEG
                #   encoding of the image.
                # Runs the softmax tensor by feeding the image_data as input to the graph.
                softmax_tensor = sess.graph.get_tensor_by_name('softmax:0')
                predictions = sess.run(softmax_tensor,
                                       {'DecodeJpeg/contents:0': image_data})
                predictions = np.squeeze(predictions)

                # Creates node ID --> English string lookup.
                node_lookup = NodeLookup()

                top_k = predictions.argsort()[-num_top_predictions:][::-1]
                for node_id in top_k:
                    human_string = node_lookup.id_to_string(node_id)
                    score = predictions[node_id]
                    print('%s (score = %.5f)' % (human_string, score))

if __name__ == '__main__':

    img_reg=ImageRecognizer()
    img_path='https://github.com/bluemapleman/MapleAI/blob/master/ComputerVision/Image%20Recognition/data/';
    meme1=img_path+'test-meme1.jpg'
    meme2=img_path+'test-meme2.jpg'
    image_list=[meme1,meme2]
    img_reg.run_inference_on_image(image_list)