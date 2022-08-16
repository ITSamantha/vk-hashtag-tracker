import inflect
import nltk
import string
import re
import numpy

from Processing import create_tree_entities

if __name__ == '__main__':
    text = 'Птицекрылка королевы Александры, или птицекрылка Александры, или птицекрыл королевы Александры, или орнитоптера Александра, или орнитоптера королевы Александры (Ornithoptera alexandrae) — вид дневных бабочек из рода Ornithoptera семейства парусников. Размах крыльев самцов достигает 14,7—22 см, самок — 18,7—24,8 см, а по некоторым данным даже до 28—30 см. Считается одной из крупнейших по размаху крыльев дневных бабочек в мире.'
    print(create_tree_entities(text))