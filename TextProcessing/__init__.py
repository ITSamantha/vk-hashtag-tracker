# -*- coding: utf8 -*-
import inflect
import nltk
import string
import re
import numpy

import TextProcessing.Preprocessing
import TextProcessing.Processing
import TextProcessing.Vectorizing
import TextProcessing.Lemmatization

if __name__ == '__main__':
    text = 'Птицекрылка королевы Александры, или птицекрылка Александры, ' \
           'или птицекрыл королевы Александры, или орнитоптера Александра, ' \
           'или орнитоптера королевы Александры (Ornithoptera alexandrae) — ' \
           'вид дневных бабочек из рода Ornithoptera семейства парусников. ' \
           'Размах крыльев сsffdfdfFDSfdfамцов достигает 14,7—22 см, самок — 18,7—24,8 см, #dianathebest ' \
           'а по некоторым данным даже до 28—30 см. Считается одной из крупнейших по размаху сантиметры сантиметры крыло метр сантим крыльев дневных бабочек в мире сантиметры.'

    text2 = 'Разобраться во всем этом многообразии обычному человеку действительно не просто.' \
            ' Wikimotors постарается вам помочь в этом. ' \
            'Здесь рассматриваются современные и относительно современные двигатели автомобилей, преимущественно бензиновые, ' \
            'но некоторая часть будет отведена под роторные, дизельные и электромоторы.' \
            ' Кроме общего обзора, мы рассмотрим основные проблемы, неисправности, недостатки и конструкционные просчеты моторов,' \
            ' а также, их ремонт, как устранить возникшую неприятность и снова получать удовольствие от ровной работы движка.'





    text3 = 'Кроме общего обзора, мы рассмотрим основные проблемы, неисправности, недостатки и конструкционные просчеты моторов,' \
            ' а также, их ремонт, как устранить возникшую неприятность и снова получать удовольствие от ровной работы движка.'
    text4 = 'Размах крыльев сsffdfdfFDSfdfамцов достигает 14,7—22 см'


#TODO: Не все действия!
    text = TextProcessing.Preprocessing.preprocessing_text(text, 'russian')
    text = TextProcessing.Lemmatization.using_mystem(text)

    l1 = [text, text2]
    l2 = [text3, text4]



    #text = [word for word in text if re.fullmatch(r'[a-zA-ZёЁА-Яа-я\_\-0-9]+', word)]

    matrix1, matrix2 = TextProcessing.Vectorizing.using_TF_IDF(l1, l2)
    print('Matrix1:\n', matrix1)
    print('Matrix2:\n', matrix2)
