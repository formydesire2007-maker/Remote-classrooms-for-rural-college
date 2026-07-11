"""
Common Helper Functions
"""

import os
import uuid
from datetime import datetime



def generate_filename(filename):

    """
    Creates a unique filename
    """

    extension = filename.split(".")[-1]


    new_name = (

        str(uuid.uuid4())

        + "."

        + extension

    )


    return new_name





def save_file(file, folder):

    """
    Save uploaded files safely
    """

    if not os.path.exists(folder):

        os.makedirs(folder)


    filename = generate_filename(
        file.filename
    )


    path = os.path.join(

        folder,

        filename

    )


    file.save(path)


    return path





def get_current_time():

    """
    Returns current timestamp
    """

    return datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )





def clean_text(text):

    """
    Removes unwanted spaces
    """

    if not text:

        return ""


    return " ".join(
        text.split()
    )





def limit_history(history, limit=20):

    """
    Keeps chatbot history limited
    """

    if len(history) > limit:

        return history[-limit:]


    return history