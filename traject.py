class Traject():
    """ This class contains a single 'traject', later used for T in the score function. """

    def __init__(self, connection_list):
        self.connection_list = connection_list

    def minutes(self):
    """ adds up the time of all connections in traject. """
        time = 0
        for connection in self.connection_list:
            time += connection["time"]
        return time

  def add_connection(self, station1, station2, time):
        self.connection_list.append({"station1": station1, "station2": station2, "time": time})
