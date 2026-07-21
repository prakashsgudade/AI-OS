from datetime import datetime

def think(question, name):

    question = question.lower().strip()

    if question == "hello":

        return f"Hello {name}"

    elif question == "time":

        return datetime.now().strftime("%I:%M %p")

    elif question == "date":

        return datetime.now().strftime("%d-%m-%Y")

    elif question == "tum kaun ho":

        return "Main AI OS hoon."

    elif question == "bye":

        return "Bye."

    else:

        return "Ye feature abhi develop ho raha hai."
    
