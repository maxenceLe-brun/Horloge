from time import*
from datetime import*
#easy : this code is the simplest of the program, because a module already exist at this time
#       that use the actual time of the computer
"""
def easy():
    hour = str(datetime.now())[11:19]
    while True:
        if str(datetime.now())[11:19] != hour:
            hour = str(datetime.now())[11:19]
            print(hour)
"""

def hour():
    """
    
    Parameters
    ----------
    None

    Returns
    -------
    None.
    
    Actions
    -------
    Print the exact time of your computer

    """
    
    hh = int(str(datetime.now())[11:13])
    mm = int(str(datetime.now())[14:16])
    ss = int(str(datetime.now())[17:19])
    
    while True:
        HH,MM,SS = str(hh),str(mm),str(ss)
        h = [hh,mm,ss]
        H = [HH,MM,SS]
        if len(str(hh)) + len(str(mm)) + len(str(ss)) != 6:
            for a in range(3):
                H[a] = str(h[a])
                if len(str(h[a])) == 1:
                    H[a] = "0" + str(h[a])
            print(H[0]+":"+H[1]+":"+H[2])
            
        else:
            print(str(hh)+":"+str(mm)+":"+str(ss))
            
        sleep(0.995)
        
        ss += 1
        if ss == 60:
            mm += 1
            ss = 0
        if mm == 60:
            hh += 1
            mm = 0
        if hh == 24:
            hh = 0

def clock(hh, mm, ss):
    """

    Parameters
    ----------
    hh : int
        Hour of your own time
    mm : int
        Min of your own time
    ss : int
        Sec of your own time

    Returns
    -------
    None.
    
    Actions
    -------
    print the time that the guest asked till he manually stops the program
    
    """
    
    while True:
        HH,MM,SS = str(hh),str(mm),str(ss)
        h = [hh,mm,ss]
        H = [HH,MM,SS]
        
        if len(str(hh)) + len(str(mm)) + len(str(ss)) != 6:
            for a in range(3):
                H[a] = str(h[a])
                if len(str(h[a])) == 1:
                    H[a] = "0" + str(h[a])
            print(H[0]+":"+H[1]+":"+H[2])
        else:
            print(str(hh)+":"+str(mm)+":"+str(ss))
            
        sleep(0.995)
        
        ss += 1
        if ss == 60:
            mm += 1
            ss = 0
        if mm == 60:
            hh += 1
            mm = 0
        if hh == 24:
            hh = 0

def alarm(ho, mn, sc):
    """

    Parameters
    ----------
    ho : int
        The hour of the alarm
    mn : int
        the minute of the alarm
    sc : int
        the second of the alarm
    
    Returns
    -------
    None
    
    Actions
    -------
    Start the time at the exact same as your computer, and will print the time
    Once the time is the same as the alarm selected by the guest, it will print
    "Time's over", and continue to print the time until the guest stops it
    
    """
    
    hh = int(str(datetime.now())[11:13])
    mm = int(str(datetime.now())[14:16])
    ss = int(str(datetime.now())[17:19])
    
    while True:
        HH,MM,SS = str(hh),str(mm),str(ss)
        h = [hh,mm,ss]
        H = [HH,MM,SS]
        
        if len(str(hh)) + len(str(mm)) + len(str(ss)) != 6:
            for a in range(3):
                H[a] = str(h[a])
                if len(str(h[a])) == 1:
                    H[a] = "0" + str(h[a])
            print(H[0]+":"+H[1]+":"+H[2])
        else:
            print(str(hh)+":"+str(mm)+":"+str(ss))
        
        if hh == ho and mm == mn and ss == sc:
            print("Time's over!")
        
        sleep(0.995)
        
        ss += 1
        if ss == 60:
            mm += 1
            ss = 0
        if mm == 60:
            hh += 1
            mm = 0
        if hh == 24:
            hh = 0

def AM_PM(timer):
    """

    Parameters
    ----------
    timer : int
        timer will only take "12" and "24" as an answear, else, it will ask
        you to leave

    Returns
    -------
    None.
    
    """
    
    if timer == 12:
        
        hh = int(str(datetime.now())[11:13])
        mm = int(str(datetime.now())[14:16])
        ss = int(str(datetime.now())[17:19])
        
        tell = hh//12
        hh = (hh-1)%12+1
        ampm = ["AM","PM"]
        
        while True:
            HH,MM,SS = str(hh),str(mm),str(ss)
            h = [hh,mm,ss]
            H = [HH,MM,SS]
            if len(str(hh)) + len(str(mm)) + len(str(ss)) != 6:
                for a in range(3):
                    H[a] = str(h[a])
                    if len(str(h[a])) == 1:
                        H[a] = "0" + str(h[a])
                
                print(H[0]+":"+H[1]+":"+H[2]+ampm[tell%2])
            else:
                print(str(hh)+":"+str(mm)+":"+str(ss)+ampm[tell%2])
            
            sleep(0.995)
            
            ss += 1
            if ss == 60:
                mm += 1
                ss = 0
            if mm == 60:
                hh += 1
                mm = 0
            if hh == 12 and mm == 0 and ss == 0:
                tell +=1
            if hh == 13:
                hh = 1
    elif timer == 24:
        hour()
    else:
        return "Please, pass your way"
