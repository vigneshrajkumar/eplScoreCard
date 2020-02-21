class Team:
  def __init__(self, name, played, wins, logo):
    self.name = name
    self.played = played
    self.wins  = wins
    self.losses = played - wins
    self.points = (3 * wins)
    self.logo = logo

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name