import time
def main():
    #initalize battery
    battery=100
    current_mode=""
    last_mode=""   #stores the last mode
    is_pluggedin=True  #  laptop is plugged in initially
    while battery>=0:
          current_mode=""
          if is_pluggedin:
           current_mode="Plugged in performance mode :6000RPM\n"
          else:
            if battery>=80:
                current_mode=f"Performance mode:6000RPM,battery left {battery}%\n"
            elif battery>=40:
                current_mode=f"Balanced mode:4000RPM,battery left {battery}%\n"
            elif battery>=20:
                current_mode=f"Whisper mode:2000RPM,battery left {battery}% consider plugging in\n"
            else:
                current_mode=f"Shutting down {battery}% left"

            #print the mode only if currentmode!=lastmode
          if current_mode!= last_mode:
           print(current_mode,end="")
          last_mode=current_mode  #update the last mode with current mode

        #unplugg the laptop when battery level reach to 80
          if battery==80:
           is_pluggedin=False
           print("On battery!! unplugged")
        #simulate battery drain
          time.sleep(2)
          battery-=20

if __name__=="__main__":
    main()
                

