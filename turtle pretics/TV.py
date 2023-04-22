class TV:
    power=True
    channel=1
    volume=16
    def info(self):
        print('Power : %s'% self.power)
        print('Channel : %d'%self.channel)
        print('Volume : %d'% self.volume)
    def on_off(self):
        if self.power==True:
            self.power=False
            print('Turn Off')
            self.power=True
            print('Turn On')
        else:
            self.power=True
            print('Turn On')
            self.power=False
            print('Turn Off')
    def set_channel(self,n):
        self.channel=n
    def set_volume(self,n):
        self.volume=n
tv=TV()
tv.info()
tv.on_off()
tv.set_channel(5)
tv.set_volume(20)