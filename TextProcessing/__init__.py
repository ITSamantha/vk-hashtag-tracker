# -*- coding: utf8 -*-
import inflect
import nltk
import string
import re
import numpy

import Preprocessing
import Processing

if __name__ == '__main__':
     text = 'Птицекрылка королевы Александры, или птицекрылка Александры, ' \
            'или птицекрыл королевы Александры, или орнитоптера Александра, ' \
        'или орнитоптера королевы Александры (Ornithoptera alexandrae) — ' \
          'вид дневных бабочек из рода Ornithoptera семейства парусников. ' \
            'Размах крыльев самцов достигает 14,7—22 см, самок — 18,7—24,8 см, #dianathebest ' \
          'а по некоторым данным даже до 28—30 см. Считается одной из крупнейших по размаху сантиметры сантиметры крыло метр сантим крыльев дневных бабочек в мире сантиметры.'

     print(Processing.get_keywords(text, 'russian'))