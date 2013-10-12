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
import datetime
import logging

def getdiv(matchid):
    return matchid.split("_")[0]


def getseason(matchid):
    return matchid.split("_")[1]


def get_matchstr_from_matchid(matchid):
    myarr=matchid.split("_")
    return myarr[2] +" v "+myarr[3]

def get_betmarket_from_oddskey(oddskey):
    try:
	return oddskey.split("#")[2].split("_")[0]
    except:
	return None

def get_sourceoddstype_from_oddskey(oddskey):
    try:
	return oddskey.split("#")[3]
    except:
	return None


def gethometeam(matchid):
    return matchid.split("_")[2]


def getawayteam(matchid):
    return matchid.split("_")[3]


def getdate(matchid):
    datestr=matchid.split("_")[-1]                
    year1 = int(datestr.split("/")[0])
    month1 = int(datestr.split("/")[1])
    day1 = int(datestr.split("/")[2])
    return datetime.datetime(year1,month1,day1)


def getdatestr(matchid):                    
    myarr=matchid.split("_")[-1].split("/")
    myres=myarr[2]+"-"+myarr[1]+"-"+myarr[0][2:]
    return myres 


def getdmstr(matchid):                    
    myarr=matchid.split("_")[-1].split("/")
    myres=myarr[2]+"-"+myarr[1]
    return myres 

#matchid#FT_Home#bf_lo1;

def get_match_teams(matchid):
    oddskeyarr=matchid.split("_")
    if len(oddskeyarr)==4:
	return (oddskeyarr[2],oddskeyarr[3])
    else:
	return (None,None)

def match_voddskey(matchstr,matchid):
    team1,team2 = get_match_teams(matchid)
    matchkeyarr=matchstr.split(" v ")
    if team1!=None and team2!=None and len(matchkeyarr)==2:
	if len(matchkeyarr[0])<=len(team1) and len(matchkeyarr[1])<=len(team2):
	    if team1[:len(matchkeyarr[0])].lower()==matchkeyarr[0].lower() and \
	    team2[:len(matchkeyarr[1])].lower()==matchkeyarr[1].lower():
		return True
    return False

def get_atc_key(key_pattern,inpvalue):
    currentvalue=inpvalue
    for idx,item in enumerate(key_pattern):
	if idx%2==1:
	    action=key_pattern[idx-1]
	    position=int(key_pattern[idx])
	    currentvalue=currentvalue.split(action)[position]
    return currentvalue


def match_oddskey(pattern,key):
    if (len(pattern.split("#"))!=len(key.split("#"))):
	return False
    else:
	match_list=[]
	for item in [pattern,key]:
	    match_list.append([])
	    for outersplit in item.split("#"):
		if len(outersplit.split("_"))==2:
		    match_list[-1].append(outersplit.split("_"))
		else:
		    match_list[-1].append([outersplit,outersplit])
	for idx,item in enumerate(match_list[0]):
	    if len(item)==2:
		if (item==match_list[1][idx]) or (item[0]=="any" and item[1]=="any") or \
		(item[0]=="any" and item[1]==match_list[1][idx][1]) or \
		(item[1]=="any" and item[0]==match_list[1][idx][0]):
		    pass
		else:
		    return False
	    else:
		if (item==match_list[1][idx]) or (item[0]=="any"):
		    pass
		else:
		    return False
	  
    return True

	

def get_fu(self,matchid,ha):
    try:
	myret=None
	hot_odds=self.get_odds(matchid,"Match Odds;Home")
	awt_odds=self.get_odds(matchid,"Match Odds;Away")
	if hot_odds!=None and awt_odds!=None:
	    if ha=="h" and hot_odds<awt_odds:
		myret="Fav"
	    elif ha=="h" and hot_odds>=awt_odds:
		myret="Underdog"
	    elif ha=="a" and hot_odds<awt_odds:
		myret="Underdog"
	    elif ha=="a" and hot_odds>=awt_odds:
		myret="Fav"
    except:
	myret=None
    return myret


def get_ap_midha(self,matchid,matchidrecord, ha,htft):
    try:
	if ha=="h":
	    if matchidrecord["hot_"+htft]>matchidrecord["awt_"+htft]:
		myret=3
	    elif matchidrecord["hot_"+htft]==matchidrecord["awt_"+htft]:
		myret=1
	    else:
		myret=0
	else:
	    if matchidrecord["hot_"+htft]>matchidrecord["awt_"+htft]:
		myret=0
	    elif matchidrecord["hot_"+htft]==matchidrecord["awt_"+htft]:
		myret=1
	    else:
		myret=3
    except:
	myret=None
    return myret


def get_ep_midha(self,matchid,ha,htft):
    if htft=="ft":
	betmarket="Match Odds"
    else:
	betmarket="Half Time"
    try:
	if ha=="h":
	    myret=3.0/float(self.get_odds(matchid,betmarket+";Home")) + \
	    1.0/float(self.get_odds(matchid,betmarket+";Draw"))
	else:
	    myret=3.0/float(self.get_odds(matchid,betmarket+";Away")) + \
	    1.0/float(self.get_odds(matchid,betmarket+";Draw"))
    except:
	myret=None
    return myret
        

def get_goals_midha(self,matchid,ha,htft,returnmatchid=False):
    if ha=="h":
	teamfor,teamag=int(self.cache["gamemap"][matchid]["hot_"+htft]),int(self.cache["gamemap"][matchid]["awt_"+htft]) 
    else:
	teamfor,teamag=int(self.cache["gamemap"][matchid]["awt_"+htft]),int(self.cache["gamemap"][matchid]["hot_"+htft])            
    if returnmatchid==False:
	return (teamfor,teamag)
    else:
	return (teamfor,teamag,matchid)
