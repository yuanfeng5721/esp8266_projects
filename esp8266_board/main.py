import ledflash
import network
import subscribe

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('boboo123', 'w2395721k')
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())
        return True
    else:
        print('network config:', wlan.ifconfig())
        return True
   
    return False

if __name__ == "__main__":
    if do_connect():
        subscribe.main()
    print('network error!')
    