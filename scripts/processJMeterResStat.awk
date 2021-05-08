BEGIN{FS=":"}
ARGIND==1{
    if(index($0,"transaction")){
	    t1=substr($2,3,index($2,",")-4);
	}; 
	if(index($0,"meanResTime")){
	    trans1[t1]=substr($2,1,index($2,",")-1);
	}
}
ARGIND==2{
    if(index($0,"transaction")){
	    t2=substr($2,3,index($2,",")-4);
	}; 
	if(index($0,"meanResTime")){
	    trans2[t2]=substr($2,1,index($2,",")-1);
	}
}
END{
    asorti(trans1,strans1);
    printf("%-50s\t%s\n", "Transactions","Prev\tCurrent\tDiff");
	print "------------------------------------------------------------------------------";
    for(x in strans1){
	    key=strans1[x]
	    printf("%-50s\t%.2f\t%.2f\t%.2f%%\n", key,trans1[key],trans2[key],((trans2[key]-trans1[key])/trans1[key])*100);
	}
}