class Position:
  def __init__(self, position, logoX, logoY, playedX, playedY, offset):
    self.position = position

    self.logoX = logoX
    self.logoY = logoY

    self.playedX = playedY
    self.playedY = playedX

    self.winsX = playedY + offset
    self.winsY = playedX

    self.lossesX = playedY + (2 * offset)
    self.lossesY = playedX

    self.pointsX = playedY + (3 * offset)
    self.pointsY = playedX
    
    self.teamLogo = ""
    self.played = 0
    self.wins  = 0
    self.losses = 0
    self.points = 0
  
  def updateScores(self, played, wins, logo):
      self.played = played
      self.wins = wins
      self.losses = played - wins
      self.points = (wins * 3)
      self.teamLogo = logo

