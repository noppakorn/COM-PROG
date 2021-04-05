import glob
import time
start = time.time()
errors = []
file_in = 'stressgene.png'
print('----------Case 1----------')
print('Testing embeding text file and reading it back')
for txt in glob.glob('*.txt'):
    print('********',txt)
    rtxt = open(txt).read()
    try :
        assert embed_text_to_image(rtxt,file_in,'%s_%s.png' % (file_in[:-4],txt[:-4])) == True
        get = get_embedded_text_from_image('%s_%s.png' % (file_in[:-4],txt[:-4]))
        if txt == 'disclaimer.txt' :print(get)
        assert get == rtxt
    except: 
        errors.append('Case 1 : ' + txt)
print('----------Case 2----------')
print('Testing not large enough images')
file_in = '5x5_none0.png'
for txt in glob.glob('*.txt'):
    print('********',txt)
    rtxt = open(txt).read()
    try :
        assert embed_text_to_image(rtxt,file_in,'%s_%s.png' % (file_in[:-4],txt[:-4])) != True 
    except: 
        errors.append('Case 2 : ' + txt)
print('---------------------------------------------------------\nReport :')
if len(errors) > 0 :
    print('Errors : ') 
    for i in errors : print(i)
else : print('All tests passes! Say Thanks!')
print('Execution Time :',time.time()-start, 'seconds')
