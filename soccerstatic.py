"""
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

import os


completetourmap={
    #"CL-No1":{"shortname":"Nor Tlge"},
    #"CL-US":{"shortname":"US MLS"},
    #"CL-Ir1":{"shortname":"Irish Prem"},
    "ICC-ECL":{"shortname":"EUFA Champ Lge",
    "xref":{"pinnacle":'UEFA CL',"bf":"UEFA Champions League"}},
    "ICC-EL":{"shortname":"EUFA Europa Lge",
    "xref":{"bf":"UEFA Europa League"}},
    #"CL-Sw1":{"shortname":"Swed Allsv"},
    "CL-En0":{"shortname":"Eng Prem",
    "xref":{"pin":'Eng. Premier',
    "bf":"English Soccer/Barclays Premier League"}},
    #"CL-En1":{"shortname":"Eng Champ",
    #"xref":{"pinnacle": 'Eng. Chship'}},
    #"CL-En2":{"shortname":"Eng Lge 1"},
    #"CL-En3":{"shortname":"Eng Lge 2"},
    "CL-Fr1":{"shortname":"Fr Lge 1",
    "xref":{"pin":'French 1',"bf":"French Soccer/Ligue 1 Orange"}},
    "CL-D1":{"shortname":"Ger Bund",
    "xref":{"pin":'Bundesliga',"bf":"German Soccer/Bundesliga 1"}},
    "CL-I1":{"shortname":"Itl Serie A",
    "xref":{"pin":'Serie A',"bf":"Italian Soccer/Serie A"}},
    "CL-SP1":{"shortname":"Spain Primera","bf":"Spanish Soccer/Primera Division"}  
  }
  


completeteammap={
"Birmingham":{'xref': {'twitterht': '#BCFC', 'fd': '', 'pin': 'Birmingham City'}},
"Bolton":{'xref': {'twitterht': '#BWFC', 'fd': '', 'pin': 'Bolton Wanderers'}},
"Blackburn":{'xref': {'twitterht': '#BRFC', 'fd': '', 'pin': 'Blackburn Rovers'}},
"West Ham":{'xref': {'twitterht': '#WHUFC', 'fd': '', 'pin': 'West Ham United'}},
"Wolves":{'xref': {'twitterht': '#WWFC', 'fd': '', 'pin': 'Wolverhampton Wanderers'}},
"Stoke":{'xref': {'twitterht': '#SCFC', 'fd': '', 'pin': 'Stoke City'}},
"Newcastle":{'xref': {'twitterht': '#NUFC', 'fd': '', 'pin': 'Newcastle United'}},
"Tottenham":{'xref': {'twitterht': '#THFC', 'fd': '', 'pin': 'Tottenham Hotspur'}},
"Man City":{'xref': {'twitterht': '#MCFC', 'fd': '', 'pin': 'Manchester City'}},
'Osasuna': {'xref': {'twitterht': '#OSA', 'fd': '', 'pin': 'Osasuna'}}, 
'Chievo': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Chievo'}}, 
'Real Madrid': {'xref': {'twitterht': '#MAD', 'fd': '', 'pin': 'Real Madrid'}}, 
'Bologna': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Bologna'}}, 
'Stuttgart': {'xref': {'twitterht': '#VfB', 'fd':'', 'pin': 'VfB Stuttgart'}}, 
'Aston Villa': {'xref': {'twitterht': '#AVFC', 'fd': '', 'pin': 'Aston Villa'}}, 
'Man Utd': {'xref': {'twitterht': '#MUFC', 'fd':'','pin': 'Manchester United'}}, 
'Hoffenheim': {'xref': {'twitterht': '#TSG', 'fd':'','pin': 'TSG Hoffenheim'}}, 
'Nurnberg': {'xref': {'twitterht': '#FCN', 'fd': '', 'pin': 'N_rnberg'}}, 
'Valencia': {'xref': {'twitterht': '#VAL', 'fd': '', 'pin': 'Valencia'}}, 
'Mallorca': {'xref': {'twitterht': '#MLL', 'fd': '', 'pin': 'Mallorca'}}, 
'Schalke': {'xref': {'twitterht': '#S04', 'fd': '','pin':'Schalke 04'}}, 
'AC Milan': {'xref': {'twitterht': '', 'fd': '', 'pin': 'AC Milan'}}, 
'Udinese': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Udinese'}}, 
'Zaragoza': {'xref': {'twitterht': '#ZAR', 'fd': ''}}, 
'W Bremen': {'xref': {'twitterht': '#WERDER', 'fd': '','pin':'Werder Bremen'}}, 
'Liverpool': {'xref': {'twitterht': '#LFC', 'fd': '', 'pin': 'Liverpool'}}, 
'Wolfsburg': {'xref': {'twitterht': '#VfL', 'fd': '','pin':'VfL Wolfsburg'}}, 
'B Munich': {'xref': {'twitterht': '#FCB', 'fd': '','pin':'Bayern M_nchen'}}, 
'Ath Bilbao': {'xref': {'twitterht': '#ATH', 'fd': ''}}, 
'Lecce': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Lecce'}}, 
'Cesena': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Cesena'}}, 
'Atl Madrid': {'xref': {'twitterht': '#ATL', 'fd': ''}}, 
'Leverkusen': {'xref': {'twitterht': '#BAYER', 'fd': '','pin':'Bayer Leverkusen'}}, 
'Fulham': {'xref': {'twitterht': '#FFC', 'fd': '', 'pin': 'Fulham'}}, 
'Gijon': {'xref': {'twitterht': '#SPO', 'fd': ''}}, 
'Santander': {'xref': {'twitterht': '#RAC', 'fd': ''}}, 
'Everton': {'xref': {'twitterht': '#EFC', 'fd': '', 'pin': 'Everton'}}, 
'Inter': {'xref': {'twitterht': '', 'fd': '','pin':'Inter Milan'}}, 
'Espanyol': {'xref': {'twitterht': '#ESP', 'fd': '', 'pin': 'Espanyol'}}, 
'Cagliari': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Cagliari'}}, 
'Fiorentina': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Fiorentina'}}, 
'Dortmund': {'xref': {'twitterht': '#BVB', 'fd': '','pin':'Borussia Dortmund'}}, 
'Palermo': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Palermo'}}, 
'Hannover': {'xref': {'twitterht': '#H96', 'fd': '','pin':'Hannover 96'}}, 
'Deportivo': {'xref': {'twitterht': '#DEP', 'fd': ''}}, 
'Napoli': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Napoli'}}, 
'Lazio': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Lazio'}}, 
'Hamburg': {'xref': {'twitterht': '#HSV', 'fd': '','pin':'Hamburger SV'}}, 
'Kaiserslautern': {'xref': {'twitterht': '#FCK', 'fd': '', 'pin': 'Kaiserslautern'}}, 
'Barcelona': {'xref': {'twitterht': '#BAR', 'fd': '', 'pin': 'Barcelona'}}, 
'Getafe': {'xref': {'twitterht': '#GET', 'fd': '', 'pin': 'Getafe'}}, 
'Catania': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Catania'}}, 
'St Pauli': {'xref': {'twitterht': '#FCSP', 'fd': '','pin':'FC St. Pauli'}}, 
'Juventus': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Juventus'}}, 
'Roma': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Roma'}}, 
'Freiburg': {'xref': {'twitterht': '#SCF', 'fd': '', 'pin': 'Freiburg'}}, 
'Genoa': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Genoa'}}, 
'Chelsea': {'xref': {'twitterht': '#CFC', 'fd': '', 'pin': 'Chelsea'}}, 
'Levante': {'xref': {'twitterht': '#LEV', 'fd': '', 'pin': 'Levante'}}, 
'Brescia': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Brescia'}}, 
'Hercules': {'xref': {'twitterht': '#HER', 'fd': ''}}, 
'Mainz': {'xref': {'twitterht': '#FSV', 'fd': '','pin':'FSV Mainz 05'}}, 
'Blackpool': {'xref': {'twitterht': '#BPFC', 'fd': '', 'pin': 'Blackpool'}}, 
'Frankfurt': {'xref': {'twitterht': '#EINTRACHT', 'fd': '','pin':'Eintracht Frankfurt'}}, 
'Malaga': {'xref': {'twitterht': '#MGA', 'fd': ''}}, 
'Sampdoria': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Sampdoria'}}, 
'FC Koln': {'xref': {'twitterht': '#KOELN', 'fd': '','pin':'FC K_ln'}}, 
'Sevilla': {'xref': {'twitterht': '#SEV', 'fd': '', 'pin': 'Sevilla'}}, 
'Arsenal': {'xref': {'twitterht': '#AFC', 'fd': '', 'pin': 'Arsenal'}}, 
'Parma': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Parma'}}, 
'Mgladbach': {'xref': {'twitterht': '#BMG', 'fd': '','pin':'Borussia M_nchengladbach'}}, 
'Villarreal': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Villarreal'}}, 
'Sunderland': {'xref': {'twitterht': '#SAFC', 'fd': '', 'pin': 'Sunderland'}}, 
'Wigan': {'xref': {'twitterht': '#WAFC', 'fd': '','pin':'Wigan Athletic'}}, 
'Sociedad': {'xref': {'twitterht': '#SOC', 'fd': ''}}, 
'Bari': {'xref': {'twitterht': '', 'fd': '', 'pin': 'Bari'}}, 
'West Brom': {'xref': {'twitterht': '#WBAFC', 'fd': '', 'pin': 'West Brom'}}, 
'Almeria': {'xref': {'twitterht': '#ALM', 'fd': '', 'pin': 'Almeria'}}}


#newmap={}
#for key in completeammap:
#    newmap[key]=completematchmap[key]
#    if key in list1:
#	newmap[key]["xref"]["pin"]=key
#print newmap


ltlist=[
('English Soccer/Npower League Two', 'Winner 2010/11'), 
('English Soccer/Npower League Two', 'Promotion 2010/11'), 
('English Soccer/Npower League Two', 'Top Gscorer 2010/11'), 
('English Soccer/Npower League One', 'Top Gscorer 2010/11'), 
('English Soccer/Npower League One', 'Winner 2010/11'), 
('English Soccer/Npower League One', 'Promotion 2010/11'), 
('English Soccer/Npower League One', 'Relegation 2010/11'), 
('English Soccer/The Championship', 'Top Gscorer 2010/11'), 
('English Soccer/The Championship', 'Handicap Win 2010/11'), 
('English Soccer/The Championship', 'Winner 2010/11'), 
('English Soccer/The Championship', 'Promotion 2010/11'), 
('English Soccer/The Championship', 'Top 6 Finish 2010/11'), 
('English Soccer/The Championship', 'Relegation 2010/11'), 
('English Soccer/Barclays Premier League', 'Relegation 2010/11'), 
('English Soccer/Barclays Premier League', 'Winner/Top GS 2010/11'), 
('English Soccer/Barclays Premier League', 'Best of Rest 2010/11'), 
('English Soccer/Barclays Premier League', 'Top Gscorer 2010/11'), 
('English Soccer/Barclays Premier League', 'Top 2 Finish 2010/11'), 
('English Soccer/Barclays Premier League', 'Top Gscorer - Top 4'), 
('English Soccer/Barclays Premier League', 'Top English Gscorer'), 
('English Soccer/Barclays Premier League', 'Top 4 Finish 2010/11'), 
('English Soccer/Barclays Premier League', 'Winner 2010/11'), 
('English Soccer/Barclays Premier League', 'Top 6 Finish 2010/11'), 
('English Soccer/Barclays Premier League', 'Top 3 Finish 2010/11'), 
('English Soccer/Barclays Premier League', 'Handicap Win 2010/11'), 
('English Soccer/Barclays Premier League', 'Top 10 Finish 2010/11'), 
('English Soccer/Barclays Premier League', 'Straight Forecast'), 
('English Soccer/Barclays Premier League/Head to Head Leagues', 'Top London Club'), 
('English Soccer/Barclays Premier League/Head to Head Leagues', 'Top Midlands Club'), ('English Soccer/Barclays Premier League/Head to Head Leagues', 'Top Northwest Club'), ('English Soccer/Barclays Premier League/Season Match Bets', 'Everton v Liverpool'), 
('UEFA Europa League', 'Winner 2010/11'), 
('UEFA Champions League', 'Winner 2010/11'), 
('UEFA Champions League', 'Top Goalscorer 10/11'), 
('UEFA Champions League', 'Winning Nation'), 
('UEFA Champions League', 'To Reach The Final'), 
('UEFA Champions League', 'Spanish Progress'), 
('German Soccer/Bundesliga 1', 'Top 3 Finish 2010/11'), 
('German Soccer/Bundesliga 1', 'Top Gscorer 2010/11'), 
('German Soccer/Bundesliga 1', 'Winner 2010/11'), 
('Italian Soccer/Serie A', 'Top Gscorer 2010/11'), 
('Italian Soccer/Serie A', 'Top 4 Finish 2010/11'), 
('Italian Soccer/Serie A', 'Relegation 2010/11'), 
('Italian Soccer/Serie A', 'Winner 2010/11'), 
('Spanish Soccer/Primera Division', 'Relegation 2010/11'), 
('Spanish Soccer/Primera Division', 'Top Gscorer 2010/11'), 
('Spanish Soccer/Primera Division', 'Winner 2010/11'), 
('Spanish Soccer/Primera Division', 'Top 4 Finish 2010/11'), 
('English Soccer/Carling Cup', 'Winner 2010/11')]


bfmarketmap={"Over/Under 5.5 Goals":
{"marketname": "OU55",
"selectionorder": ["U55", "O55"]},
"Over/Under 2.5 Goals":
{"marketname": "OU25",
"selectionorder": ["U25", "O25"]},
"Match Odds":
{"marketname": "FT",
"selectionorder": ["Home", "Away", "Draw"]},
"DRAW NO BET":
{"marketname": "DNB",
"selectionorder": ["Home", "Away"]},
"Correct Score":
{"marketname": "CS",
"selectionorder": ["00", "01", "02", "03", "10", "11", "12", "13", "20", "21", "22", "23", "30", "31", "32", "33", "Other"]}, "Over/Under 4.5 Goals": {"marketname": "OU45", "selectionorder": ["U45", "O45"]}, "Over/Under 1.5 Goals": {"marketname": "OU15", "selectionorder": ["U15", "O15"]}, "Over/Under 3.5 Goals": {"marketname": "OU35", "selectionorder": ["U35", "O35"]},
"First Half Goals": {"marketname": "OUHT15", "selectionorder": ["U15", "O15"]},
"Half Time/Full Time": {"marketname": "HTFT", "selectionorder":
			["HomeHome", "HomeDraw", "HomeAway", "DrawHome", "DrawDraw", "DrawAway", "AwayHome", "AwayDraw", "AwayAway"]},
"Over/Under 6.5 Goals": {"marketname": "OU65", "selectionorder": ["U65", "O65"]},
"Half Time": {"marketname": "HT", "selectionorder": ["Home", "Away", "Draw"]}}

bfhamarketmap={
"Win Both Halves":
{"marketname": "Wbh",
"selectionorder": ["Yes", "No"]},
"Win to Nil":
{"marketname": "Wtn",
"selectionorder": ["Yes", "No"]},
"Clean Sheet?":
{"marketname": "Csh",
"selectionorder": ["Yes", "No"]},
"To Score in Both Halves?":
{"marketname": "Sbh",
"selectionorder": ["Yes", "No"]},
"Win a Half?":
{"marketname": "Wah",
"selectionorder": ["Yes", "No"]},
"Win from Behind":
{"marketname": "Wfb",
"selectionorder": ["Yes", "No"]},
  }
  
def get_team_xref(teamname,xref_name):
    if completeteammap.has_key(teamname)==False:
	return teamname
    elif completeteammap[teamname].has_key("xref")==False:
	return teamname
    elif completeteammap[teamname]["xref"].has_key(xref_name)==False:
	return teamname
    else:
	if len(completeteammap[teamname]["xref"][xref_name])>0:
	    return completeteammap[teamname]["xref"][xref_name]
	else:
	    return teamname
