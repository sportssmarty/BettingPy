/* ==========================================================
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
 * ========================================================== */
import os

def parse_xml_id(inpxml,fn_eventgroup,fn_eventid,fn_betmarket,fn_betname,filtermap):
    retmap={}
    eventlist = inpxml.split("<event");   
    for myevent in eventlist[1:]:
	eventarr=myevent.split(">")[0].split('"')
	menupath=eventarr[1]
	eventdatestr=eventarr[3]
	datearr=eventdatestr.split("/")
	eventdatestr = eventarr[3]
	eventgroup = fn_eventgroup(menupath)
	eventid = fn_eventid(menupath,eventdatestr)
	mto=0
	eventdatetimestr=""
	eventdatestr=""
	if ((eventgroup!=None) and (eventid!=None)):
	    subeventlist=myevent.split("<subevent")       
	    eventdate=None
	    tempeventmap={}
	    for subevent in subeventlist[1:]:
		titlearr=subevent.split(">")[0].split('"')
		if eventdate==None and len(titlearr[5])>0:
		    try:
			timearr=titlearr[5].split(":")
			eventdatestr=datearr[2]+datearr[1]+datearr[0]
			tempeventmap["datestr"]=eventdatestr
			eventdate = datetime.datetime(int(datearr[2]),
			int(datearr[1]),int(datearr[0]),int(timearr[0]),int(timearr[1]))
		    except:
			eventdate=None
		bfmarketname=titlearr[1]
		betmarket=fn_betmarket(menupath,bfmarketname)
		betmarket_matchedamt=int(titlearr[9])
		if (betmarket!=None and (
		(filtermap.has_key("betmarket_matchedamt")==False) or
		(betmarket_matchedamt>filtermap["betmarket_matchedamt"]))):
		    
		    tempeventmap[betmarket]=titlearr[7]
		    selectionlist=subevent.split("<selection")
		    for idx,selection in enumerate(selectionlist[1:]):
			selectionarr=selection.split('>')[0].split('"')
			bfselectionname=selectionarr[1]           
			betname=fn_betname(menupath,bfmarketname,bfselectionname,idx)
			if (betname!=None):
			    tempeventmap[betmarket]=selectionarr[3]
			    
	    if eventdate!=None and ((filtermap.has_key("eventdate_lt")==False) or (eventdate<filtermap["eventdate_lt"])) and \
	    ((filtermap.has_key("eventdate_gt")==False) or (eventdate>filtermap["eventdate_gt"])):
		if len(tempeventmap)>0:
		    if retmap.has_key(eventid)==False:
			retmap[eventid]={"bf":{}}
		    for key,value in tempeventmap.items():
			if key=="datestr":
			    retmap[eventid][key]=value
			else:
			    retmap[eventid]["bf"][key]=value
    return retmap



def bf_parse_divmap(inpxml,fn_eventgroup,fn_eventid,filtermap):
    retmap={}
    eventlist = inpxml.split("<event");   
    for myevent in eventlist[1:]:
	eventarr=myevent.split(">")[0].split('"')
	menupath=eventarr[1]
	eventdatestr=eventarr[3]
	datearr=eventdatestr.split("/")
	eventdatestr = eventarr[3]
	eventgroup = fn_eventgroup(menupath)
	eventid = fn_eventid(menupath,eventdatestr)
	if ((eventgroup!=None) and (eventid!=None)):
	    subeventlist=myevent.split("<subevent")       
	    eventdate=None
	    mto=0
	    eventdatetimestr=None
	    for subevent in subeventlist[1:]:
		titlearr=subevent.split(">")[0].split('"')
		if eventdate==None and len(titlearr[5])>0:
		    try:
			timearr=titlearr[5].split(":")
			eventdatetimestr=datearr[2]+datearr[1]+datearr[0]+"-"+titlearr[5]
			eventdate = datetime.datetime(int(datearr[2]),
			int(datearr[1]),int(datearr[0]),int(timearr[0]),int(timearr[1]))
			if filtermap.has_key("eventdate_gt")==True:
			    mto=((eventdate-filtermap["eventdate_gt"]).days)*24*60+((eventdate-filtermap["eventdate_gt"]).seconds)/60
		    except:
			eventdate=None
	    if eventdate!=None and ((filtermap.has_key("eventdate_lt")==False) or (eventdate<filtermap["eventdate_lt"])) and \
	    ((filtermap.has_key("eventdate_gt")==False) or (eventdate>filtermap["eventdate_gt"])):
		if retmap.has_key(eventgroup)==False:
		    retmap[eventgroup]=[]
		if eventid not in retmap[eventgroup]:
		    retmap[eventgroup].append({"eventid":eventid,
		    "eventdatetimestr":eventdatetimestr,"mto":mto})
    return retmap


