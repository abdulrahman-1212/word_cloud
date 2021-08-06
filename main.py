import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def _upload():
    _upload_widget = fileupload.FileUploadWidget()
    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename

        print('Uploaded `{}` ({:.2f} kB)'.format(filename, len(decoded.read()) / 2 **10))

        file_contents = decoded.getvalue()
        _upload_widget.observe(_cb, names='data')
        display(_upload_widget)
        _upload()
FileUploadWidget(label='Browse', _dom_classes=('widget_item', 'btn-group'))


def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too"]

    non_puncuation = ''
    clean_words = []
    frequencies = {}

    for char in file_contents:
        if char not in punctuations:
            non_puncuation += char
        
    words = non_puncuation.split(' ')
    for word in words:
        if word not in uninteresting_words:
            clean_words.append(word)

    for word in clean_words:
        if word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1
    
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

my_image = calculate_frequencies(file_contents)
plt.imshow(my_image, interpolation = 'nearest')
plt.axis('off')
plt.show()


