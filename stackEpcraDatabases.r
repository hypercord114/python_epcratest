script_name.var="stackEpcraDatabases"
dataDate.var="2024-06-21"
#
#
# Self
# Title:  Stack EPCRA databases and conglomerate into single file
# Author:  K. Navagh
# Date Created:  2024-06-21
# Date Last Updated:  
#
# Summary:  XXX
#

#=================================================
# Begin 'Reading data into R'

# Initialize route variable
route.strVar="C:/Users/kelna/Documents/pythonTest/"

# Read in data files to initialize dataframes
appa_raw.df=read.csv(paste(route.strVar,"appA.csv",sep=""),header=TRUE,sep=",",as.is=TRUE)
appb_raw.df=read.csv(paste(route.strVar,"appB.csv",sep=""),header=TRUE,sep=",",as.is=TRUE)

# End 'Reading data into R'
#=================================================



#=================================================
# Begin 'Data pre-processing'

#--------------------
# stack dataframes, loop over CAS numbers, set lowest value for repQuant vector, and rewrite dataframe without duplicates
appa_raw.df$source="app A"
appb_raw.df$source="app B"

appStack.df=rbind(appa_raw.df,appb_raw.df)

info.df=data.frame(casNum=unique(appStack.df$casNum),
					chemName=NA,
					repQuant=NA,
					planQuant=NA,
					rep_appa=NA,
					rep_appb=NA,
					higher=NA)

for(cas.looper in unique(appStack.df$casNum)) {

	sub.df=appStack.df[appStack.df$casNum==cas.looper,]
	
	info.df$rep_appa[info.df$casNum==cas.looper]=sub.df$repQuant[sub.df$source=="app A"]
	info.df$rep_appb[info.df$casNum==cas.looper]=sub.df$repQuant[sub.df$source=="app B"]

	# qualifier stuff
	if(info.df$rep_appa[info.df$casNum==cas.looper]>info.df$rep_appb[info.df$casNum==cas.looper]) {
		if(sub.df$planQuant[sub.df$source=="app A"]==sub.df$planQuant[sub.df$source=="app B"]) {
			info.df$higher[info.df$casNum==cas.looper]="appa"
			info.df$chemName[info.df$casNum==cas.looper]=sub.df$chemName[sub.df$source=="app A"]
			info.df$repQuant[info.df$casNum==cas.looper]=sub.df$repQuant[sub.df$source=="app A"]
			info.df$planQuant[info.df$casNum==cas.looper]=sub.df$planQuant[sub.df$source=="app A"]
		}
		else {
			info.df$higher[info.df$casNum==cas.looper]="appa, planQuant*"
		}
	}

	if(info.df$rep_appa[info.df$casNum==cas.looper]<info.df$rep_appb[info.df$casNum==cas.looper]) {
		if(sub.df$planQuant[sub.df$source=="app A"]==sub.df$planQuant[sub.df$source=="app B"]) {
			info.df$higher[info.df$casNum==cas.looper]="appb"
			info.df$chemName[info.df$casNum==cas.looper]=sub.df$chemName[sub.df$source=="app B"]
			info.df$repQuant[info.df$casNum==cas.looper]=sub.df$repQuant[sub.df$source=="app B"]
			info.df$planQuant[info.df$casNum==cas.looper]=sub.df$planQuant[sub.df$source=="app B"]
		}
		else {
			info.df$higher[info.df$casNum==cas.looper]="appb, planQuant*"
		}
	}

	if(info.df$rep_appa[info.df$casNum==cas.looper]==info.df$rep_appb[info.df$casNum==cas.looper]) {
		if(sub.df$planQuant[sub.df$source=="app A"]==sub.df$planQuant[sub.df$source=="app B"]) {
			info.df$higher[info.df$casNum==cas.looper]="same"
			info.df$chemName[info.df$casNum==cas.looper]=sub.df$chemName[sub.df$source=="app A"]
			info.df$repQuant[info.df$casNum==cas.looper]=sub.df$repQuant[sub.df$source=="app A"]
			info.df$planQuant[info.df$casNum==cas.looper]=sub.df$planQuant[sub.df$source=="app A"]
		}
		else {
			info.df$higher[info.df$casNum==cas.looper]="same, planQuant*"
		}
	}

}

# write file
write.csv(info.df,file=paste(route.strVar,script_name.var,"_",dataDate.var,".csv",sep=""))
#--------------------


# End 'Data pre-processing'
#=================================================