from peak.events import trellis
class DistanceConverter(trellis.Component):

    kilometers = trellis.maintain(
        lambda self: self.miles / 0.621371,
        initially = 1
    )
    miles = trellis.maintain(
        lambda self: (self.kilometers * 0.621371),
        initially = 0.621371
    )

    @trellis.perform
    def show_values(self):
        print self.kilometers, "km\n", self.miles, " miles\n---------------------------"
