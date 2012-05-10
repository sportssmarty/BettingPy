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
from soccerstatic import completetourmap,completeteammap
from matchidutil import getdiv,get_match_teams
import types
import logging
runenv="gae"

if runenv=="gae":
    from google.appengine.api import urlfetch
else:
    pass
  

class FeedUtil(object):
    def __init__(self,sourceid,url):
	self.sourceid=sourceid
	self.tourmap={}
	for key in completetourmap:
	    if completetourmap[key].has_key("xref") and completetourmap[key]["xref"].has_key(sourceid)==True:
		self.tourmap[completetourmap[key]["xref"][sourceid]]=key
	self.teammap={}
	for key in completeteammap:
	    if completeteammap[key].has_key("xref") and completeteammap[key]["xref"].has_key(sourceid)==True:
		self.teammap[completeteammap[key]["xref"][sourceid]]=key
	if type(url)==types.ListType:
	    self.urllist=url
	else:
	    self.urllist=[url]
	self.feedts=None
	    
    @staticmethod
    def get_xml_tag(inpxml,tagname):
	try:
	    return inpxml.split("<"+tagname+">")[1].split("</"+tagname+">")[0]
	except:
	    return None
	    
    @staticmethod
    def match_teams(inpbfmap,inpdatestr,inpteam1,inpteam2,xrefteam1,xrefteam2):
	for matchid in inpbfmap:
	    if inpbfmap[matchid]["datestr"]==inpdatestr:
		bfteams=get_match_teams(matchid)
		bfteam1=bfteams[0]
		bfteam2=bfteams[1]
		if bfteam1==inpteam1 or bfteam2==inpteam2 or bfteam1==xrefteam1 or bfteam2==xrefteam2:
		    return matchid
	return None


    @staticmethod
    def count_retmap(retmap):
	count=0
	for groupid,oddsmap in retmap.items():
	    for eventid in oddsmap:
		for oddskey,oddsvalue in oddsmap[eventid].items():
		    count=count+1
	return count

    @staticmethod
    def append_retmap(prelmap,retmap):
	for groupid,oddsmap in prelmap.items():
	    if retmap.has_key(groupid)==False:
		retmap[groupid]={}
	    for eventid in oddsmap:
		if retmap[groupid].has_key(eventid)==False:
		    retmap[groupid][eventid]={}
		for oddskey,oddsvalue in oddsmap[eventid].items():
		    retmap[groupid][eventid][oddskey]=oddsvalue

    def _fetch_xml(self,url):
	if runenv=="gae":
	    for x in range(3):
		try:
		    result=urlfetch.fetch(url=url,deadline=10)
		    result=result.content
		    break
		except:
		    result=None
	    return result
	    

    def process_xml_id(self,idmap,ts=None,filtermap={},inpxml=None):
      	for url in self.urllist:
	    if inpxml==None:
		rawxml=self._fetch_xml(self.get_url_ts(url,ts))
	    else:
		rawxml=inpxml
	    if rawxml==None:
		return idmap
	    bmmap=self.parse_xml_id(rawxml)
	    for datestr in bmmap:
		for teamtuple in bmmap[datestr].keys():
		    inpteam1=teamtuple[0]
		    inpteam2=teamtuple[1]
		    xrefteam1=self.get_team_xref(inpteam1)
		    xrefteam2=self.get_team_xref(inpteam2)    
		    bfmatchid=FeedUtil.match_teams(idmap,datestr,inpteam1,inpteam2,xrefteam1,xrefteam2)		  
		    if bfmatchid!=None:
			if idmap[bfmatchid].has_key(self.sourceid)==False:
			    idmap[bfmatchid][self.sourceid]={}
			idmap[bfmatchid][self.sourceid]["FT"]=bmmap[datestr][teamtuple]["FT"]
		    else:
			pass
	return idmap

    def process_xml(self,idmap,ts=None,filtermap={},inpxml=None):
	retmap={}
	rawxml=None
	for url in self.urllist:
	    if inpxml==None:
		rawxml=self._fetch_xml(self.get_url_ts(url,ts))
	    else:
		rawxml=inpxml
	    if rawxml==None:
		return None
	    prelmap=self.parse_xml(rawxml,idmap=idmap,filtermap=filtermap)
	    #logging.info(self.sourceid+"-"+str(FeedUtil.count_retmap(prelmap)))
	    FeedUtil.append_retmap(prelmap,retmap)
	self.feedts=self.get_feed_ts(rawxml)
	#logging.info("records before post process-"+self.sourceid+"-"+str(FeedUtil.count_retmap(retmap)))
	self.post_process(retmap)
	#logging.info("records after post process-"+self.sourceid+"-"+str(FeedUtil.count_retmap(retmap)))
	return retmap

    def get_team_xref(self,inpname):
	return self.teammap.get(inpname,None)


    def get_tour_xref(self,inpname):
	return self.tourmap.get(inpname,None)
		
    def get_url_ts(self,url,ts):      
	return url
      
    def parse_xml(self,inpxml,idmap=None,filtermap=None):
	pass

    def parse_xml_id(self,inpxml):
	pass
      
    def get_feed_ts(self,inpxml):
	return ""
           
    def post_process(self,inpmap):
	pass
      
