from peak.events import trellis

class TempConverter(trellis.Component):
    F = trellis.maintain(
        lambda self: self.C * 1.8 + 32,
        initially = 32
    )
    C = trellis.maintain(
        lambda self: (self.F - 32)/1.8,
        initially = 0
    )
    
    @trellis.perform
    def show_values(self):
        print "Celsius......", self.C
        print "Fahrenheit...", self.F

print "... Starting"
tc = TempConverter(C=100)
print "... F = 32"
tc.F = 32
print "... C = -40"
tc.C = -40
