from peak.events import trellis

class Viewer(trellis.Component):
    model = trellis.attr(None)
    @trellis.perform
    def view_it(self):
        if self.model is not None:
            print self.model
            
view = Viewer(model=q2)
Rectangle((0, 99), (20, 30), (20, 129))