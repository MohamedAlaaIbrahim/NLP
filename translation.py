from deep_translator import GoogleTranslator
import pandas as pd
arabic_test = pd.read_csv("empatheticdialogues/processed_train_2.csv", index_col=[0])
i = 0
for x in arabic_test.index:
    #print(i)
    print(x)
    try:
        translated_text = GoogleTranslator(source='auto', target='ar').translate(arabic_test['Text'][x])
        translated_response = GoogleTranslator(source='auto', target='ar').translate(arabic_test['Response'][x])
        translated_context = GoogleTranslator(source='auto', target='ar').translate(arabic_test['Context'][x])
        arabic_test['Text'][x] = translated_text
        arabic_test['Response'][x] = translated_response
        arabic_test['Context'][x] = translated_context
        i = i + 1
    except:
        arabic_test['Text'][x] = 'Error'
        arabic_test['Response'][x] = 'Error'
        arabic_test['Context'][x] = 'Error'
        i = i + 1
        print('Error')

arabic_test.to_csv("empatheticdialogues/processed_train_4_translated.csv")