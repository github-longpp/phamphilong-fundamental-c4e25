from random import *
import ex11_and_12

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    
    return  [
                shapes[randint(0,3)]["text"].upper(),
                shapes[randint(0,3)]["color"],
                randint(0,1)
    ]
def mouse_press(x, y, text, color, quiz_type):
    for  sha in shapes:
        if quiz_type == 1:
            if sha['text'] == text.lower():
                click = ex11_and_12.is_inside([x, y], sha['rect'])
        else:
            if sha['color'] == color:
                click = ex11_and_12.is_inside([x, y], sha['rect'])
        print(sha['text'], text.lower())
        print(click)
    return click


