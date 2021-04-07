import glob
import time
import difflib
import sys
line = 59
cfn = open(__file__).readlines()[:line]
ofn = open('original.py').readlines()[:line]
id_name = cfn[1].strip().split()
print('-------------------------------------------')
try :
    print('Name:',id_name[2],id_name[3])
except:
    print("Please add exec(open('%s').read()) to the end of your code" % __file__[-15:])
    print('Then run you code not this file!!')
    sys.exit(0)
id = id_name[1]
print('ID:',id)
if len(id) != 10 :
    print('----- Check your id -----')
    sys.exit()
print('Please Check if your information is correct')
print('-------------------------------------------')
time.sleep(3)
diff = difflib.context_diff(cfn[2:],ofn[2:])
sys.stdout.writelines(diff)
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
print('-------------------------------------------')
print(' '.join(id_name[1:]))
print('Report:')
if len(errors) > 0 :
    print('Errors : ') 
    for i in errors : print(i)
else : print('All tests passes! Say Thanks!')
print('Execution Time :',time.time()-start, 'seconds')