def pendapatan(nilai):        
          if (0<=nilai and 0.4>=nilai):
                    low=1
                    mid=0
                    midhigh=0
                    high=0
          elif (0.4<nilai and 0.6>nilai):
                low=(0.6-nilai)/0.2
                mid=(nilai-0.4)/0.2
                midhigh=0
                high=0
          elif (0.6<=nilai and 1>=nilai):
                    low=0
                    mid=1
                    midhigh=0
                    high=0
          elif (1<nilai and 1.2>nilai):
                    low=0
                    mid=(1.2-nilai)/0.2
                    midhigh=(nilai-1)/0.2
                    high=0
          elif (1.2<=nilai and 1.6>=nilai):
                    low=0
                    mid=0
                    midhigh=1
                    high=0
          elif (1.6<nilai and 1.8>nilai):
                    low=0
                    mid=0
                    midhigh=(1.8 - nilai)/0.2
                    high=(nilai - 1.6)/0.2
          elif (1.8<=nilai and 2>=nilai):
                    low= 0
                    mid= 0
                    midhigh=0
                    high=1
          return (low,mid,midhigh,high)

def hutang(nilai2):
          if (0<=nilai2 and 20>=nilai2):
                    low2= 1
                    mid2= 0
                    midhigh2=0
                    high2=0
          elif (20<nilai2 and 30>nilai2):
                    low2= (30-nilai2)/10
                    mid2= (nilai2-20)/10
                    midhigh2=0
                    high2=0
          elif (30<=nilai2 and 50>=nilai2):
                    low2= 0
                    mid2= 1
                    midhigh2=0
                    high2=0
          elif (50<nilai2 and 60>nilai2):
                    low2= 0
                    mid2= (60-nilai2)/10
                    midhigh2=(nilai2-50)/10
                    high2=0
          elif (60<=nilai2 and 80>=nilai2):
                    low2= 0
                    mid2= 0
                    midhigh2=1
                    high2=0
          elif (80<nilai2 and 90>nilai2):
                    low2= 0
                    mid2= 0
                    midhigh2=(90-nilai2)/10
                    high2=(nilai2-80)/10
          elif (90<=nilai2 and 100>=nilai2):
                    low2= 0
                    mid2= 0
                    midhigh2=0
                    high2=1

          return (low2,mid2,midhigh2,high2)

def FuzzyRules(low,mid,midhigh,high,low2,mid2,midhigh2,high2):
          # 0 = tidak
          # 1 = ya
        if (0<low<=1 and 0<low2<=1):
                rules=1
                ya=low
                tidak=0
        elif (0<low<=1 and 0<mid2<=1):
                rules=1
                ya=low
                tidak=0
        elif (0<low<=1 and 0<midhigh2<=1):
                rules=1
                ya=low
                tidak=0
        elif (0<low<=1 and 0<high2<=1):
                rules=1
                ya=low
                tidak=0
        elif (0<mid<=1 and 0<low2<=1):
                rules=0
                tidak=mid
                ya=0                
        elif (0<mid<=1 and 0<mid2<=1):
                rules=1
                ya=mid
                tidak=0
        elif (0<mid<=1 and 0<midhigh2<=1):
                rules=1
                ya=mid
                tidak=0
        elif (0<mid<=1 and 0<high2<=1):
                rules=1
                ya=mid
                tidak=0
        elif (0<midhigh<=1 and 0<low2<=1):
                rules=0
                tidak=midhigh
                ya=0
        elif (0<midhigh<=1 and 0<mid2<=1):
                rules=0
                tidak=midhigh
                ya=0
        elif (0<midhigh<=1 and 0<midhigh2<=1):
                rules=1
                ya=midhigh
                tidak=0
        elif (0<midhigh<=1 and 0<high2<=1):
                rules=1
                ya=midhigh
                tidak=0
        elif (0<high<=1 and 0<low2<=1):
                rules=0
                tidak=high
                ya=0
        elif (0<high<=1 and 0<mid2<=1):
                rules=0
                tidak=high
                ya=0
        elif (0<high<=1 and 0<midhigh2<=1):
                rules=0
                tidak=high
                ya=0
        elif (0<high<=1 and 0<high2<=1):
                rules=1
                ya=high
                tidak=0
        return (rules,ya,tidak)

def sugeno(nilai1,nilai2):
        return (nilai1*70)+(nilai2*50)/(nilai1+nilai2)
        
#main
import csv

pend = [];
htg = [];
csvFile = csv.reader(open("DataTugas2.csv"))
for row in csvFile:
        pend.append(row[1]);
        htg.append(row[2]);
i=1
n=1
data=[]
j=0
while i <= 100:
        low,mid,highmid,high = pendapatan(float(pend[i]))
        low2,mid2,highmid2,high2 = hutang(float(htg[i]))
        rules,ya,tidak = FuzzyRules(low,mid,highmid,high,low2,mid2,highmid2,high2)
        z=sugeno(ya,tidak)
        if (z>=70 and n<=20):
                print("No :",i," BLT : YES, Data Ke-",n)
                data.insert(n,i)
                n=n+1
        i=i+1

f = open('TebakanTugas2.csv', 'w')
with f:
    writer = csv.writer(f,lineterminator='\n')
    for val in data:
        writer.writerow([val])

