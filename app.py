from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

from position import Position
from team import Team

import yaml

def main():
    date = ""
    teams = []
    with open('scores.yaml') as file:
        teamStats = yaml.load(file, Loader=yaml.FullLoader)
        teams.append(Team(teamStats['Hawks'], teamStats['Hawks']['played'], teamStats['Hawks']['wins'], 'resources/teams/hawks.gif'))
        teams.append(Team(teamStats['Falcons'], teamStats['Falcons']['played'], teamStats['Falcons']['wins'], 'resources/teams/falcons.gif'))
        teams.append(Team(teamStats['Eagles'], teamStats['Eagles']['played'], teamStats['Eagles']['wins'], 'resources/teams/eagles.gif'))
        teams.append(Team(teamStats['Cheetahs'], teamStats['Cheetahs']['played'], teamStats['Cheetahs']['wins'], 'resources/teams/cheetahs.gif'))
        teams.append(Team(teamStats['Panthers'], teamStats['Panthers']['played'], teamStats['Panthers']['wins'], 'resources/teams/panthers.gif'))
        teams.append(Team(teamStats['Jaguars'], teamStats['Jaguars']['played'], teamStats['Jaguars']['wins'], 'resources/teams/jaguars.gif'))

        date = teamStats['Date']

    
    # sorting teams by points
    teams.sort(key=lambda x: x.points, reverse=True)
    
    positions = []
    # img 142 | score 145    
    positions.append(Position(1, 220, 320, 360, 480+50, 130))
    positions.append(Position(2, 220, 480, 505, 480+50, 130))
    positions.append(Position(3, 220, 630, 670, 480+50, 130))
    positions.append(Position(4, 220, 770, 820, 480+50, 130))
    positions.append(Position(5, 220, 930, 980, 480+50, 130))
    positions.append(Position(6, 220, 1080, 1125, 480+50, 130))
    
    template = Image.open("resources/template.jpg")
    draw = ImageDraw.Draw(template)
    dateFont = ImageFont.truetype("resources/font.ttf", 32)
    draw.text((810,125), date, (0,0,0), font=dateFont)

    ctr = 0
    for p in positions:
        p.updateScores(teams[ctr].played, teams[ctr].wins, teams[ctr].logo)    
        render(template, draw, p)
        ctr = ctr + 1

    template.save('Table '+date.strip()+'.jpg')

def render(template, draw, pos):
    font = ImageFont.truetype("resources/font.ttf", 36)

    # Logo
    template.paste(Image.open(pos.teamLogo), (pos.logoX, pos.logoY))
    # Scores
    draw.text((pos.playedX, pos.playedY), str(pos.played), (0,0,0), font=font)
    draw.text((pos.winsX, pos.winsY), str(pos.wins), (0,0,0), font=font)
    draw.text((pos.lossesX, pos.lossesY), str(pos.losses), (0,0,0), font=font)
    draw.text((pos.pointsX, pos.pointsY), str(pos.points), (0,0,0), font=font)

if __name__ == "__main__":
    main()