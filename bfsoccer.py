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
 * ========================================================== 
"""

import datetime
import copy
import logging
from feedutil import FeedUtil
from soccerstatic import bfmarketmap,bfhamarketmap
from bfxmlutil import bf_parse_xml_id,bf_parse_xml,bf_parse_divmap,wom_postprocess

class BfUtil(FeedUtil):  
    def __init__(self,sourceid,url,bftype):
	FeedUtil.__init__(self,sourceid,url)
	self.bftype=bftype
	
    def get_tour_xref(self,inpname):
	myarr=inpname.split("/")
	tour=None
	myarr2=[]
	for menupart in myarr:
	    myarr2.append(menupart)
	    if (self.tourmap.has_key("/".join(myarr2)))==True:
		return self.tourmap["/".join(myarr2)]
	return None

    def process_xml_id(self,idmap,ts=None,filtermap={},inpxml=None):
	retmap={}
	for url in self.urllist:
	    if inpxml==None:
		rawxml=self._fetch_xml(self.get_url_ts(url,ts))
	    else:
		rawxml=inpxml
	    if rawxml==None:
		return None
	    prelmap=self.parse_xml_id(rawxml)
	    retmap=prelmap
	return retmap



    def parse_xml(self,inpxml,idmap=None,filtermap=None):
	if self.bftype=="match":
	    lt_date=datetime.datetime.today()+datetime.timedelta(days=3)
	    gt_date=datetime.datetime.today()
	    calcfiltermap = {"eventdate_lt":lt_date,"eventdate_gt":gt_date}
	    fn_eventgroup = self.get_tour_xref  
	    fn_eventid = self.get_match_eventid
	    fn_betmarket = self.get_match_betmarket  
	    fn_betname = self.get_match_betname	    
	    return bf_parse_xml(True,inpxml,fn_eventgroup,fn_eventid,fn_betmarket,fn_betname,calcfiltermap)

    def parse_xml_id(self,inpxml):
	if self.bftype=="match":
	    lt_date=datetime.datetime.today()+datetime.timedelta(days=3)
	    gt_date=datetime.datetime.today()
	    calcfiltermap = {"eventdate_lt":lt_date,"eventdate_gt":gt_date}
	    fn_eventgroup = self.get_tour_xref  
	    fn_eventid = self.get_match_eventid
	    fn_betmarket = self.get_match_betmarket  
	    fn_betname = self.get_match_betname	    
	    return bf_parse_xml_id(inpxml,fn_eventgroup,fn_eventid,fn_betmarket,fn_betname,calcfiltermap)
          
    def post_process(self,inpmap):
	wom_postprocess(inpmap)
      
      
    def get_match_eventid(self,inpmenupath,datestr):
	tour=self.get_tour_xref(inpmenupath)
	if (tour==None):
	    return None
	else:
	    myarr=inpmenupath.split("/")
	    stopidx=-1
	    matchid=None
	    for idx,menupart in enumerate(myarr):
		if (menupart[:7]=="Fixture"):
		    stopidx=idx
	    if (stopidx!=-1 and len(myarr)>(stopidx+1)) and \
	    len(myarr[stopidx+1].split(" v "))==2:
		team1=myarr[stopidx+1].split(" v ")[0].strip()
		team2=myarr[stopidx+1].split(" v ")[1].strip()
		return tour+"_2010_"+team1+"_"+team2
	    return matchid
	    
    def _teams(self,inpmenupath):
	myarr=inpmenupath.split("/")
	stopidx=-1
	for idx,menupart in enumerate(myarr):
	    if (menupart[:7]=="Fixture"):
		stopidx=idx
	if (stopidx!=-1 and len(myarr)>(stopidx+1)) and \
	len(myarr[stopidx+1].split(" v "))==2:
	    team1=myarr[stopidx+1].split(" v ")[0].strip()
	    team2=myarr[stopidx+1].split(" v ")[1].strip()
	    return (team1,team2)
	return (None,None)
	    
    def get_match_betmarket(self,menupath,bfmarketname):
	if (bfmarketmap.has_key(bfmarketname)==True and bfmarketmap[bfmarketname].has_key("marketname")==True):
	    return bfmarketmap[bfmarketname]["marketname"]
	else:
	    team1,team2 = self._teams(menupath)
	    if team1!=None and team2!=None:
		if team1 in bfmarketname:
		    ha="Home"
		elif team2 in bfmarketname:
		    ha="Away"
		else:
		    return None
	    else:
		return None
	    for key in bfhamarketmap:
		if key in bfmarketname:
		    return ha+bfhamarketmap[key]["marketname"]
	    return None
	    
    def get_match_betname(self,menupath,bfmarketname,bfselectionname,selcount):
	if (bfmarketmap.has_key(bfmarketname)==True and bfmarketmap[bfmarketname].has_key("marketname")==True):
	    return bfmarketmap[bfmarketname]["selectionorder"][selcount]
	else:
	    team1,team2 = self._teams(menupath)
	    if team1!=None and team2!=None:
		if team1 in bfmarketname:
		    ha="Home"
		elif team2 in bfmarketname:
		    ha="Away"
		else:
		    return None
	    else:
		return None
	    for key in bfhamarketmap:
		if key in bfmarketname:
		    return bfhamarketmap[key]["selectionorder"][selcount]
	    return None
	    
    def get_nonmatch_betmarket(self,menupath,bfmarketname):
	if (menupath,bfmarketname) in ltlist:
	    return bfmarketname
	else:
	    return None
	    
    def get_nonmatch_betname(self,menupath,bfmarketname,bfselectionname,selcount):
	return bfselectionname

    def get_nonmatch_eventid(self,inpmenupath,datestr):
	tour=self.get_tour_xref(inpmenupath)
	if (tour ==None):
	    return None
	else:
	    myarr=inpmenupath.split("/")
	    stopidx=-1
	    matchid=None
	    for idx,menupart in enumerate(myarr):
		if (menupart[:7]=="Fixture"):
		    stopidx=idx
	    if (stopidx==-1):
		return "All"
	    else:
		return None


#def bf_parse_xml_id(inpxml,fn_eventgroup,fn_eventid,fn_betmarket,fn_betname,filtermap):
#def bf_parse_xml(bl,inpxml,fn_eventgroup,fn_eventid,fn_betmarket,fn_betname,filtermap):
#def bf_parse_divmap(inpxml,fn_eventgroup,fn_eventid,filtermap):

    



