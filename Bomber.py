#// Don't forget to hit SUBSCRIBE, COMMENT, LIKE, SHARE! and LEARN... :)
# But srsly, hit that sub button so you don't miss out on more content! 


'''imports'''
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


 def banner(): 
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ Made by Danny-Cro ]+]+]+')
    print(bcolors.GREEN + '''
                   
                                                            _:_
                                                    '-.-'
                                           ()      __.'.__
                                        .-:--:-.  |_______|
                                 ()      \____/    \=====/
                                 /\      {====}     )___(
                      (\=,      //\\      )__(     /_____\
      __    |'-'-'|  //  .\    (    )    /____\     |   |
     /  \   |_____| (( \_  \    )__(      |  |      |   |
     \__/    |===|   ))  `\_)  /____\     |  |      |   |
    /____\   |   |  (/     \    |  |      |  |      |   |
     |  |    |   |   | _.-'|    |  |      |  |      |   |
     |__|    )___(    )___(    /____\    /____\    /_____\
    (====)  (=====)  (=====)  (======)  (======)  (=======)
    }===={  }====={  }====={  }======{  }======{  }======={
jgs(______)(_______)(_______)(________)(________)(_________) ' ' ')


class Email_Bomber:
    count = 0

 def __init__(self):
     try:
         print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]')
         self.target = str(input(bcolors.RED + 'Enter target email <: '))
         self.mode = str(input(bcolors.RED + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4: (custom) <: '))
         if int(self.mode) > int(4) or int(self.mode) < int(1): 
             print('ERROR: Sei un pezzo di merda. GoodBye. ')
             sys.exit(1)
    except Exception as e:
        print(f'ERROR: {e}')

 def bomb(self):
     try:                  
        print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
        self.amount = None

        







