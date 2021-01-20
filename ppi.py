import webbrowser
import zipfile
def install(repo, path_to_file, extract_path):
    webbrowser.open('https://github.com/ppi-lib/' + repo +'/archive/main.zip')
    with zipfile.ZipFile(path_to_file,  'r') as zip_ref:
        zip_ref.extractall(path_to_file)

def build(about_file, yourname, filename, decrpition):
    form = (yourname + "\n" + filename + "\n" + about_file + " in short " + decrpition)
    print('copy the below sentence\n')
    print('to srinidhithegret01@gmail.com\n')
    print(form)
    webmail=input('Want to send this? First copy the paragraph above')
    if webmail == 'yes':
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=new')

    elif webmail == 'no':
          print("ok")

def easyzip(repo):
    webbrowser.open('https://github.com/ppi-lib/' + repo +'/archive/main.zip')