def bf_parse_xml(bl,inpxml,fn_eventgroup,fn_eventid,fn_betmarket,fn_betname,filtermap):
    retmap={}
    eventlist = inpxml.split("<event");   
    depth_list=["1","2","3"]
    os_list=["o","a"]
    if (bl==True):
	bl_list=["b","l"]
    else:
	bl_list=["b"]
    for myevent in eventlist[1:]:
	eventarr=myevent.split(">")[0].split('"')
	menupath=eventarr[1]
	eventdatestr=eventarr[3]
	datearr=eventdatestr.split("/")
	eventdatestr = eventarr[3]
	eventgroup = fn_eventgroup(menupath)
	eventid = fn_eventid(menupath,eventdatestr)
	mto=0
	eventdatetimestr=""
	eventdatestr=""
	if ((eventgroup!=None) and (eventid!=None)):
	    keystub=eventgroup+"#"+eventid+"#"
	    subeventlist=myevent.split("<subevent")       
	    eventdate=None
	    tempeventmap={"mto":0}
	    bfmnl=[]
	    for subevent in subeventlist[1:]:
		titlearr=subevent.split(">")[0].split('"')
		if eventdate==None and len(titlearr[5])>0:
		    try:
			timearr=titlearr[5].split(":")
			eventdatetimestr=datearr[2]+datearr[1]+datearr[0]+"-"+titlearr[5]
			eventdatestr=datearr[2]+datearr[1]+datearr[0]
			eventdate = datetime.datetime(int(datearr[2]),
			int(datearr[1]),int(datearr[0]),int(timearr[0]),int(timearr[1]))
			if filtermap.has_key("eventdate_gt")==True:
			    tempeventmap["mto"]=((eventdate-filtermap["eventdate_gt"]).days)*24*60+((eventdate-filtermap["eventdate_gt"]).seconds)/60

		    except:
			eventdate=None
		bfmarketname=titlearr[1]
		bfmnl.append(bfmarketname)
		betmarket=fn_betmarket(menupath,bfmarketname)
		betmarket_matchedamt=int(titlearr[9])
		if (betmarket!=None and (
		(filtermap.has_key("betmarket_matchedamt")==False) or
		(betmarket_matchedamt>filtermap["betmarket_matchedamt"]))):
		    tempeventmap[keystub+betmarket+"#bf_id"]=titlearr[7]
		    tempeventmap[keystub+betmarket+"#bf_id"]=titlearr[7]
		    tempeventmap[keystub+betmarket+"#bf_datestr"]=eventdatestr
		    tempeventmap[keystub+betmarket+"#bf_timestr"]=titlearr[5]
		    tempeventmap[keystub+betmarket+"#bf_matchedamt"]=betmarket_matchedamt
		    selectionlist=subevent.split("<selection")
		    for idx,selection in enumerate(selectionlist[1:]):
			selectionarr=selection.split('>')[0].split('"')
			bfselectionname=selectionarr[1]           
			betname=fn_betname(menupath,bfmarketname,bfselectionname,idx)
			if (betname!=None):
			    tempeventmap[keystub+betmarket+"_"+betname+"#bf_id"]=selectionarr[3]
			    rowcount=3       
			    for depth in depth_list:
				for bl in bl_list:
				    for oddsamt in os_list:
					rowcount=rowcount+2
					oddsName=betmarket+"_"+betname+"#bf_"+bl+oddsamt+depth
					odds=float(selectionarr[rowcount].replace(",",""))
					tempeventmap[keystub+oddsName]=odds
	    if eventdate!=None and ((filtermap.has_key("eventdate_lt")==False) or (eventdate<filtermap["eventdate_lt"])) and \
	    ((filtermap.has_key("eventdate_gt")==False) or (eventdate>filtermap["eventdate_gt"])):
		if len(tempeventmap)>0:
		    if retmap.has_key(eventgroup)==False:
			retmap[eventgroup]={}
		    if retmap[eventgroup].has_key(eventid)==False:
			retmap[eventgroup][eventid]={}
		    for key,value in tempeventmap.items():
			retmap[eventgroup][eventid][key]=value
    return retmap
