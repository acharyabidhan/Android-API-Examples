from kivy.clock import mainthread
from plyer import gps
from kivy.app import App
from kivy.utils import platform
from kivy.lang import Builder
from kivy.properties import StringProperty
from android.permissions import request_permissions, Permission

KV = """
GridLayout:
    rows:2
    Label:
        text:app.gps_location
        font_size:self.width/8
    ToggleButton:
        text:"Start" if self.state == "normal" else "Stop"
        font_size:self.width/8
        on_state:app.startGPS() if self.state == "down" else app.stopGPS()
"""

class GpsTest(App):
    gps_location = StringProperty()
    def build(self):
        try:gps.configure(on_location=self.onLocation,on_status=self.onStatus)
        except:print("GPS not available")
        if platform == "android":self.askForPermission()
        else:print("This is not Android")
        return Builder.load_string(KV)
    
    def callback(self, permissions, results):
        if all([res for res in results]):
            print("Callback: All permissions granted.")
        else:print("Callback: Some permissions refused.")
        print("Permissions:", permissions)

    def askForPermission(self):
        request_permissions(
            [Permission.ACCESS_COARSE_LOCATION,
            Permission.ACCESS_FINE_LOCATION],
            self.callback)

    def startGPS(self):
        gps.start(1, 1)

    def stopGPS(self):
        gps.stop()

    @mainthread
    def onLocation(self, **kwargs):
        self.gps_location = "\n".join(["{}={}".format(v, d) for v, d in kwargs.items()])

    def onStatus(self, stype, status):
        pass

if __name__ == '__main__':
    GpsTest().run()