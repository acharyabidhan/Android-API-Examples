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
    ToggleButton:
        text:"Start" if self.state == "normal" else "Stop"
        on_state:app.startGPS() if self.state == "down" else app.stopGPS()
"""

class GpsTest(App):
    gps_location = StringProperty()
    def build(self):
        try:gps.configure(on_location=self.onLocation,on_status=self.onStatus)
        except:pass
        if platform == "android":self.askForPermission()
        else:pass
        return Builder.load_string(KV)
    
    def callback(self, permissions, results):
        pass

    def askForPermission(self):
        request_permissions(
            [Permission.ACCESS_COARSE_LOCATION,
            Permission.ACCESS_FINE_LOCATION],
            self.callback)

    def startGPS(self):
        gps.start(100, 1)

    def stopGPS(self):
        gps.stop()

    def onLocation(self, **kwargs):
        try:
            print("Latitude:",kwargs["lat"])
            print("Longitude:",kwargs["lon"])
            print("Speed:",kwargs["speed"])
            print("Bearing:",kwargs["bearing"])
            print("Altitude:",kwargs["altitude"])
            print("Accuracy:",kwargs["accuracy"])
        except:pass
        self.gps_location = "\n".join(["{}={}".format(v, d) for v, d in kwargs.items()])

    def onStatus(self, stype, status):
        pass

if __name__ == '__main__':
    GpsTest().run()