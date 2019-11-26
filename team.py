class Team:
  def __init__(self, name, played, wins, fairplayPoints, logo):
    self.name = name
    self.played = played
    self.wins  = wins
    self.losses = played - wins
    self.fairplayPoints = fairplayPoints
    self.points = (3 * wins) + fairplayPoints
    self.logo = logo

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name