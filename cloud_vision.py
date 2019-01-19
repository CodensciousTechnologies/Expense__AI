import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./api_key.json"
#  use your own api_key.json
import argparse
import io
import re

# [START vision_fulltext_detection]
def detect_document(path):
    text = ''
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_document_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            text += '\n' 
            #print()

            for paragraph in block.paragraphs:
                text += '\n'
                #print()

                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    text += ' '
                    #print(" ",end="")

                    for symbol in word.symbols:
                        text += symbol.text
                        #print(symbol.text,end="")
    return text
    # [END vision_python_migration_document_text_detection]
# [END vision_fulltext_detection]

print(detect_document("./1.jpg"))
